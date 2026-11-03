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
for row in rows:
    try:
        
# TODO: assign `total_days` and `counted` to 0
# TODO: loop over `rows`; `continue` past any row validate_request() rejects
days_open = int(row[4])
# TODO: assign `days_open` to int() of the row's fourth field
total_days + days_open
counted +=1
# TODO: add `days_open` to `total_days` and 1 to `counted`
print(f'days open: {days_open}
# TODO: print the row's ID, "days open:" and `days_open`
# TODO: after your answers, comment out this step so Step 4 can run

print("average days open:", total_days / counted)

# Step 3, answer 1:
#
# Step 3, answer 2:
#
# Step 3, answer 3:
#


# Step 4: Rebuild the Report So Every Row Is Counted or Skipped
def check_days_open(value):
    # TODO: in a try, assign `days` to int(value)
    # TODO: in except ValueError, return False and a reason
    # TODO: make that reason "days_open is not a number: " plus `value`
    # TODO: if `days` is below 0, return False and a reason
    # TODO: make that reason "days_open is negative: " plus `value`
    # TODO: return True and "ok"
    pass


# TODO: assign `total_days`, `counted` and `skipped` to 0
# TODO: loop over `rows`; unpack validate_request(row) into ok, reason
# TODO: if ok, unpack check_days_open() of the fourth field into ok, reason
# TODO: if still ok, add the days to `total_days` and 1 to `counted`
# TODO: else add 1 to `skipped`; print the ID, "SKIPPED -" and `reason`

print("counted:", counted, "| skipped:", skipped)
print("average days open:", round(total_days / counted, 1))

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
