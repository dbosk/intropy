import arrow
import ics.icalendar
import nytid.schedules as sched
import nytid.schedules.utils as utils
import sys

COURSES = {
        "DD1310": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=453080.10&e=220609&enol=t&ku=29&k=1B9F3AD696BCA5C434C68950EFD376DD",
        "DD1317": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=455995.10&e=220609&enol=t&ku=29&k=BA4400E3C003685549BC65AD9EAD3DC58E"
        }

SIGNUP = {
        "DD1317": utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/1GfwYBTJ2_D8TDap6HpWvoXuEP_lOMRTRnahCiXTk3hE/edit#gid=1060580342"),
        "DD1310": utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/18-afYjlI--e8hDwzSp9VcHjatc7SPvBFW0fH9JRrZ-4/edit#gid=1755336853")
        }

def events_booked_TAs(csv_rows):
    """
    Input: a list of CSV data (tuples)

    Output: a list of CSV data, only containing booked TAs, excluding the 
    reserves.
    """
    for row in csv_rows:
        booked, _ = utils.get_booked_TAs_from_csv(row)
        yield row[:len(utils.SIGNUP_SHEET_HEADER)] + booked


def generate_schedule(csv_rows):
    """
    Generates schedule (ICS format) from a list of CSV rows,
    returns an ics.icalendar.Calendar object.
    """
    schedule = ics.icalendar.Calendar()
    schedule.events |= set(map(utils.EventFromCSV, csv_rows))

    return schedule


def format_event(event):
    """
    Returns a string representation of the event.
    """
    return f"{sched.format_event_short(event)}; " + \
            ", ".join([attendee.email for attendee in event.attendees])


def main():
    """Main program"""
    booking_data = []
    for _, url in SIGNUP.items():
        booking_data += utils.read_signup_sheet_from_url(url)

    schedule = generate_schedule(events_booked_TAs(booking_data))
    now = arrow.get(2022, 8, 29)
    if now < arrow.now():
        now = arrow.now()

    if len(sys.argv) > 1:
        try:
            time_limit = now.shift(weeks=+int(sys.argv[1]))
        except ValueError as err:
            print(f"{sys.argv[0]}: {err}: "
                  f"first argument must be the number of weeks to print",
                  file=sys.stderr)
            sys.exit(1)

    first = True
    for event in schedule.timeline:
        try:
            if event.end < now:
                continue
            elif event.begin > time_limit:
                break
        except NameError:
            pass

        if first:
            first = False
            current_week = event.begin.isocalendar()[1]
        elif event.begin.isocalendar()[1] != current_week:
            current_week = event.begin.isocalendar()[1]
            print(end="\n\n")

        print(format_event(event))


if __name__ == "__main__":
    main()
