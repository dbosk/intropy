import kthutils.ug
import os
from pprint import pprint
import nytid.schedules.utils as utils

COURSES = {
        "DD1310": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=453080.10&e=220609&enol=t&ku=29&k=1B9F3AD696BCA5C434C68950EFD376DD",
        "DD1317": 
        "https://cloud.timeedit.net/kth/web/public01/ri.ics?sid=7&p=0.w%2C12.n&objects=455995.10&e=220609&enol=t&ku=29&k=BA4400E3C003685549BC65AD9EAD3DC58E"
        }

prgi22 = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/1GfwYBTJ2_D8TDap6HpWvoXuEP_lOMRTRnahCiXTk3hE/edit#gid=1060580342"))

prgm22 = utils.read_signup_sheet_from_url(
        utils.google_sheet_to_csv_url(
            "https://docs.google.com/spreadsheets/d/18-afYjlI--e8hDwzSp9VcHjatc7SPvBFW0fH9JRrZ-4/edit#gid=1755336853"))

ug = kthutils.ug.UGsession(os.environ["KTH_LOGIN"], os.environ["KTH_PASSWD"])

members = []

for user in utils.hours_per_TA(prgi22 + prgm22):
    user_data = ug.find_user_by_username(user)
    if len(user_data) > 1:
        pprint(user_data)
        continue
    elif len(user_data) < 1:
        print(f"ug: can't find {user}")
        continue
    members.append(user_data[0]["kthid"])

prgi = next(ug.find_group_by_name("edu.courses.DD.DD1317.20222.1.assistants"))
ug.set_group_members(members, prgi["kthid"])

prgm = next(ug.find_group_by_name("edu.courses.DD.DD1310.20222.3.assistants"))
ug.set_group_members(members, prgm["kthid"])

