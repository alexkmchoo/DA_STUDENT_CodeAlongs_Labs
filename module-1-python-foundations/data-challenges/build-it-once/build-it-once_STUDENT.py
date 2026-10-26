#!/usr/bin/env python3
"""Data Challenge: Build It Once, Use It Again
GitBook Quest 1.2: Build It Once, Use It Again

HOW TO RUN
    Open a terminal in the folder that holds data/ and run:
        python3 build-it-once_STUDENT.py
    If this file sits one folder below data/, run it from the folder
    above instead:  python3 build-it-once/build-it-once_STUDENT.py
    Or make it executable once:
        chmod +x build-it-once_STUDENT.py
    and from then on run it directly:
        ./build-it-once_STUDENT.py
    The first line, #!/usr/bin/env python3 (the "shebang"), is what
    makes ./ work. python3 <file> ignores it as a comment.

THE DATA      data/rec_center_signups.txt

ANSWER EVERYTHING IN THIS FILE
    - Code goes under each step's banner.
    - Written answers go in # comments under each "# Your answer:"
      line.
    - Run the file after every change. It runs top to bottom, so a
      later step can use anything an earlier step made.

HINTS live in the worksheet (DataChallengeOverview&Steps.md), collapsed
under each step. Open one only when you are stuck.

AI TOOLKIT: prompts to try and how to check them are in
DataChallengeOverview&Steps.md.

SUBMIT
    Commit this file (you may rename it build-it-once.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
    Submit once, at the end of Day 3. Keep every day's work in here.
"""

############################################################################
#  THE DATA: open data/rec_center_signups.txt and look at it
#  before you write any code. The worksheet's "The Data" section
#  shows how to load it.
############################################################################

# 1. What does one row represent?
# Your answer:
# the data of each member, the class they're taking, and number of sessions
#

# 2. Which fields hold numbers, and which hold text?
# Your answer:
# The member field and the class_name field holds text and the sessions field comes number
#

# 3. What already looks wrong, missing or inconsistent?
# Your answer:
# Nothing looks wrong, the person that made the dataset could have put the column names in another line, but other than that its fine
#

############################################################################
#  DAY 1
############################################################################

# ===== Step 1: Write total_sessions(), Then Call It on Every Class and on Swim Only =====
# One function that adds up a sessions column, called twice: once on every
# record, once on just the Swim records.
#
# 1. Predict two numbers by hand off the file. Total sessions across every
#    class: add the third field down all 13 records. Total sessions for Swim
#    only: add that same field, but only on the records whose class is Swim.
#    Write both in a comment before you run anything.
# 2. Write total_sessions(records) so it adds up the sessions column across
#    every record in records and hands the total back with return, not
#    print.
# 3. Build swim_only: the records whose class is Swim, and nothing else.
# 4. Run it, and check both printed numbers against your two predictions.
#
# The arithmetic is the same arithmetic a plain loop would do. What changes
# is that the answer comes back to you instead of going to the screen.

with open("data/rec_center_signups.txt") as f:
    signups = [line for line in f.read().splitlines()
               if line and not line.startswith("#")]

def total_sessions(records):
    total = 0
    for record in records:
        member, class_name, sessions = record.split(",")
        total += int(sessions)
    return total

swim_only = []
for record in signups:
    member, class_name, sessions = record.split(",")
    if class_name == "Swim":
        swim_only.append(record)
        
print("every class:", total_sessions(signups))
print("swim only:  ", total_sessions(swim_only))

# Side note :
'''
swim_only = []
total = 0
for record in signups:
    member, class_name, sessions = record.split(",")
    if class_name == "Swim":
        total += int(sessions)
print("swim only:  ", total)
'''
# this code also worked, I had originally put this as a my code because I did not want to use AI. 
# my thought process is if the total sessions worked, then it should work for swim only as well
# It wouldn't print with print("swim only:  ", total_sessions(swim_only)) so I asked AI what was wrong
# and to explain to me where I went wrong, apparently I did not get it wrong, but there was just one of two 
# ways to write this code, the .append one I got from AI, but the print total code I had done myself
# Tina told me to also include my own code here and add a side note saying why this worked and what AI showed me



# ===== Step 2: Count Long Bookings at Two Different Cutoffs With One Function =====
# The board changed the long-booking cutoff from 4 sessions to 2. Answering
# both should cost you one extra argument, not a second function.
#
# 1. Predict both returned: counts in a comment, reading the third field
#    down the file: once for 4 or more, once for 2 or more.
# 2. Write count_long_bookings(records, minimum) so it counts the records
#    whose sessions number is minimum or more, and returns that count.
# 3. Write show_long_bookings(records, minimum) so it prints a sentence with
#    the same count in it. Only print. Do not add a return.
# 4. Run the whole file, including the lines at the bottom that were written
#    for you.
# 5. Write down what handed_back holds, and why. It is on the last printed
#    line.
# 6. Name the parameter and the arguments, pointing at the lines: which name
#    is minimum, and which values are the 4 and the 2.
#
# One of the two functions you just wrote gives you something back. The
# other only puts something on the screen.

def count_long_bookings(records, minimum):
    count = 0
    for record in records:
        member, class_name, sessions = record.split(',')
        if int(sessions) >= minimum:
            count += 1
    return count 

def show_long_bookings(records, minimum):
    x = count_long_bookings(records, minimum)
    print(f'{x} bookings have {minimum} or more sessions')

print("returned:", count_long_bookings(signups, 4))
print("returned:", count_long_bookings(signups, 2))

handed_back = show_long_bookings(signups, 4)
print("what show_long_bookings handed back:", handed_back)

# Your answer:
# every class: 45
# swim only:   15
# returned: 7
# returned: 11
# 7 sessions has 4 or more sessions
#

# ----- Share Out: Day 1 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your two totals. Whole file, and Swim only. If your numbers differ from
#   another group's, say so. You read the same file, so one of you has a bug
#   worth finding.
# - Your function next to the loop it replaced. Name the specific thing that
#   got easier. Not "cleaner."
# - What show_long_bookings handed back, and why. Say what that tells you
#   about return versus print.
# - Which name is the parameter and which value is the argument, pointing at
#   your own two lines.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#

############################################################################
#  DAY 2
############################################################################

# ===== Step 3: Count the Same Bookings Without a Cutoff Parameter, and Compare =====
# Two functions that answer the same question. The one you wrote on Day 1
# takes the cutoff as a parameter. This one takes no cutoff at all.
#
# 1. Predict both printed counts with no new arithmetic. You already
#    produced the count at a cutoff of 4 and the count at a cutoff of 2 in
#    Day 1's second step. All you are predicting here is which of those two
#    numbers each of the two identical-looking calls prints. Write both in a
#    comment, and write why.
# 2. Write count_reaching_outside(records) so it counts the same thing
#    count_long_bookings does, but takes no minimum parameter. It reads
#    sessions_cutoff from outside the function instead.
# 3. Call it once at a cutoff of 4, printing the result.
# 4. Call it again, unchanged, after sessions_cutoff becomes 2, and print
#    that result too. The call line is identical both times.
# 5. Print count_long_bookings(signups, 4) underneath for comparison.
#
# Both versions run clean. Decide which of the two you would trust in a file
# you did not write, and say what in the call line told you.

sessions_cutoff = 4

def count_reaching_outside(records):
    count = 0
    for record in records:
        member, class_name, sessions = record.split(',')
        if int(sessions) >= sessions_cutoff:
            count += 1
    return count
print("cutoff", sessions_cutoff, "gives", count_reaching_outside(signups))

# counts the same thing as count_long_bookings, but takes no minimum
# so this means the function is the same, we are finding what to replace "minimum" with
# which they gave us the variable of sessions_cutoff

sessions_cutoff = 2
print(count_reaching_outside(signups))
# call count_reaching_outside(signups) again, unchanged, and print it
print(count_long_bookings(signups, 4))
# print count_long_bookings(signups, 4) underneath for comparison


# ===== Step 4: Pass the Last Member In and Out, Then Trigger an UnboundLocalError =====
# The coordinator wants each sign-up printed next to the one before it. The
# top half is yours to write. The bottom half is written for you, and is
# supposed to raise.
#
# 1. Write log_signup(record, previous_member) so it pulls the member name
#    out of record, prints the previous member and this one on one line, and
#    returns this member's name.
# 2. Call it on signups[0], then on signups[1], storing what it returns back
#    into last_member each time. Predict both printed lines in a comment
#    first, reading the names off the top of the file.
# 3. Leave log_signup_broken exactly as written. It tries the same job by
#    reading and then updating last_seen, a name defined above the function.
# 4. Predict in a comment whether its print line will work. The step above
#    showed a function reading an outside name just fine.
# 5. Run the file, read the traceback, and write down the exception name,
#    the variable and the line it points at, in your own words, before you
#    look anything up.
#
# global is not the fix. The working half of this same step already shows
# what is: pass the value in, return it back out.
#
# This step is supposed to raise UnboundLocalError. Run it, read the
# traceback, answer below, then put a # in front of the line that raises so
# the steps after it can run.

def log_signup(record, previous_member):
        member, class_name, sessions = record.split(',')
        #pull the member name out of `record` = seperated with split
        print(f'Previous member: {previous_member} | This one: {member}')
        # print the previous member and this one on one line = printed it
        return member
        # return this member's name
    

last_member = "nobody yet"
last_member = log_signup(signups[0], last_member)
last_member = log_signup(signups[1], last_member)

# TODO: call log_signup on signups[0], then on signups[1], storing = called log_signup , argument = signups[0]
# comma last_member, returns it back into last_member each time

last_seen = "nobody yet"

def log_signup_broken(record):
    # Leave this body exactly as written. It is supposed to raise.
    print("previous:", last_seen)
    last_seen = record.split(",")[0]
    return last_seen

log_signup_broken(signups[2])

# Your answer:
# you get an error :UnboundLocalError: local variable 'last_seen' referenced before assignment
# last_seen was defined already outside the function = "nobody yet", but we assigned it another one 
# inside the function = record.split(",")[0]
# This means that it is treated like a local variable, if it was a global variable, it could be called on.
# 

# ----- Share Out: Day 2 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Which of the two functions you would trust in a file you did not write,
#   and what in the call line decided it.
# - The exception name and the variable it named, plus your own one-sentence
#   account of the rule. Written before you looked anything up.
# - Why the print line failed when it only reads last_seen, and what
#   deleting the line below it changed.
# - Anything AI told you about global. Say whether it offered it as the fix,
#   and what you did instead.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#

############################################################################
#  DAY 3
############################################################################

# ===== Step 5: Build Per-Member Totals Out of Three Functions, Not One =====
# The coordinator wants per-member totals. Write this as three functions,
# not one.
#
# 1. Write sessions_in(record) so it pulls the sessions number out of a
#    single record and returns it.
# 2. Write signups_for(records, member) so it returns just the records
#    belonging to one member.
# 3. Write total_for(records, member) so it returns that member's total
#    sessions, doing almost nothing itself. It gets its work done by calling
#    the other two.
# 4. Predict Gwen's total in a comment, adding up Gwen's rows in the file by
#    hand.
# 5. Print one line per member for Nia, Omar, Tess, Rafi and Gwen, and check
#    Gwen's line against your comment.
#
# Before you run it, show your partner the line where each of the three
# functions gets called.

# Three function names. Everything else is yours.

def sessions_in(record):
        member, class_name, sessions = record.split(",")
        return int(sessions)
# write sessions_in(record) = def sessions_in(record). pull sessions number = split.
# return it = return int(sessions)

def signups_for(records, member):
    category = []
    for record in records:
        member_name, class_name, sessions = record.split(",")
        if member_name == member:
            category.append(record)
    return category
        # created a new variable for an empty list, like the swim_only question, append brings them into the list 
    

def total_for(records, member):
    x = signups_for(records, member)
    # created a variable for the function I made above, that calls the other two
    return total_sessions(x)
    # returned a previous variable from another function and placed my argument as the new variable I created


    # This one should get its work done by calling the other two.
    pass

list = []
# makes an empty list that we are going to put information into
for record in signups:
    member_name, class_name, sessions = record.split(",")
    if member_name not in list:
        list.append(member_name)
            #append will push it into the new list, since it's empty
            # This is similar to the swim_only line of code
# 

for member in list:
    print(f'{member} total sessions: {total_for(signups, member)}')
# TODO: print a line per member

# ===== Step 6: Run total_for() on Five Inputs Nobody Asked For, Then Judge Each Answer =====
# No new functions. Call the ones you already have on inputs nobody asked
# for, and write a verdict beside each printed result.
#
# 1. total_for on an empty list. Print the result.
# 2. total_for on a list holding exactly one record.
# 3. total_for with a member name that is not in the file at all, such as
#    "Marco".
# 4. total_for with a name differing from a real member's only by
#    capitalization, such as "nia" for Nia.
# 5. signups_for on the empty list.
# 6. Add up the per-member totals for all five members, and print that sum
#    beside total_sessions(signups). The two should agree.
# 7. Write a verdict beside each of the five results in a comment: right, or
#    just a number that did not crash? Argue each one with your partner
#    first.
#
# Every line runs clean. Two of them deserve a different answer than they
# get.

# No new functions. Call the ones you already have, on inputs nobody
# asked for, and write a verdict beside each printed result.

print(total_for([], "Omar"))
# empty list
print(total_for(["Nia,Spin,6"], "Nia"))
# list holding exactly one record
print(total_for(signups, "Marco"))
# member name not in file at all, marco
print(total_for(signups, "nia"))
# capitalization comparison
print(signups_for([], "Omar"))
# signups for on an empty list
per_member_total = 0
for member in list:
   per_member_total += total_for(signups, member)
print(f'per-member totals: {per_member_total} | lined up with total sessions : {total_sessions(signups)}')
# shows the per member total and the total sessions we did in the first part


# ----- Share Out: Day 3 -----
# Last 15 minutes, back together as a class. Bring:
#
# - Your verdict on one edge case. Pick the strangest result. Say whether
#   the answer is right or just quiet, and what you would change if this
#   were the center's real data. If you and your partner disagreed, bring
#   both positions.
# - Your cross-check. Did the five per-member totals add up to the
#   whole-file total? Say how you would run that check on a 430-row file you
#   cannot eyeball.
# - Three functions or one? Say which you wrote and what it cost or saved
#   you.
# - One question you could not settle, or one thing you would do differently
#   starting over. Half-finished thinking is what this slot is for.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
# The prompt for AI, if used, was always :
# Don't write the code for me unless I say so, instead be a teacher and I am the student here is the code I have so far
# For step 6, I really struggled with the second prompt "total_for on a list holding exactly one record"
# I had to ask AI to fill in the gap for me because I tried to put signups, member, class_name, sessions
# where the ["Nia,Spin,6"] is in print(total_for(["Nia,Spin,6"], "Nia")) 
# I even tried splitting it again into column names and printing something there, but I couldn't do it
# while still using total_for like the prompt was asking for
# AI gave me this answer, but I made sure I understood exactly what it was telling me