#!/usr/bin/env python3
"""Day 2 code-along: Nested Loops & Conditionals. Run: python3 <file>"""

# ===== 1. Nested Loop, Live =====
# Print all six row and column pairs, starting at 0 0 and ending at 1 2.
# DISCUSS: If both loops used range(2), order: A: 1 0. B: 0 0. C: 1 1. D: 0 1.
# Your answer:
#
print('----- 1. Nested Loop, Live -----')
<<<<<<< HEAD

for row in range(2):
    for col in range(3):
        print(row,col)
=======
# TODO: write a nested loop that prints every (row, col) pair
# TODO: row goes through range(2), col through range(3)
>>>>>>> upstream/main

# PREDICT before you run: Outer range(3), inner range(2): how many lines print?
# Your answer:
<<<<<<< HEAD
# The same amount of lines print : 2 * 3 is 6. 6 lines print on both codes.
#
#
# DISCUSS: With range(3) outside and range(2) inside, a classmate's version
#          prints only 3 lines instead of 6. What's the most likely cause?
# Your answer:
# The print function is probbaly outside the nested loop, only printing the range(3)
=======
#
# DISCUSS: A classmate gets 3 lines instead of 6. What's the likely cause?
# Your answer:
>>>>>>> upstream/main
#


# ===== 2. Nested Conditional, Live =====
# Check the operation type first, then if the quantity is positive.
print('----- 2. Nested Conditional, Live -----')
# TODO: check operation first
# TODO: if it's "ADD", nest a second check that quantity is above 0
operation = "ADD"
quantity = -5

<<<<<<< HEAD
if operation == "ADD":
    if quantity > 0:
        print(f"yay! It's a valid add! {quantity} is greater than 0")
    else:
        print(f'No! Invalid add! {quantity} is not greater than 0')
else:
    print("Sorry, I can't read that input!")
# DISCUSS: Suppose the inner quantity check in the Nested Conditional code
#          never seems to run. What should you trace first? Try it: set
#          operation to "SEARCH" and run.
# Your answer:
# if you set operation to search, it will print my print "Sorry I can't read that input"
=======
# DISCUSS: If the inner quantity check never runs, what do you trace first?
# Your answer:
>>>>>>> upstream/main
#


# ===== 3. Putting It Together: Loop + Nested Conditional =====
# Check each line: print whether it is valid, a bad quantity, or a remove.
print('----- 3. Putting It Together: Loop + Nested Conditional -----')
<<<<<<< HEAD
# TODO: loop over transactions; for each line, split it into
# operation and amount, then nest the ADD/quantity check
# from the nested-conditional step inside the loop


=======
# TODO: loop over transactions; split each into operation and amount
# TODO: put the nested ADD/quantity check inside the loop
>>>>>>> upstream/main
transactions = ["ADD 10", "REMOVE 3", "ADD -5"]
for x in transactions:
    operation,amount = x.split()
    amount = int(amount)
    if operation == "ADD":
        if amount > 0:
            print(f"Amount added: {amount}")
        else:
            print(f'No, sorry amount must be a positive number, I got {amount}, which is not greater than 0')
    elif operation == "REMOVE":
        print(f"Ok removed {amount}!")
    else:
        print(f'No, sorry amount must be a positive number, I got {amount}, which is not greater than 0')

# PREDICT before you run: Which check flags "ADD -5" as invalid?
# Your answer:
<<<<<<< HEAD
# the amount > 0
=======
>>>>>>> upstream/main
#
