import nytid.schedules.utils as utils

COURSES = {
        "DD1310": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=453080.10&e=220609&enol=t&ku=29&k=1B9F3AD696BCA5C434C68950EFD376DD",
        "DD1317": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=455995.10&e=220609&enol=t&ku=29&k=BA4400E3C003685549BC65AD9EAD3DC58E"
        }

def to_hours(td):
    return td.total_seconds()/60/60

def needed_TAs(event):
    if "Övning" in event.name and event.begin.weekday() in [3, 4]:
        return 1
    elif "laboration" in event.name or "Laboration" in event.name:
        return event.description.split().count("grupp")
    return utils.needed_TAs(event)

for course, url in COURSES.items():
    utils.generate_signup_sheet(course, url, needed_TAs)


prgi22booked = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/1GfwYBTJ2_D8TDap6HpWvoXuEP_lOMRTRnahCiXTk3hE/edit#gid=1060580342"))

#prgi22 = utils.read_signup_sheet_from_file("DD1317.csv")
prgi22 = prgi22booked

prgm22booked = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/18-afYjlI--e8hDwzSp9VcHjatc7SPvBFW0fH9JRrZ-4/edit#gid=1755336853"))

#prgm22 = utils.read_signup_sheet_from_file("DD1310.csv")
prgm22 = prgm22booked

prgi22tuts = filter(lambda x: "Övning" in x[0], prgi22)
prgi22labs = filter(
        lambda x: "laboration" in x[0] or "Laboration" in x[0],
        prgi22)

h_per_student = utils.hours_per_student(prgi22)

print("# prgi22")

for event, hours in h_per_student.items():
    print(f"{event}: {to_hours(hours)} h/student")

print(f"Booked: {to_hours(utils.total_hours(prgi22booked))} h "
        f"({to_hours(utils.max_hours(prgi22))} h)\n")


prgm22tutorials = filter(lambda x: "Övning" in x[0], prgm22)
prgm22labs = filter(
        lambda x: "laboration" in x[0] or "Laboration" in x[0],
        prgm22)

h_per_student = utils.hours_per_student(prgm22)

print("# prgm22")

for event, hours in h_per_student.items():
    print(f"{event}: {to_hours(hours)} h/student")

print(f"Booked: {to_hours(utils.total_hours(prgm22booked))} h "
        f"({to_hours(utils.max_hours(prgm22))} h)\n")


print("# Amanuenser")
amanuensis = utils.compute_amanuensis_data(prgi22 + prgm22)
for user, data in amanuensis.items():
    if not user:
        continue
    print(f"{user}: {data[2]:.2f} h, "
          f"{100*utils.compute_percentage(*data):.1f}%: "
          f"{data[0].format('YYYY-MM-DD')}--{data[1].format('YYYY-MM-DD')}")

print()
print("# Hourly")
for user, hours in utils.hours_per_TA(prgi22 + prgm22).items():
    if not user or user in amanuensis:
        continue
    print(f"{user}: {to_hours(hours):.2f} h")


