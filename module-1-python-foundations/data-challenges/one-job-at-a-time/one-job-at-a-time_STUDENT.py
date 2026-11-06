#!/usr/bin/env python3
"""One Job at a Time: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/pantry_donations.csv"  # edit the filepath with the data


# ===== Day 1 =====

# Step 1: Write the Read-and-Validate Pair, Each With a Docstring
def read_donations(path):
    """Read the donation log into one raw string per record."""
    records = []
    with open(path) as f:
        for line in f.read().splitlines()[1:]:
            if line.strip():
                records.append(line)
    return records


def validate_donation(record):
    """Returns a verdict and reason of a record"""
    # add a one-sentence docstring naming its one job
    parts = record.split(',')
    # assign `parts` to `record` split on commas
    if len(parts) != 5:
        return False, "wrong field count"
    # return False, "wrong field count" if `parts` lacks 5 fields
    if parts[2].strip() == '':
        return False, "missing category"
    # return False, "missing category" if parts[2].strip() is ""
    try:
        float(parts[3])
        # in a try, call float(parts[3])
    except ValueError:
        return False, "pounds is not a number"
    # in except ValueError, return False, "pounds is not a number"
    return True, ''
# return True and ""



records = read_donations(DATA_FILE)
valid = []
# assign `records` to read_donations(DATA_FILE), `valid` to []
for record in records:
    ok, reason = validate_donation(record)
    # loop over `records`; unpack validate_donation(record) as ok, reason
    if ok:
        valid.append(record)
        # if `ok`, append `record` to `valid`
    else:
        print("rejected", record[:4], ":", reason)
    # else print "rejected", the record's ID plus ":", and `reason`

print(len(valid), "usable records out of", len(records))

# Step 1, answer 1: Before you code: what does one record hold, and which records already look wrong?
# One record holds the donation ID, item, category, pounds, and the date it was recieved on.
# There is a missing value in the category and recieved on column. There are unstructured data types in the pounds category.
# Step 1, answer 2: Name three things your validator promises about each record it keeps.
# it promises 5 columns, promises pounds has to be a number, and to catch any missing values.


# Step 2: Write `summarize_donations()` for the Category Breakdown Only
def summarize_donations(valid_records):
    '''summarize the count of the donation of the records into valid records, total pounds, and by category
    This function does not validate records'''
    # add a one-sentence docstring naming its one job
    # Rubric exceed step : plus one docstring states what its function is not responsible for, like validating records.
    by_category = {}
    total_pounds = 0.0
    # assign `by_category` to {} and `total_pounds` to 0.0
    for x in valid_records:
        parts = x.split(',')
        # loop over `valid_records`; split each record on commas into `parts`
        category = parts[2]
        pounds = float(parts[3])
        # assign `category` to parts[2], `pounds` to float(parts[3])
        if category not in by_category:
            by_category[category]= {"donations": 0, "pounds": 0.0} 
            # if `category` is not in `by_category`, add an entry for it start that entry as {"donations": 0, "pounds": 0.0}
        by_category[category]["donations"] += 1
        by_category[category]["pounds"] += pounds
        # add 1 to its "donations" and `pounds` to its "pounds" add `pounds` to `total_pounds`
        total_pounds += pounds
    return {"records": len(valid_records),
            "total_pounds": total_pounds,
            "by_category": by_category
    }
    # return a dict of "records", "total_pounds" and "by_category"


summary = summarize_donations(valid) 
# assign `summary` to summarize_donations(valid)

category_pounds = 0.0
for pound in summary["by_category"].values():
    category_pounds += pound["pounds"]
if category_pounds == summary["total_pounds"]:
       print(True, "check passed")
else:
        print(False, "category_pounds:", category_pounds, "do not match total pounds:", summary["total_pounds"])
# Rubric extra step : code checks that the category pounds add up to total_pounds.

print("records:", summary["records"], "| total pounds:",
      summary["total_pounds"])
for category, stats in summary["by_category"].items():
    print(category, stats["donations"], "donations,", stats["pounds"],
          "lbs")

# Step 2, answer 1: Hand-count one category's pounds off the CSV. Which category, what did you get, and does it match your printed line?
# Protein category. I got 15. It matches my printed line which was : protein 2 donations, 15.0 lbs


# ===== Day 2 =====

# Step 3: Add `export_summary()` and `run_pipeline()`, Then Print Docstrings
def export_summary(summary, path):
    """Exports the data to a JSON file"""
    # add a one-sentence docstring naming its one job
    with open(path, "w") as f:
        json.dump(summary, f, indent=2)
        # in a with open(path, "w") block, json.dump `summary`, indent=2
    return path
    # return `path`


def run_pipeline(in_path, out_path, summarize):
    """Running the donation pipeline read, validate, and summarize to an export"""
    # add a one-sentence docstring naming its one job
    kept = []
    for x in read_donations(in_path):
        # assign `kept` to [] and loop over read_donations(in_path)
        valid, reason = validate_donation(x)
        # append each record that validate_donation() passes to `kept`
        if valid:
            kept.append(x)
    return export_summary(summarize(kept), out_path)
    # return export_summary() of summarize(kept) and `out_path`


written = run_pipeline(DATA_FILE, "donation_summary.json",
                       summarize_donations)
print("wrote", written)
for func in [read_donations, validate_donation, summarize_donations,
             export_summary]:
    print(func.__name__ + ":", func.__doc__.splitlines()[0])
#print(len)
#print(len("abc"))

# Step 3, answer 1: What did print(len) and print(len("abc")) each print, and what do the parentheses do?
# print(len) : <built-in function len> , print(len("abc")) > 3
# The parentheses is the call operator, telling python to execute something.
# Step 3, answer 2: Read the four printed docstring lines with your partner. Does any one need "and" twice?
# none of them need and twice. They each have different functions as listed by the output
# read_donations: Read the donation log into one raw string per record.
# validate_donation: Returns a verdict or reason of a record
# summarize_donations: summarize the donation of the records into valid records, total pounds, and by category
# export_summary: Exports the data to a JSON file


# Step 4: Swap In `summarize_by_day()` and Count the Functions You Edited
def summarize_by_day(valid_records):
    """Summarizes valid records by records, total pounds and per day
    This function does not validate records"""
    # add a one-sentence docstring naming its one job
    # Rubric exceed step : plus one docstring states what its function is not responsible for, like validating records.
    by_day = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(',')
        day = parts[4]
        pounds = float(parts[3])
        if day not in by_day:
            by_day[day] = {"donations": 0, "pounds": 0.0}
        by_day[day]["donations"] += 1
        by_day[day]["pounds"] += pounds
        total_pounds += pounds
    return {"records" : len(valid_records),
            "total_pounds" : total_pounds,
            "by_day" : by_day
        }
    
    #return the same dict shape, with "by_day" keyed by parts[4]
def summarize_pounds_per_items(valid_records):
    '''This function counts how many pounds each item holds
    This function does not validate records'''
    lb_per_item = {}
    total_pounds = 0.0
    for record in valid_records:
        parts = record.split(',')
        items = parts[1]
        pounds = float(parts[3])
        if items not in lb_per_item:
            lb_per_item[items] = {"items" : 0, "pounds": 0.0}
        lb_per_item[items]["items"] += 1
        lb_per_item[items]["pounds"] += pounds
        total_pounds += pounds
    return {"records" : len(valid_records),
                "total_pounds" : total_pounds,
                "lb_per_item" : lb_per_item
            }
# Rubric extra step : writes a third summarizer, like pounds per item, and swaps it in with no other edits.

run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
# call run_pipeline(DATA_FILE, "donation_summary.json", summarize_by_day)
with open("donation_summary.json", "r") as f:
    reloaded = json.load(f)
    # replace None with json.load() of "donation_summary.json"

print("records:", reloaded["records"], "| total pounds:",
      reloaded["total_pounds"])
for day, stats in sorted(reloaded["by_day"].items()):
    print(day, stats["donations"], "donations,", stats["pounds"], "lbs")

run_pipeline(DATA_FILE, "lbperitem_summary.json", summarize_pounds_per_items)
with open("lbperitem_summary.json", 'r') as f:
    reloaded_two = json.load(f)

print("records:", reloaded_two["records"], "| total pounds:",
      reloaded_two["total_pounds"])
for item, stats in sorted(reloaded_two["lb_per_item"].items()):
    print(item, stats["items"], "donations,", stats["pounds"], "lbs")

# Step 4, answer 1: How many of your other functions did you edit for the swap? If any, what was the summarizer reaching into?
# 0. I didn't change any function for the swap. In the print, I had to call my reloaded_two 
# and my new variable I set (lb_per_item). The summarize acts as a parameter.
# Step 4, answer 2: Three dates show only 1 donation. Why, and what should the coordinator see?
# 3 dates show 1 donation while the rest show 2 because it did not pass the validate donation function in step 1.
# we can see that those 3 dates that only show one, have value errors which (as stated in step 1):
# wrong field count, missing category, and pounds is not a number.
# The coordinator should see the errors so they can quickly correct them before relying on a summarizer.
