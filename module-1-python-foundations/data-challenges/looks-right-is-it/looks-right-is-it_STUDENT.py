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

# Step 1, answer 1:
#
# Step 1, answer 2:
#
# Step 1, answer 3:
#


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


# Step 2, answer 1:
#
# Step 2, answer 2:
#
# Step 2, answer 3:
#


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

# Step 3, answer 1:
#
# Step 3, answer 2:
#
# Step 3, answer 3:
#


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

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
