import os
import requests
from datetime import date

print("""
    ┏┓┳┓┓┏┏┓┳┓┏┳┓  ┏┓┏┓  ┏┓┏┓┳┓┏┓
    ┣┫┃┃┃┃┣ ┃┃ ┃   ┃┃┣   ┃ ┃┃┃┃┣ 
    ┛┗┻┛┗┛┗┛┛┗ ┻   ┗┛┻   ┗┛┗┛┻┛┗┛
""")

r = requests.Session()
r.cookies.set("session", os.environ["AOC_SESSION_ID"])
YEAR, DAY = str(date.today().year), str(date.today().day)

def get_todays_input():
    with open(f"{YEAR}/day_{DAY.rjust(2, '0')}/input.txt", "wb") as f:
        f.write(r.get(f"https://adventofcode.com/{YEAR}/day/{DAY}/input").content)

    print("\033[1;32m[*] Downloaded todays' input\033[0m")


if YEAR not in os.listdir():
    os.mkdir(YEAR)

if (dir := f"day_{DAY.rjust(2, '0')}") not in os.listdir(YEAR):
    print("\033[1;32m[*] Created folder for today\033[0m")
    os.mkdir(f"{YEAR}/{dir}")
    get_todays_input()
