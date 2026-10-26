#!/usr/bin/env python3
"""Day 1 code-along: Control Flow & Conditionals. Run: python3 <file>"""

# ===== 1. If/Elif/Else, Live =====
# Print "Too hot", "Too cold", or "Just right" based on temperature.
print('----- 1. If/Elif/Else, Live -----')
# TODO: set temperature to any number
# TODO: write the if/elif/else check yourself
temperature = 71
if temperature > 85:
    print(f"NAHH it's {temperature} degrees. I'm sweating ode")
elif temperature < 50:
    print(f"NAHH it's {temperature} degrees. It's madddd brick")
else:
    print(f"Ouuu it's {temperature} degrees. It's nice out")


# ===== 2. For Loop, Live =====
# Print the four scores, one per line, so the output is 88, 92, 75, then 100.
print('----- 2. For Loop, Live -----')
# TODO: write a for loop that prints every value in scores
scores = [88, 92, 75, 100]
for grade in scores:
    print(grade)

# ===== 3. range() Generates Numbers to Loop Over =====
# Count from 0 to 4 with range(). Notice it stops before 5.
print('----- 3. range() Generates Numbers to Loop Over -----')
# TODO: use range() to print the numbers 0 through 4
<<<<<<< HEAD
for i in range(5):
    print(i)
# PREDICT before you run: Change range(5) to range(3). What does the loop print
#                         now?
# Your answer:
# if you change it to range(3) it will print 0, 1, 2
=======

# PREDICT before you run: Change range(5) to range(3). What prints now?
# Your answer:
>>>>>>> upstream/main
#


# ===== 4. While Loop, Live =====
<<<<<<< HEAD
# Count up from 0 and stop after 3, so the output is 0, 1, 2, 3 on separate
# lines.
#
# DISCUSS: Before you write the While Loop, Live code, put these steps in the
#          order Python runs them. A: Run the loop body. B: Check the condition
#          again. C: Check the condition the first time.
# Your answer: C, A, B
=======
# Count up from 0 and stop after 3, printing 0, 1, 2, 3.
# DISCUSS: Put these in order: A: run body. B: check again. C: first check.
# Your answer:
>>>>>>> upstream/main
#
print('----- 4. While Loop, Live -----')
# TODO: write a while loop that prints 0, 1, 2, 3 (check the condition!)
count = 0
while count <=3:
    print(count)
    count += 1

<<<<<<< HEAD
# PREDICT before you run: In the While Loop, Live code above, change count <= 3
#                         to count < 3. How many numbers print?
# Your answer: 
# 3 numbers print : 0, 1, and 2
=======
# PREDICT before you run: Make it count < 3, not count <= 3. How many print?
# Your answer:
>>>>>>> upstream/main
#


# ===== 5. Loop and Conditional, Together =====
# Label each score: 90+ gets "great job", lower gets "keep practicing".
print('----- 5. Loop and Conditional, Together -----')
# TODO: loop over scores; print "great job" if a score is 90 or above
# TODO: otherwise print "keep practicing"
scores = [88, 92, 75, 100]
for score in scores:
    if score >= 90:
        print(f"Wow great job! You got a {score}")
    else:
        print(f"I'm disappointed.I expected better. You only got a {score}")
