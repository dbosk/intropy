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

def generate_schedule():
    """Generates schedule, uses sys.args, returns schedule
    as ics.icalendar.Calendar object"""

    schedule = ics.icalendar.Calendar()

    if len(sys.argv) > 1:
        schedule.events |= set(map(utils.EventFromCSV,
                utils.read_signup_sheet_from_url(SIGNUP[sys.argv[1]])))
    else:
        for course, url in SIGNUP.items():
            schedule.events |= set(map(utils.EventFromCSV,
                utils.read_signup_sheet_from_url(url)))

    return schedule


def main():
    """Main program"""
    schedule = generate_schedule()

    first = True
    time_limit = arrow.get(2022, 8, 29).shift(weeks=+4)

    for event in schedule.timeline:
        if first:
            first = False
            current_week = event.begin.isocalendar()[1]
        elif event.begin.isocalendar()[1] != current_week:
            current_week = event.begin.isocalendar()[1]
            print()

        """
        if event.begin > time_limit:
            break
        """

        print(sched.format_event_short(event))


if __name__ == "__main__":
    main()
