#!/usr/bin/env python3
"""Lookups Matter: see DataChallengeOverview&Steps.md for the steps."""

import csv

DATA_FILE = "/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/member_directory.csv"  # edit the filepath with the data
CHECKINS_FILE = "/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/door_checkins.txt"  # edit the filepath with the data

with open(DATA_FILE, newline="") as f:
    members = list(csv.DictReader(f))


# Step 1: Write `find_linear()` to Return the Member and Its Comparisons
def find_linear(members, member_id):
    comparisons = 0
    # assign `comparisons` to 0
    for row in members:
        comparisons += 1
        # loop over `members`; add 1 to `comparisons` for every row
        if row["member_id"] == member_id:
            return row, comparisons
            # inside the loop, return row, comparisons on a member_id match
    return None, comparisons 
    # after the loop, return None, comparisons


row, count = find_linear(members, "M1150")
print("members in the directory:", len(members))
print("found:", row["name"], "at", row["home_branch"])
print("comparisons:", count)

# Step 1, answer 1: Before you run: your predicted count for M1150, and how you got it.
# 150 cause it starts at 001 so 150-001 is 149 but we count the header so 150. I got it by looking at the file.


# Step 2: Total the Comparisons for All 20 Swipes in `door_checkins.txt`
with open (CHECKINS_FILE, 'r') as f:
    swipes = f.read().splitlines()
# open CHECKINS_FILE in a with block as `f`
# inside it, assign `swipes` to f.read().splitlines()
linear_total = 0
not_members = 0
# assign `linear_total` and `not_members` to 0
for member_id in swipes:
    row, comparisons = find_linear(members, member_id)
    # loop over `swipes`; call find_linear(members, member_id)
    # grabbed row, comparisons from Step 1 row, count
    linear_total += comparisons
    # add each count to `linear_total`
    if row is None:
        print(member_id, "NOT A MEMBER", comparisons)
        # print the ID, the name or "NOT A MEMBER", and the comparisons
        not_members +=1
        # add 1 to `not_members` for every swipe with no row
    else:
        print(member_id, row["name"], comparisons)

print("swipes:", len(swipes), "| not members:", not_members)
print("linear total comparisons:", linear_total)

# Step 2, answer 1: Before you run: the cost of each of the first three swipes, their sum, and the cost of a swipe that is not a member.
# 4, 12, and 27. Sum would be 43. The cost is 312 because it would scan each one by one
# Step 2, answer 2: Which swipe cost the most, and why?
# M1313 costs the most bc based on the file, it only goes up to M1312 and that doesn't exist so it has to run through the whole list


# Step 3: Build `members_by_id` and Find the Swipe Where It Pays Off
members_by_id = {}
build_steps = 0
# assign `members_by_id` to an empty dict and `build_steps` to 0
for row in members:
    members_by_id[row["member_id"]] = row
    # loop over `members`; store each row under row["member_id"]
    # had for member in members at first, bottom = member for same variable, but only printed 1 for keys in dict
    # decided to use row in my for and my = since it was provided to us in the TODO
    build_steps += 1
    # add 1 to `build_steps` for every row
def find_dict(members_by_id, member_id):
    # write find_dict(members_by_id, member_id)
    return members_by_id.get(member_id), 1
    # make find_dict() return members_by_id.get(member_id), 1
print("build cost:", build_steps, "| keys in the dict:", len(members_by_id))

linear_running = 0
dict_running = build_steps
# assign `linear_running` to 0 and `dict_running` to build_steps
pays_off_at = None
swipe_number = 0
# assign `pays_off_at` to None and `swipe_number` to 0
for member_id in swipes:
    swipe_number += 1
    # add 1 to `swipe_number`
    _, linear_count = find_linear(members, member_id)
    _, dict_count = find_dict(members_by_id, member_id)
    # no idea what _ means, are we supposed to fill it out?
    # decided not to because in step 4's TODO it asks us to use it again
    linear_running += linear_count
    dict_running += dict_count
    #add each search's count to its running total
    print(swipe_number, member_id,"linear:", linear_running, "dict:", dict_running)
    # print swipe_number, the ID and both running totals
    if pays_off_at is None and dict_running < linear_running:
        # If you don't use pays_off_at is None (since we set it = None in the beginning) here, it just returns the total
        # wasn't too sure on this 
        pays_off_at = swipe_number
        # the first time dict_running < linear_running, set `pays_off_at`

print("dict pays off at swipe:", pays_off_at)
print("morning totals | linear:", linear_running, "| dict:", dict_running)

# Step 3, answer 1: Before you run: at which swipe does the dict total first drop below the linear total?
# 6 M1313 linear: 574 dict: 318// It drops at swipe 6
# Step 3, answer 2: Why a dictionary keyed on member_id fits the door's job. Quote the swipe where it pulled ahead.
# The door job scans (or just asks in verbal terms) the member ID so it directly correlates. "6 M1313 linear: 574 dict: 318"
# Step 3, answer 3: A morning where the plain list would be the better choice.
# Single lookups which will cost more. Small plain lists as well. We see from the output that building a dict costs 312 lookups
# whereas it can cost significantly less


# Step 4: Test an AI Speed Claim Against Your Totals and Write a Verdict
# TODO: replace the text below with your AI's claim, word for word
ai_claim = "For your situation — 20 lookups in a list of 312 rows — a dictionary will generally be significantly faster, especially as the number of lookups increases. Here's the breakdown: - Linear search: Checks items one by one until it finds a match. On average, each lookup checks about 156 rows (assuming matches are distributed throughout the list). - Dictionary lookup: Uses a hash table to find the item directly, typically without scanning the other rows. For 20 lookups: - Linear search: approximately 3,120 row comparisons on average. - Dictionary: approximately 20 lookups, each typically taking constant time. That's roughly 156 times fewer search operations. One important distinction: dictionary construction has an upfront cost. You have to iterate through all 312 rows to build it. My takeaway: If you're only searching once or twice, linear search is perfectly reasonable. If you're doing 20 lookups against the same 312 rows, building a dictionary first is likely the better approach. And the bigger the dataset gets, the more valuable that dictionary becomes."
print("AI CLAIM:", ai_claim)

_, front_count = find_linear(members, swipes[0])
# unpack find_linear() for swipes[0] into `_, front_count`
_, absent_count = find_linear(members, "M1313")
# unpack find_linear() for "M1313" into `_, absent_count`
ratio = round(linear_running / dict_running, 1)
#  assign `ratio` to round(linear_running / dict_running, 1)

print("one front-of-file swipe | linear:", front_count, "| dict: 1")
print("one non-member swipe | linear:", absent_count, "| dict: 1")
print("whole morning | linear:", linear_running, "| dict:", dict_running,
      "| ratio:", ratio)

# TODO: replace the text below with your own verdict
verdict = "Linear search would be O(n) because it looks through the rows one at a time. Dictionary would be O(1) average case because we did 1 per lookup. Linear showed 2924 searches while dict showed 332 in step 3. "
print("VERDICT:", verdict)

# Step 4, answer 1: Hold the AI's claim against your three comparisons. Which one did it match, and which did it miss?
#  AI missed 2924 for linear. It said 3120. It's within range, but is wrong
# it matched 312 rows to build but forgot to add the 20 extra rows to make it 332, so it's actually incorrect
# Step 4, answer 2: Did its number count the cost of building the dictionary? What did it say when you pasted your totals back?
# No the number didn't count the cost of building the dict, only mentioned it 20 and 312.
# The AI said this when I sent my totals back :
# the dictionary became more efficient after the 6th lookup, overcoming its initial construction cost of 312 operations. 
# Across 20 lookups, linear search required 2,924 operations compared to just 332 for the dictionary, 
# making the dictionary approximately 8.8 times more efficient in total operation count.
