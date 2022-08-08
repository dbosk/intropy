import arrow
import calendar
import dateutil
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

def format_header(event):
    """Formats the event header"""
    header = f"Week {event.begin.isocalendar()[1]} " + \
            calendar.day_name[event.begin.weekday()] + " " + \
            event.begin.to(dateutil.tz.tzlocal()).format('DD/MM HH:mm')

    if "DD1317" in event.name or "DD1310" in event.name:
        header += f" {event.name.split(',')[0]}"
    else:
        header += f" {event.name}"

    return header

def format_event(event):
    """Takes event (ics.event.Event) object,
    returns string representation"""
    header = format_header(event)
    location = event.location
    description = "\n".join(filter(lambda x: "http" not in x,
            event.description.splitlines()))

    return f"{header}\n{location}\n{description}".strip()

def filter_event_description(event_desc):
    """Takes event description event_desc as string,
    returns filtered string"""

    desc_parts = event_desc.splitlines()
    desc_parts_keep = []

    for part in desc_parts:
        if "http" in part:
            continue
        elif "grupp" in part:
            continue
        elif "ID " in part:
            continue
        elif "CINEK" in part:
            continue
        elif "Daniel Bosk" in part:
            continue

        desc_parts_keep.append(part)

    return " ".join(desc_parts_keep)

def format_event_short(event):
    """Takes event (ics.event.Event) object,
    returns string representation"""
    header = format_header(event)
    description = filter_event_description(event.description)

    return f"{header} {description}".strip()



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

        print(format_event_short(event))


if __name__ == "__main__":
    main()
