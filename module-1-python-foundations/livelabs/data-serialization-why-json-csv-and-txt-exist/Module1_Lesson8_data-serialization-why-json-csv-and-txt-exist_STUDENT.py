#!/usr/bin/env python3
"""Day 8 code-along: Data Serialization. Run: python3 <file> or ./<file>"""

# ===== 1. Writing to a File =====
# Write two restock reminders to a file called notes.txt, one per line.
print('----- 1. Writing to a File -----')
with open ("notes.txt", "w") as f:
    # use a `with` block and open("notes.txt", "w")
    f.write("Restock staplers\n")
    f.write("Restock printer paper\n")
# TODO: write "Restock staplers" and "Restock printer paper"
# TODO: end each line with "\n"


# ===== 2. Reading It Back =====
# Open notes.txt again and print everything inside it.
print('----- 2. Reading It Back -----')
with open("notes.txt", "r") as f:
    # use a `with` block and open("notes.txt")
    print(f.read())
# TODO: print its full contents with f.read()

# PREDICT before you run: Rewrite notes.txt in "w" mode. Do old lines survive?
# Your answer:
# yeah every line survives cause its writing it (replacing) the file


# ===== 3. A CSV File Is Just Plain Text =====
# This code saves three supply rows as a CSV, then prints the file as text.
# TODO: run this and read the output
print('----- 3. A CSV File Is Just Plain Text -----')
csv_content = "name,count,department\nStapler,12,Office\nPaper,200,Office\n"

with open("supply.csv", "w") as f:
    f.write(csv_content)

with open("supply.csv") as f:
    print(f.read())


# ===== 4. Serializing a Record With json.dump() =====
# Save one supply record, stored as a dict, to a file called supply.json.
print('----- 4. Serializing a Record With json.dump() -----')
import json
# import json
supply = {"Name": "Stapler", "Count": 12, "Department": "Office"}
with open ("supply.json", "w") as f:
    # create a dict called supply: name, count and department
    # use "Stapler", 12 and "Office"
    json.dump(supply, f)
    # open "supply.json" in write mode; save the dict with json.dump()


# ===== 5. Deserializing It Back With json.load() =====
# Load supply.json back into Python and check that it is a real dict again.
print('----- 5. Deserializing It Back With json.load() -----')
import json
# import json
with open ("supply.json", "r") as f:
    supply = json.load(f)
# TODO: open "supply.json"; read it into supply with json.load()
print(supply["Name"])
print(type(supply))
# TODO: print supply["name"], then print type(supply)

# PREDICT before you run: Dump a tuple to JSON and load it back. What type?
# Your answer:
# We answered this in class, it will become a list
