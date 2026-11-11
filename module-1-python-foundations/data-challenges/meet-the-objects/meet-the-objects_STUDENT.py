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
# Each record is multiple information on one station, containing the name of the station, the id of the station, how many
# bikes are available, the capcity of that station, and whether or not it needs maintenance. Capacity and bikes available
# hold numbers, while needs maintenance, station ID and name of the station hold text.
# Step 1, answer 2: What .pop(2) removes, what it hands back, and what happens to the positions after it.
# .pop removes an index which is (2). That index doesn't get used anymore so the positions after that move over one.
# Step 1, answer 3: Which stations got a bike count that was never theirs? Whose real count does nobody see?
# Only 2 stations get the real bike count which is 0 and 1, while the rest 2-8 don't due to the pop.
# The real count of index 9 never gets seen.


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
# I made a list of index 0,2,4 and 1,7,9 because the station is either empty or the bikes avaiable is close to the capacity (full)
# Vans go to stations that are nearly empty or jammed full
# Step 2, answer 2: Where your two lists differed, what each of you argued, and which list you kept.
# 0,2,4 had more space while 1,7,9 had basically no room. I kept 0 and 4 just because they had similar values (2x bigger)
# Step 2, answer 3: Which field from the file you left out, and why the dispatcher does not need it.
# I actually included every field. But if I were to leave one out station ID because 
# the dispatcher just needs the name of the station. It can identify what to do after
# Step 2, answer 4: Why your two stations prove independence, with their answers before and after.
# We started with no changes with 0 and 4 for quiet and busy, which they both proved to be False. After setting busy.bikes_available 
# to 0, only busy changed.


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
    #copy your Station class from Step 2 here
    def __str__(self):
        return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"
        # add __str__(self) to return text like "Grand Army Plaza: 6 of 48 bikes"
        # build it from self.name, self.bikes_available and self.capacity
fleet = []
for s in stations:
    # assign `fleet` to []; loop over `stations` as `s`
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s['station_id'], s['needs_maintenance']))
    # rebuild `fleet` from this class with the same loop as Step 2
print(fleet[0])
print(fleet[:2])

# Step 3, answer 1: Before you run: the shape you expect from each of the four prints, in order.
# 1. print(fleet[0]) >> Like what we saw in class something like [<main_. words numbers at 01231]
# 2. print(fleet[:2]) >> same as above
# 3. print(fleet[0]) >> one line Grand Army Plaza 6 of 48 bikes
# 4. print(fleet[:2]) >> two lines from 0 and 1 in a list since I made __str__
# Step 3, answer 2: Which prediction was wrong, and which method does a list use instead of __str__?
#  1,2,and 4 were wrong, it used a __repr__ instead


# Step 4: Add `__repr__` and Print the Van List for You and the Dispatcher
class Station:
    def __init__(self,name,capacity,bikes_available,station_id,needs_maintenance):
        self.name = name
        self.capacity = capacity
        self.bikes_available = bikes_available
        self.station_id = station_id
        self.needs_maintenance = needs_maintenance
    def needs_restock(self):
         return self.bikes_available < self.capacity/4
    def __str__(self):
            return f"{self.name}: {self.bikes_available} of {self.capacity} bikes"
# copy your Station class from Step 3 here
    def __repr__(self):
        return f"Station('{self.name}', {self.bikes_available})"
# add __repr__(self) to return text like "Station('Grand Army Plaza', 6)"
fleet = []
for s in stations:
    # assign `fleet` to []; loop over `stations` as `s`
    fleet.append(Station(s["name"], s["capacity"], s["bikes_available"], s['station_id'], s['needs_maintenance']))
# rebuild `fleet` from this class with the same loop as Step 2
van_list = []
for x in fleet:
    # `van_list` to []; loop over `fleet`
    if x.needs_restock():
        van_list.append(x)
# each station whose needs_restock() returns True to `van_list`

print(van_list)
for station in van_list:
    print(station)

# Step 4, answer 1: Before you run: how many stations land in van_list, and which method print(van_list) will use.
# 5 and since we made it an empty list, it will display in a __str__ format.
# Step 4, answer 2: What each display method is for, and who reads it.
# __str__ is for people friendly display. It makes it readable 
# __repr__ is for developers or debuggers. It makes it understandable for someone maybe tasked to fix your code.
# Step 4, answer 3: Which printout you would hand the dispatcher, and why.
#  I would hand the dispatcher step 4 printout with the for loop because it makes it easier for that person to understand.
# Even if the dispatcher was a developer, it would make it easier for them to understand something like Grand Army Plaza: 6 of 48 bikes
# instead of [<__main__.Station object at 0x101162e20>, <__main__.Station object at 0x101162dc0>] so they can
# make a decision right away
