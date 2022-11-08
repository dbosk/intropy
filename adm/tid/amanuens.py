import arrow
import csv
import nytid.schedules as sched
import nytid.schedules.utils as utils
import operator
import sys

COURSES = {
        "DD1310": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=453080.10&e=220609&enol=t&ku=29&k=1B9F3AD696BCA5C434C68950EFD376DD",
        "DD1317": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=455995.10&e=220609&enol=t&ku=29&k=BA4400E3C003685549BC65AD9EAD3DC58E"
        }

def to_hours(td):
    return td.total_seconds()/60/60

def shift_dates_forward(start_date, end_date):
    """Takes dates and shifts them so that start_date is tomorrow."""
    now = arrow.now()
    today = arrow.Arrow(now.year, now.month, now.day,
                        hour=start_date.hour, minute=start_date.minute,
                        second=start_date.second)

    if start_date > today:
        return start_date, end_date

    diff = (today-start_date).days
    return start_date.shift(days=diff+1), end_date.shift(days=diff+1)


if len(sys.argv) < 2:
    print(f"{sys.argv[0]}: requires argument 'username'",
          file=sys.stderr)
    print(f"{sys.argv[0]} <username> [<start date>]")
    sys.exit(1)
else:
    user = sys.argv[1]

if len(sys.argv) > 2:
    date = arrow.get(sys.argv[2])
else:
    date = None

prgi22 = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/1GfwYBTJ2_D8TDap6HpWvoXuEP_lOMRTRnahCiXTk3hE/edit#gid=1060580342"))

prgm22 = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/18-afYjlI--e8hDwzSp9VcHjatc7SPvBFW0fH9JRrZ-4/edit#gid=1755336853"))

amanuensis = utils.compute_amanuensis_data(prgi22 + prgm22,
                                           begin_date=date)
data = amanuensis[user]

#start, end = shift_dates_forward(data[0], data[1])
start = data[0]
end = data[1]

print(f"{user}: {data[2]:.2f} h, "
      f"{round(100*utils.compute_percentage(*data))}%: "
      f"{start.format('YYYY-MM-DD')}--{end.format('YYYY-MM-DD')}")

prgx = utils.filter_events_by_TA(user, sorted(prgi22 + prgm22,
         key=operator.itemgetter(utils.SIGNUP_SHEET_HEADER.index("Start"))))
prgx = filter(lambda x: user in utils.get_booked_TAs_from_csv(x)[0], prgx)
prgx = list(map(lambda x: x[0:len(utils.SIGNUP_SHEET_HEADER)] + [user], prgx))

for event, hours in utils.hours_per_event(prgx).items():
    print(f"{event}: {to_hours(hours)}")

print()

csvout = csv.writer(sys.stdout)

for event in prgx:
    csvout.writerow(event)
