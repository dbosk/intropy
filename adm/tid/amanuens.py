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

if len(sys.argv) < 2:
    print(f"{sys.argv[0]}: requires argument 'username'",
          file=sys.stderr)
    sys.exit(1)
else:
    user = sys.argv[1]

prgi22 = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/1GfwYBTJ2_D8TDap6HpWvoXuEP_lOMRTRnahCiXTk3hE/edit#gid=1060580342"))

prgm22 = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/18-afYjlI--e8hDwzSp9VcHjatc7SPvBFW0fH9JRrZ-4/edit#gid=1755336853"))

amanuensis = utils.compute_amanuensis_data(prgi22 + prgm22)
data = amanuensis[user]

print(f"{user}: {data[2]:.2f} h, {100*utils.compute_percentage(*data):.1f}%: "
      f"{data[0].format('YYYY-MM-DD')}--{data[1].format('YYYY-MM-DD')}")

prgx = utils.filter_events_by_TA(user, sorted(prgi22 + prgm22,
         key=operator.itemgetter(utils.SIGNUP_SHEET_HEADER.index("Start"))))
prgx = list(map(lambda x: x[0:len(utils.SIGNUP_SHEET_HEADER)] + [user], prgx))

for event, hours in utils.hours_per_event(prgx).items():
    print(f"{event}: {to_hours(hours)}")

print()

csvout = csv.writer(sys.stdout)

for event in prgx:
    csvout.writerow(event)
