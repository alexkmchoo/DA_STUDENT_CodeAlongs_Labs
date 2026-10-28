#!/usr/bin/env python3
"""Pick the Right Container: see DataChallengeOverview&Steps.md."""

import json

DATA_FILE = "station_taps.csv"  # edit the filepath with the data

with open(DATA_FILE) as f:
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

# Predicted count for T001: 1, its the first one looking at the dataset
# Predicted count for T040: 41, its the 41st row so it has to check all 41
# Predicted count for T999: 41, it doesn't exist, so it has to check all 41 as well

# Step 1, answer 2: Which of the three counts should you plan around, and why?

# We should plan around the 2nd and 3rd prediction because there are 40 rows of data here.
# We won't always have the luxury of the first one like the first prediction
# We have to plan to look at like row 27, 38, etc.


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
# Big multiplies the taps by 10 so we will have 400 and if we pair this, we have to do 400 by 400 so we get 160000

# Step 2, answer 2: The scan's pattern in one sentence, then the pair loop's, with no notation.
# yo im ngl 


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

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Count Taps Per Card With a Dictionary, and Stations With a Set
# TODO: assign `taps_by_card` to an empty dict (card ID: tap count)
# TODO: assign `lookups` to 0
# TODO: loop over `taps`; add 1 to `lookups`
# TODO: add 1 to row[1]'s count in `taps_by_card`, or set it to 1 if new
# TODO: assign `stations` to set(); loop over `taps` and .add() row[2]
# TODO: assign `repeat_riders` to 0
# TODO: loop over `taps_by_card`; add 1 to `repeat_riders` if a count is > 1

print("distinct cards:", len(taps_by_card))
print("lookups the dictionary needed:", lookups)
print("unique stations:", len(stations), sorted(stations))
print("cards that tapped more than once:", repeat_riders)
print("taps for C001:", taps_by_card["C001"])

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
# Step 4, answer 4:
#


# ===== Day 3 =====

# Step 5: Save the Summary as JSON and Read the TypeError a Set Causes
# TODO: replace each None with your Day 2 value; keep `stations` a set
summary = {
    "service_day": "2026-03-02",
    "total_taps": None,
    "distinct_cards": None,
    "stations": None,
    "taps_by_card": None,
}

print("about to serialize", len(summary), "keys")
# TODO: run the file and answer below before you change anything
# TODO: then put # in front of the next two lines so Step 6 can run
text = json.dumps(summary, indent=2)
print(text)

# Step 5, answer 1:
#
# Step 5, answer 2:
#
# Step 5, answer 3:
#


# Step 6: Write `tap_summary.json`, Reload It, and Check Which Types Survived
# TODO: assign summary["stations"] to a type JSON can hold; keep the key
# TODO: json.dump() `summary` into a with open("tap_summary.json", "w")
# TODO: replace None with json.load() of "tap_summary.json"
reloaded = None

print("total_taps came back as:", reloaded["total_taps"])
print("taps_by_card came back as a", type(reloaded["taps_by_card"]).__name__)
print("C001 straight out of the file:", reloaded["taps_by_card"]["C001"])
print("stations came back as a", type(reloaded["stations"]).__name__)
print("round trip identical:", reloaded["taps_by_card"] == taps_by_card)

# Step 6, answer 1:
#
# Step 6, answer 2:
#
