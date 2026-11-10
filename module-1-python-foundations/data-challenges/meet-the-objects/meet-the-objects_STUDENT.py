#!/usr/bin/env python3
"""Meet the Objects: see DataChallengeOverview&Steps.md for the steps."""

import json

DATA_FILE = "/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/bike_stations.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    stations = json.load(f)


# ===== Day 1 =====

# Step 1: Reproduce the Parallel-List Bug and Name the Wrong Stations
names = []
bikes = []
# assign `names` and `bikes` to two empty lists
for x in stations:
    names.append(x['name'])
    # loop over `stations`; append each one's "name" to `names`
    bikes.append(x['bikes_available'])
    # append the same station's "bikes_available" to `bikes`
names.pop(2)
print("stations in the file:", len(stations))
for i in range(len(names)):
    print(f"{names[i]} | {bikes[i]} bikes")
    # #loop over range(len(names)); print names[i], "|", bikes[i], "bikes"

# Step 1, answer 1: Describe the data file in two or three sentences. What is one record? Which fields are numbers, and which are text? What looks wrong?
# 
# Step 1, answer 2: What .pop(2) removes, what it hands back, and what happens to the positions after it.
# 
# Step 1, answer 3: Which stations got a bike count that was never theirs? Whose real count does nobody see?
#


# Step 2: Define the Station Class and Prove Two Instances Are Independent
class Station:
    def __init__(self,name,capacity,bikes_available,station_id,needs_maintenance):
        # add __init__ with name (str), capacity and bikes_available (int)
        # add a parameter and self.<name> for each extra field you agreed
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance
        # in __init__, assign each parameter to self.<same name>
    def needs_restock(self):
        return self.bikes_available < self.capacity/4
    # add needs_restock(self): True if bikes_available < capacity / 4

fleet = []
for s in stations:
    # assign `fleet` to []; loop over `stations` as `s`
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s['station_id'], s['needs_maintenance']))
    # append Station(s["name"], s["capacity"], s["bikes_available"])
busy = fleet[0]
quiet = fleet[4]
# assign `busy`, `quiet` to two stations with equal needs_restock()
print(busy.needs_restock())
print(quiet.needs_restock())
# print both needs_restock() answers
busy.bikes_available = 0
print(busy.needs_restock())
print(quiet.needs_restock())
# set busy.bikes_available to 0, then print both answers again

# Step 2, answer 1: Your own list, made before you compared. Put the dispatcher's words beside each attribute.
#
# Step 2, answer 2: Where your two lists differed, what each of you argued, and which list you kept.
#
# Step 2, answer 3: Which field from the file you left out, and why the dispatcher does not need it.
#
# Step 2, answer 4: Why your two stations prove independence, with their answers before and after.
#


# ===== Day 2 =====

# Step 3: Add `__str__` and Find Out Which of Four Prints It Changes
print(fleet[0])
print(fleet[:2])

class Station:
    def __init__(self,name,capacity,bikes_available,station_id,needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
        return self.bikes_available < self.capacity/4
# TODO: copy your Station class from Step 2 here
# TODO: add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity}"
# TODO: build it from self.name, self.bikes_available and self.capacity
fleet = []
for s in stations:
    # assign `fleet` to []; loop over `stations` as `s`
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s['station_id'], s['needs_maintenance']))
# TODO: rebuild `fleet` from this class with the same loop as Step 2

print(fleet[0])
print(fleet[:2])

# Step 3, answer 1:
#
# Step 3, answer 2:
#


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
# TODO: copy your Station class from Step 3 here
# TODO: add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
# TODO: rebuild `fleet` from this class with the same loop as Step 2
# TODO: assign `van_list` to []; loop over `fleet`
# TODO: append each station whose needs_restock() returns True to `van_list`

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1:
#
# Step 4, answer 2:
#
# Step 4, answer 3:
#
