#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "data-challenges/data/station_taps.csv"  # edit the filepath with the data

with open("/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/station_taps.csv") as f:
    rows = [line.split(",") for line in f.read().splitlines() if line]

header = rows[0]
taps = rows[1:]


# ===== Day 1 =====

# Step 1: Write `scan_for()` and Count Its Comparisons for Three Tap IDs
def scan_for(tap_id, records):
    comparisons = 0
    # assign `comparisons` to 0
    for row in records:
        comparisons += 1
        #loop over `records`; add 1 to `comparisons` for every row
        if row[0] == tap_id:
            return comparisons
            #inside the loop, return `comparisons` when row[0] == tap_id
    return comparisons
    # after the loop, return `comparisons`


print("columns:", header)
print("rows in the log:", len(taps))
print("comparisons to find T001:", scan_for("T001", taps))
print("comparisons to find T040:", scan_for("T040", taps))
print("comparisons to find T999:", scan_for("T999", taps))

# Step 1, answer 1: Before you run: your predicted counts for T001, T040 and T999, and how you got each.
# Predicted each count simply by looking at the dataset
# Predicted count for T001: 1, its the first one looking at the dataset
# Predicted count for T040: 40, its the 40th row so it has to check all 40 
# Predicted count for T999: 40, it doesn't exist, so it has to check all 40 rows as well

# Step 1, answer 2: Which of the three counts should you plan around, and why?

# We should plan around the 2nd and 3rd prediction because there are 40 rows of data here, which is the worst case
# We won't always have the luxury of the first one like the first prediction
# A search for something like T040 or T999 always counts the maximum


# Step 2: Print Scan Cost at 5 to 40 Rows, Then Count a Nested Pair Loop
for size in [5, 10, 20, 40]:
    worst = scan_for("T999", taps[:size])
    print("rows:", size ,"| worst-case comparisons:", worst)
    # print "rows:", `size`, "| worst-case comparisons:", `worst`
pairs = 0
# assign `pairs` to 0
for x in taps:
    for tap in taps:
    # assign `pairs` to 0; loop over `taps` with a loop over `taps` inside
        pairs += 1
        # add 1 to `pairs` in the inner loop
print(len(taps), pairs)
# print len(taps) and `pairs`
big = len(taps) * 10
# assign `big` to len(taps) * 10
print(f'worst case: {big}, pair loops count on big rows: {big ** 2}')
# print the scan's worst case and the pair loop's count on `big` rows

# Step 2, answer 1: Before you run: every count you expect, with the arithmetic beside it.
# Id expect 5 counts, 10, counts, 20 counts, and then 40 counts. If we scan for t999, we have to do 40 counts as well
# because it doesn't exist so it has to loop through every single thing. The pairs loop is also 40 , so 40 by 40 is 1600
# Big multiplies the taps by 10 so we will have 400 and if we pair this with what is in the loop, 
# we have to do 400 by 400 so we get 160000

# Step 2, answer 2: The scan's pattern in one sentence, then the pair loop's, with no notation.
# The row went up 10 times in big = len(taps) * 10, which means the work also goes up 10 times. The pair loops goes up 10 times as well because the number of pairs goes up with the rows

# ===== Day 2 =====

# Step 3: Count Taps Per Card With Two Parallel Lists, and Their Comparisons

card_ids = []
# assign `card_ids` to an empty list (each card, first-seen order)
tap_counts = []
# assign `tap_counts` to an empty list (the count for card_ids[i])
comparisons = 0
# assign `comparisons` to 0
for row in taps:
    card = row[1] 
    found = False
    # loop over `taps`; assign `card` to row[1] and `found` to False
    for i in range(len(card_ids)):
        comparisons += 1
        # inside it, loop over range(len(card_ids)); add 1 to `comparisons`
        if card_ids[i] == card:
            tap_counts[i] += 1
            found = True
            break
            # if card_ids[i] == card, add 1 to tap_counts[i], set found, break
    if not found:
        card_ids.append(card) 
        tap_counts.append(1)
        # after the inner loop, if not found, append `card` and 1 to the lists


busiest = tap_counts.index(max(tap_counts))
print("distinct cards:", len(card_ids))
print("comparisons the two parallel lists needed:", comparisons)
print("busiest card:", card_ids[busiest], "with", max(tap_counts), "taps")

# Step 3, answer 1: Before you run: how many comparisons do you expect?
# The highest card_id is C012 in the dataset, so I expect the 40 rows that we have to be multiplied by 12
# So the number of comparisons I'd expect has to be 480, but there are repeats/cards that dont scan so maybe
# about just half or less than half 150-240
# Step 3, answer 2: After: the real count, and why it is bigger than the number of rows.
# The real count was 190. The number of rows is 40. Each tap is up to 12 times because there are 12 cards, which then
# we multiply by 40 rows, but it isn't 480 because, like mentioned it taps up to 12 times and not 12 times exactly

# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
taps_by_card = {}
# assign `taps_by_card` to an empty dict (card ID: tap count)
lookups = 0
# assign `lookups` to 0
for row in taps:
    lookups += 1
# loop over `taps`; add 1 to `lookups`
    if row[1] in taps_by_card:
        taps_by_card[row[1]] += 1
    else:
        taps_by_card[row[1]] = 1
# TODO: add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
stations = set()
for row in taps:
    stations.add(row[2])
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
repeat_riders = 0
# TODO: assign `repeat_riders` to 0
for row in taps_by_card.values():
    if row > 1:
        repeat_riders += 1
# TODO: loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1: Before you run: your lookups prediction and the rule behind it.
# 40, a dict has to look up once per tap. There are 40 rows.
# Step 4, answer 2: Finish "As the Input Size grows..." for the parallel lists, then for the dictionary.
# As the Input Size grows, the parralel list grows with with the number of rows times the distinct cards. The dictionary grows with the number of rows because it's once per lookup.
# Step 4, answer 3: For each container, name its job and how it finds what it needs. What would a list have cost you for stations?
# Parralel list : pairing a card with its count. Goes through the list until it matches
# Set : shows how many stations there are, no duplicates are allowed in sets.
# Dict : pairs each card with their count. Finds it by key indentification.
# A list would have costed more time because it would have to check if the station is already in the list, whereas sets automatically cannot contain duplicates.
# Step 4, answer 4: Which card explains the gap between distinct cards and repeat riders?
# C012 is the one card that tapped only once.


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes

import json
summary = {
    "service_day": "2026-03-02",
    "total_taps": len(taps),
    "distinct_cards": len(taps_by_card),
    "stations": stations,
    "taps_by_card": taps_by_card,
}
print("about to serialize", len(summary), "keys")
# replace each None with your Day 2 value; keep `stations` a set
#with open ("summary.json", "w") as f:
    #json.dump(summary, f)



# run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
# text = json.dumps(summary, indent=2)
# print(text)

# Step 5, answer 1: The last line of the error, exactly as printed.
# TypeError: Object of type set is not JSON serializable
# Step 5, answer 2: Which key caused it, and why, in your own words.
# The set (stations) caused it, JSON can't write sets. 
# Step 5, answer 3: Did about to serialize print before the error? What does that tell you?
# Yeah it printed before the error so that tells me the dict was fine, but the error occured
# because JSON had trouble writing the set, json.dump can't dump the set.


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived

summary["stations"] = sorted(stations)
# assign summary["stations"] to a type JSON can hold; keep the key
with open ("tap_summary.json", "w") as f:
    json.dump(summary, f)
# json.dump() `summary` into a with open("tap_summary.json", "w")
with open("tap_summary.json", "r") as f:
    reloaded = json.load(f)
# replace None with json.load() of "tap_summary.json"

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1: Can the overnight job get one card's count from this file without the raw log? How do you know?
# Yes, because we already calculated how many total taps one card has (like c001)
# this new code only stores the results from the summary and not the taps we used in day 1
# Step 6, answer 2: Which container survived the round trip, and which came back as something else?
# Taps_by_card survived the round trip
# Stations came back as a list because JSON can't write a set, so it had to change into a list.
