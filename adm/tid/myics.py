import arrow
import functools
import ics.icalendar
import nytid.schedules as sched
import nytid.schedules.utils as utils
import os
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

def add_reserve_to_title(ta, event):
    """
    Input: an event in CSV form.
    Ouput: the same CSV data, but with title prepended "RESERVE: " if TA is 
    among the reserves.
    """
    _, reserves = utils.get_booked_TAs_from_csv(event)
    if ta in reserves:
        event[0] = "RESERVE: " + event[0]

    return event

def generate_schedule():
    """Generates schedule, uses sys.args or USER environment variable, returns 
    schedule as ics.icalendar.Calendar object"""

    schedule_csv = []

    for course, url in SIGNUP.items():
        schedule_csv += utils.read_signup_sheet_from_url(url)

    if len(sys.argv) < 2:
        user = os.environ["USER"]
    else:
        user = sys.argv[1]

    schedule_csv = utils.filter_events_by_TA(user, schedule_csv)
    schedule_csv = map(functools.partial(add_reserve_to_title, user), 
            schedule_csv)

    schedule = ics.icalendar.Calendar()
    schedule.events |= set(map(utils.EventFromCSV, schedule_csv))

    return schedule


def main():
    """Main program"""
    print(generate_schedule())


if __name__ == "__main__":
    main()
