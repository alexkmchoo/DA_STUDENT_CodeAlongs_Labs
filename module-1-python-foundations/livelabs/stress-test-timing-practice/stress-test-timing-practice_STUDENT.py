#!/usr/bin/env python3
"""Lab: Stress-Test Your Code: Timing & Efficiency
GitBook Quest 1.9: Lookups Matter

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 stress-test-timing-practice_STUDENT.py
    Or make it executable once:
        chmod +x stress-test-timing-practice_STUDENT.py
    and from then on run it directly:
        ./stress-test-timing-practice_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (LiveLabOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

SUBMIT
    Commit this file (you may rename it stress-test-timing-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Generate Batches of Your Class at Three Sizes (10, 1,000, and 100,000) =====
# Any class works: your own from Day 15's lab, a new one, or the sample
# LibraryTool on today's slides.

import random  # Python's built-in module for random values

# TODO: paste your class here (or the sample LibraryTool from the slides)
class LibraryTool:
    def __init__(self, tool_name, quantity_available, requires_inspection):
        self.tool_name = tool_name
        self.quantity_available = quantity_available
        self.requires_inspection = requires_inspection

    def is_available(self):
        return self.quantity_available > 0

def make_batch(size):
    # make an empty list called batch
    batch = []
    for i in range(size):
        # loop `size` times with: for i in range(size):
        batch.append(LibraryTool(f"Tool{i}",random.randint(0, 5), random.choice([True, False])))
        # inside the loop, create one object and append it to batch
        # give each object a unique name, e.g. f"Tool{i}"
        # use random.randint(0, 5) for any number attribute
    return batch
    # after the loop, return batch

small_batch = make_batch(10)
medium_batch = make_batch(1000)
large_batch = make_batch(100000)

print(len(small_batch), len(medium_batch), len(large_batch))
# TODO: small_batch = make_batch(10)
# TODO: make medium_batch (1,000) and large_batch (100,000) the same way
# TODO: print len() of all three batches to check their sizes

# ===== Step 2: Write Two Searches Over That Batch - a Linear Scan and a Dict Lookup - and Confirm They Agree =====
# Same two functions Day 16's lecture wrote over SupplyItem - now over your
# own class and a much bigger batch.

def find_by_name_linear(batch, name):
    for x in batch:
        if x.tool_name == name:
            return x
    return None
    # TODO: loop over batch, one object at a time
    # TODO: if the object's name equals name, return the object
    # TODO: after the loop, return None (nothing matched)
    


def build_lookup(batch):
    return {x.tool_name: x for x in batch}
    # TODO: return a dict: {obj.name: obj for obj in batch}
    # TODO: (use your class's real name attribute, e.g. tool_name)

# Step 5 : AI speed up
#def find_by_name_fast(lookup, name):
    #return lookup.get(name)
    

lookup = build_lookup(large_batch)
# TODO: lookup = build_lookup(large_batch)
#name = "Tool99999"
print(find_by_name_linear(large_batch, "Tool99999").tool_name)
print(lookup.get("Tool99999").tool_name)
# TODO: pick a name you know is in large_batch, like "Tool99999"
# TODO: print what find_by_name_linear returns for that name
# TODO: print what lookup.get() returns for the same name
# TODO: check both printed lines show the same object

# ===== Step 3: Put a Stopwatch on Both Searches at All Three Sizes and Record the Numbers =====
# Predict the pattern before running: which column should grow as size
# grows, and which should stay roughly flat?

import time  # Python's built-in module; time.perf_counter() is new
import numpy as np

# TODO: predict first: which time grows with size? Write it here:
# Prediction:
pairs = [(len(small_batch), small_batch),
         (len(medium_batch), medium_batch),
         (len(large_batch), large_batch)
]
# make a list of (size, batch) pairs for your three batches
for size, batch in pairs:
    # loop over that list: for size, batch in pairs:
    # start = time.perf_counter()
    #lookup = build_lookup(batch)
    #build_time = np.round((time.perf_counter() - start), 7)
    # AI Speedup step 5
    lookup = build_lookup(batch)
    # lookup = build_lookup(batch)
    start = time.perf_counter()
    # start = time.perf_counter()
    find_by_name_linear(batch, "NotThere")
    # run find_by_name_linear(batch, "NotThere")
    linear_time = np.round((time.perf_counter() - start),7)
    #  linear_time = time.perf_counter() - start
    
    start = time.perf_counter()
    # same thing, set the start
    # find_by_name_fast(lookup, "NotThere")
    # AI speedup step 5
    lookup.get("NotThere")
    # time lookup.get("NotThere") the same way, as dict_time
    dict_time = np.round((time.perf_counter() - start),7)
    # make somethign called dict_time bc it's in the print 
    print(size, linear_time, dict_time)
    # print(size, linear_time, dict_time)

# TODO: search for "NotThere" on purpose: a missing name is the worst case
# TODO: 1.5e-06 in your output means 0.0000015 seconds

# ===== Step 4: Answer Your Manager's Question in One Sentence, in Big-O Terms =====

# Your answer:
# As the workload increases, its better to use a dict for a direct lookup because it runs faster. 
# If the workload is small like the small or medium batch its better to use a list.
# 

# ===== Step 5: Optional Stretch: Ask an AI How to Speed Up Your Linear Scan, Then Make It Prove It =====
# Stretch work only - beyond the core lab budget. Take it if you finish
# Steps 1-4 early. Same 'verify before trusting' habit from Module 0's
# AI-literacy lesson, now applied to a code-optimization claim instead of a
# chatbot fact claim.

# Your answer:
# AI changed step 2 by adding this into it : def find_by_name_fast(lookup, name): return lookup.get(name)
# It changed step 3 by calling find_by_name_fast as well by doing find_by_name_fast(lookup, "NotThere")
# I tested it and saw that the before and after dict was way slower than the AI generated answer
# Unchanged | 10 : 9.5e-06 | 1000 : 2.3e-05 | 100000 : 0.0027453
# AI | 10 : 5.5e-06 | 1000 : 0.002297 | 100000 : 0.0033397
# We can see that the AI change ran linear ran faster across all tests. As input size got larger, the results came close
# in fact, I also tested this for an input size of 1000000 and the original linear ran faster
# Unchanged | 1000000 0.0294433
# AI | 1000000: 0.0300632
# All in all though, it did work out with our input sizes. My results always showed the linear being faster than the dict search anyways
# but this AI change made the dict even faster
# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Bring your numbers, not a summary of them. Specifically:
# - Your timings at each batch size, for both searches. Everyone tested a
#   different class on a different laptop, so the raw numbers won't match -
#   put yours up anyway.
# - Which column changed as the batch grew, and which one didn't. - The
#   batch size where the difference stopped being something you had to
#   squint at.
# - Whether anything surprised you. A linear scan that looked suspiciously
#   flat is worth raising - say what you found out was going on.
# - If you tried the AI stretch: what it claimed, and whether your own
#   timings actually backed it up. "It was wrong" is a good answer if you
#   can show the number that proves it.
#
# Be ready for "why does that happen?" - the timings are evidence, and the
# explanation is what's being assessed.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
