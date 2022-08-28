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

def events_missing_TAs(csv_rows, missing_factor=0.5):
    """
    Input: a list of CSV data (tuples)

    Output: a list of CSV data, only those rows where there are fewer TAs 
    booked than the number of needed TAs.
    """
    needed_TAs_index = utils.SIGNUP_SHEET_HEADER.index("#Needed TAs")

    for row in csv_rows:
        num_TAs = len(utils.get_TAs_from_csv(row))
        needed_TAs = int(row[needed_TAs_index])

        if num_TAs < missing_factor * needed_TAs:
            yield row


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
    return f"{sched.format_event_short(event)}\n" + \
            ", ".join([attendee.email for attendee in event.attendees])


def main():
    """Main program"""
    booking_data = []
    for _, url in SIGNUP.items():
        booking_data += utils.read_signup_sheet_from_url(url)

    schedule = generate_schedule(events_missing_TAs(booking_data))

    if len(sys.argv) > 1:
        try:
            time_limit = arrow.get(2022, 8, 29).shift(weeks=+int(sys.argv[1]))
        except ValueError as err:
            print(f"{sys.argv[0]}: {err}: "
                  f"first argument must be the number of weeks to print",
                  file=sys.stderr)
            sys.exit(1)

    first = True
    for event in schedule.timeline:
        if first:
            first = False
            current_week = event.begin.isocalendar()[1]
        elif event.begin.isocalendar()[1] != current_week:
            current_week = event.begin.isocalendar()[1]
            print(end="\n\n")

        try:
            if event.begin > time_limit:
                break
        except NameError:
            pass

        print(format_event(event), end="\n\n")


if __name__ == "__main__":
    main()
