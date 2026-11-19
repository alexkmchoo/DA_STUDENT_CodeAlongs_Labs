#!/usr/bin/env python3
"""Looks Right. Is It?: see DataChallengeOverview&Steps.md for the steps."""

DATA_FILE = "/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/timesheet_hours.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()


# ===== Day 1 =====

# Step 1: Follow the TypeError in `weekly_hours()` Back to Its Cause
# run the file as given and read the traceback from the bottom up
# add print(repr(hours)) as the first line of add_hours(); run again >> Mon
# find that printed value in the CSV >> day
def add_hours(total, hours):
    # print(repr(hours))
    # delete the print(repr(hours)) line once Rosa's total is right
    return total + hours

def weekly_hours(lines, emp_id):
    total = 0
    for row in lines[1:]:
        parts = row.split(",")
        if parts[0] == emp_id:
            total = add_hours(total, int(parts[3]))
            # fix the line that reads the wrong column to read the hours column
            # wrap that value in int() so add_hours() adds a number
    return total


print("Rosa Alvarez, weekly hours:", weekly_hours(lines, "E101"))


# writes one test call per bug that fails before the fix and passes after.
print(weekly_hours(lines, "E104"))
print(weekly_hours(lines, "E103")) 

# Step 1, answer 1: Before you run: Rosa's weekly hours (E101), added up by hand from the CSV.
# 40

# Step 1, answer 2: How to read a traceback, in 2-3 bullets: what the last line tells you, what each block above it tells you, and where you found that out.
# The last line tells me there is a TypeError. We can't add an int and a str.
# Each block above it tells me which line has an error. For example, I get an error in line 6 and another on 12 (because 12 calls 6)
# I found it in my output. It tells me which line the error occurs in (Jupyter Notebook helps clean up the output a lot)

# Step 1, answer 3 : Which function the traceback ended in, and which line really held the bug.
# The traceback ended in add_hours. return total + hours tells us we are performing arthmetic, so we must add ints.
# this also means that the str is coming from below, which is in total = add_hours(total, parts[2])
# parts[2] is a str because it calls the day and not the hours.


# Step 2: Trace the ZeroDivisionError Back to the Hand-Typed Staff List
# run the file as given; note the last ID that printed >> E103
# compare every ID in `staff` with the IDs in the CSV >> There is no E106
def days_worked(lines, emp_id):
    days = 0
    for row in lines[1:]:
        if row.split(",")[0] == emp_id:
            days = days + 1
    return days

staff = []
# replace the hand-typed `staff` list with an empty list
for row in lines[1:]:
    emp_id = row.split(",")[0]
    if emp_id not in staff:
        staff.append(emp_id)
        # loop over lines[1:]; append each row's employee ID to `staff` once
print("employees in the file:", len(staff))
# print "employees in the file:" and len(staff)
if len(staff) != 5:
    print("Warning! The number of employees does not match the number of employees in the file")
    # adds a check that prints a warning when len(staff) differs from the employees in the file.

for emp_id in staff:
    hours = weekly_hours(lines, emp_id)
    days = days_worked(lines, emp_id)
    print(emp_id, "| hours:", hours, "| days:", days,
          "| average per day:", hours / days)


# Step 2, answer 1: Before you run: how many employees are in the CSV, counted by eye?
# 5
# Step 2, answer 2: How many lines printed before the crash, and which ID did it stop on?
# 3 lines printed before the crash. It stopped on E103
# Step 2, answer 3: Where the bug lives, in the division line or somewhere above it, and why, in one sentence.
# No, the bug lives above the division line in the Staff because 106 doesn't exist, it hands back 0, which is why we are getting 
# a ZeroDivisionError


# ===== Day 2 =====

# Step 3: Find Why Four of the Five Weekly Hour Totals Are Wrong
# add up Rosa's (E101) and Mei's (E103) hours by hand first >> Rosa : 40 | Mei : 32
records = []
for row in lines[1:]:
    emp_id, name, day, hours, rate = row.split(",")
    records.append({"id": emp_id, "name": name, "day": day,
                    "hours": int(hours), "rate": float(rate)})



employee_ids = []
for r in records:
    if r["id"] not in employee_ids:
        employee_ids.append(r["id"])


for emp in employee_ids:
    total = 0
    # move the line that sets `total` inside the outer loop
    name = ""
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            total = total + r["hours"]
    print(emp, name, "| weekly hours:", total)

# Step 3, answer 1: Before you run: Rosa's and Mei's weekly hours, added up by hand from the CSV.
# Rosa : 40 | Mei : 32

# Step 3, answer 2: What total held at the start of each employee's count, and the one line that explains it.
# Rosa : 40 | Darnell : 86 | Mei : 118 | Samuel : 156 | Priya : 200
# total = 0 explains it. We are doing it outside the for loop

# Step 3, answer 3: Why is Rosa's number right while Priya's equals the whole staff's hours for the week
# total is set to 0 regardless. But the difference for the other employees is that it doesn't reset and adds onto the previous 
# employee total.


# Step 4: Fix Two Overtime Bugs That Overpay the Firm by $1,810 a Week
# Rosa : $960 | Darnell : $1,543.50 | Mei : $896 |  Samuel : $836 | Priya : $1,610
# Exceeds rubric step : works out all five employees' pay by hand, not just the three the steps name.
#  work out Rosa's, Darnell's and Mei's pay by hand first
def weekly_pay(hours, rate):
    if hours > 40:
        return (40 * rate) + (hours - 40) * 1.5 * rate
        # fix weekly_pay() so it follows the handbook rule word for word
    return hours * rate

owed_overtime = 0
payroll = 0.0
for emp in employee_ids:
    total = 0
    name = ""
    rate = 0.0
    for r in records:
        if r["id"] == emp:
            name = r["name"]
            rate = r["rate"]
            total = total + r["hours"]
    if total > 40:
        # fix the other line that compares `total` against 40 the same way
        owed_overtime = owed_overtime + 1
    pay = weekly_pay(total, rate)
    payroll = payroll + pay
    print(f"{name:16} {total:3} hrs  ${pay:>9,.2f}")

print("employees owed overtime:", owed_overtime)
print(f"TOTAL PAYROLL: ${payroll:,.2f}")

# writes one test call per bug that fails before the fix and passes after.
print(weekly_pay(40, 24))
print(weekly_pay(44, 35))

# Step 4, answer 1: Before you run: Rosa's, Darnell's and Mei's weekly pay, worked out by hand from the handbook rule.
# Rosa : $960 | Darnell : $1,543.50 | Mei : $896 
# Step 4, answer 2: The two bugs you found, each with its line and what you changed it to.
# The first bug : In line 134 return hours * rate * 1.5. I changed it to (40 * rate) + (hours - 40) * 1.5 * rate
# The first one counts all hours as overtime, but we just want every hour after 40 counted as overtime.
# The second bug(s) : >= Every hour after 40 counts as overtime, >= means 40 counts as well.
# This happens on line 133 if hours >= 40 , which I changed it into if hours > 40
# This also happens on line 150 if total >= 40, which I also changed it into if hours > 40

# Step 4, answer 3: Why can only Rosa's exactly-40 week catch one of the two bugs?
# Rosa's hours are exactly 40 and in our code we have hours set to >= 40, so she cacthes the overtime, even though she doesn't meet it
