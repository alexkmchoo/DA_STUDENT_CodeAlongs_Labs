#!/usr/bin/env python3
"""Validate, Catch, Keep Going: see DataChallengeOverview&Steps.md."""

DATA_FILE = "/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/service_requests.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
    lines = f.read().splitlines()

header = lines[0]
rows = [line for line in lines[1:] if line]


# ===== Day 1 =====

# Step 1: Write `validate_request()` to Return a Verdict and a Reason
# TODO: assign `EXPECTED_FIELDS` to 5
# TODO: assign `ALLOWED_STATUS` to ["Open", "In Progress", "Closed"]

ALLOWED_STATUS = ["Open", "In Progress", "Closed"]
EXPECTED_FIELDS = 5
def validate_request(row):
    fields = row.split(',')
    # assign `fields` to `row` split on commas
    if len(fields) != EXPECTED_FIELDS:
        return False, "wrong field count: " + str(len(fields))
    request_id, complaint_type, borough, days_open, status = fields
    # unpack `fields` into the five names in the CSV header
    if borough == '':
        return False, "borough is empty"
    # if `borough` is empty, return False and "borough is empty"
    if status not in ALLOWED_STATUS:
        return False, "status not allowed: " + status
    # if `status` is not in ALLOWED_STATUS, return False and a reason
    # make that reason "status not allowed: " plus `status`
    return True, "ok"
    # return True and "ok"


print(validate_request("SR-1001,Noise - Residential,Brooklyn,3,Closed"))
print(validate_request("SR-1004,Rodent,,6,Closed"))
print(validate_request("SR-1009,Water System,Queens,4,Escalated"))

# Step 1, answer 1: Before you code: two or three sentences on what is in the file. What does one row hold, and what already looks wrong?
# One row holds the data on the request id, what complaint it is, which borough its in, how many days the issue has been open, and whether the complaint is open, closed, or in progress.
# There is missing values in borough and status. There are also different data types in days open : "3 days" and a negative value as well. There is an escalted data value in SR1009 as well.
# Step 1, answer 2: How does the caller take the two returned values apart in one line, and what is the function really handing back?
# The caller takes two returned values apart in one line through the comma. The function is really handing back a single tuple that contains two values, which is the boolean and the string.


# Step 2: Run All 15 Rows Through the Validator and Report Each Rejection
valid = 0
# assign `valid` to 0 
for row in rows:
    ok, reason = validate_request(row)
    # loop over `rows`; unpack validate_request(row) into ok, reason
    if ok:
        valid += 1
        # if `ok`, add 1 to `valid`
    else:
        print(row.split(",")[0], "REJECTED - " + reason)
# else print row.split(",")[0], "REJECTED -" and `reason`

print("header:", header)
print("rows read:", len(rows))
print("passed Day 1 validation:", valid)

# Step 2, answer 1: Before you run: how many rows fail your three rules by your own hand count, and which rule does each break?
# I would expect 3 rows to fail. SR 1004 is missing a value. SR1009's status value is outside our label : Open, In progress, and closed. I would also expect SR 1011 to fail too because its missing a value in the status column. 
# Step 2, answer 2: Read the rows that passed. Which ones got through that should not have, and why can your validator not see them?
# SR 1007 passed that shouldn't have because it's unstructured data, it's 3 days instead of 3 like the other values. SR 1013 shouldn't have as well, it should have as well because it has a negative value.
# The validator can't see SR1007 and SR1013 because it never evaluates the days_open column, so both structured and unstructured data types can pass.

# ===== Day 2 =====

# Step 3: Build the Days-Open Report With No Protection and Watch It Crash
total_days = 0
counted = 0
# assign `total_days` and `counted` to 0
for row in rows:
    ok, reason = validate_request(row)
    if not ok: 
        continue
    x = row.split(',')
# loop over `rows`; `continue` past any row validate_request() rejects
    days_open = int(x[3])
# assign `days_open` to int() of the row's fourth field
    total_days += days_open
    counted +=1
# add `days_open` to `total_days` and 1 to `counted`
    print(x[0], "Days open:", days_open)
# print the row's ID, "days open:" and `days_open`
# after your answers, comment out this step so Step 4 can run

print("average days open:", total_days / counted)

# Step 3, answer 1: Before you run: how many report lines print before it crashes, and which row stops it?
# 5 report lines will print. row 7 stops it because there will be a value error. It skips SR1004 because there is a missing borough value.
# Step 3, answer 2: The last line of the traceback, exactly as printed, and how many rows were counted before it.
# ValueError: invalid literal for int() with base 10: '3 days'
# 7 rows were counted before the error.
# Step 3, answer 3: What happens to the rows the loop never reached?
# The code crashes, so it never reaches the remaining 8 rows, which are the unprocessed rows, after the error. 
# This means that the total_days and counted stop part way and also means the average is also never reached because the line is never reached


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    try:
        days = int(value)
        # in a try, assign `days` to int(value)
    except ValueError:
        return False, "days_open is not a number: " + value
        # in except ValueError, return False and a reason "days_open is not a number: " plus `value`
    if days < 0:
        return False, "days_open is negative: " + value
        # if `days` is below 0, return False and a reason "days_open is negative: " plus `value`
    return True, "ok"
        # return True and "ok"

# Before running: I predict that it will get caught by the try except ValueError. Since 7.8 is a decimal and 
# int only takes whole numbers, so it will raise
print(check_days_open("7.8"))
print(check_days_open("5"))
# Rubric exceed step : tests one more bad days_open value and predicts which tool catches it before running.


def check_complaint_type(value):
    if value == "":
        return False, "complaint type is empty"
    return True, "ok"

total_days = 0
counted = 0
skipped = 0
# assign `total_days`, `counted` and `skipped` to 0
for row in rows:
    ok, reason = validate_request(row)
    # loop over `rows`; unpack validate_request(row) into ok, reason
    if not ok:
        print(row.split(",")[0], "SKIPPED - " + reason)
        # else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`
        skipped +=1
        continue
    fields = row.split(',')
    ok, reason = check_days_open(fields[3])
    # if ok, unpack check_days_open() of the fourth field into ok, reason
    if not ok:
        print(fields[0], "SKIPPED - " + reason)
        # else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`
        skipped += 1
        continue
    ok, reason = check_complaint_type(fields[1])
    # Rubric exceed step : adds a third check function for another field and calls it in the Step 4 loop.
    if not ok:
        print(fields[0], "SKIPPED - " + reason)
        # else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`
        skipped += 1
        continue
    days_open = int(fields[3])
    total_days += days_open
    counted += 1
    # if still ok, add the days to `total_days` and 1 to `counted`
total = counted + skipped

print("counted:", counted, "| skipped:", skipped, "| total:", total)
print("average days open:", round(total_days / counted, 1))

if counted + skipped != len(rows):
    print(f"Warning! total does not equal: {len(rows)}")
    # Rubric exceed step : adds code that prints a warning when counted plus skipped is not the row count.

# Step 4, answer 1: Before you run: how many rows get skipped now, and which ones did your Day 1 validator let through?
# 5 rows get skipped. The Day 1 validator lets 2 through (SR 1007 and SR 1013).
# Step 4, answer 2: For 3 days and for -3: did an if or a try catch it, and could the other tool have?
# The try/expect catches this, 3 days it not an int and we stated in the function if days < 0 , which a negative value is.
# Step 4, answer 3: Does counted plus skipped account for every row? Show the sum.
# Yes, this was the output : counted: 10 | skipped: 5 | total: 15 