#!/usr/bin/env python3
"""Lab: Solo Class Design Rep
GitBook Quest 1.8: Meet the Objects

HOW TO RUN
    Open a terminal in this file's folder and run:
        python3 solo-class-design-practice_STUDENT.py
    Or make it executable once:
        chmod +x solo-class-design-practice_STUDENT.py
    and from then on run it directly:
        ./solo-class-design-practice_STUDENT.py
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
    Commit this file (you may rename it solo-class-design-practice.py) to your own data
    challenge repo, inside your Module 1 folder. Paste its direct GitHub URL
    into the LMS.
"""

# ===== Step 1: Read the Stakeholder Need =====
# A new stakeholder need. Not the board-game or office-supply domain from
# lecture, and not one of the project's own 4 scenarios.

# Your answer:
# The volunteer coordinator of the local community center that lends tools. They need a way to track each tool,
# which tools are available to borrow, and whether the power tools are available to use right now due to inspection.


# ===== Step 2: Decide Your Attributes, Each With a Reason From the Scenario =====

# Your answer:
# Name of the tool, tools available, total stock of tools, needs inspection, status, and last checkout date
#

# ===== Step 3: Write __init__ and a Method, From Scratch =====
# There is no single correct design here. Your class name, your attribute
# names and your method can all differ from everyone else's and still be
# right. The test is whether each one traces back to the stakeholder
# paragraph.
import json
from datetime import date 
DATA_FILE = "/Users/alexc/Documents/DA_STUDENT_CodeAlongs_Labs/module-1-python-foundations/data-challenges/data/tool_records.json"  # edit the filepath with the data

with open(DATA_FILE) as f:
    tool_records = json.load(f)

# TODO: Write __init__ and a Method, From Scratch
class Tools:
    def __init__(self, name, tools_available, total_stock, needs_inspection, status, last_checkout, passed_inspection):
        self.name = name
        self.tools_available = tools_available
        self.total_stock = total_stock
        self.needs_inspection = needs_inspection
        self.status = status
        self.last_checkout = last_checkout
        self.passed_inspection = passed_inspection
        # identified the attributes of my class
    def availability(self):
        if self.tools_available == 0:
            return False, "no you can't borrow this"
        # return no if we don't have any avaiable stock for you to borrow
        if self.needs_inspection and not self.passed_inspection:
            return False, "not ready, needs to pass inspection first"
            # if a power tool needs inspection AND it hasn't passed inspection yet
            # return false because it needs to pass inspection first
        return True, "ok ready to borrow"
        # otherwise ok, its ready to borrow
    def check_out(self):
        ok,reason = self.availability()
        # unpacking this because availablity is true or false + message so ok (or not ok) + reason
        if not ok:
            return reason
            # otherwise don't change anything
        self.tools_available -= 1
        # if you can check it out, tools available drops by 1 every time
        self.last_checkout = date.today().isoformat()
        # if you can check it out, last checkout date (ID) also updates to today
        # made this from the import that Tina showed me.
        if self.tools_available == 0:
            self.status = "checked out"
            # if the tools_available ever drops to 0, the status updates to checked out, since none is in circulation
        return "checked out!"
        # otherwise if its already at 0, it just returns checked out
def tool_list(tools, name_of_tool):
    # made a function for the tool list to portray list of tools
    for tool in tools:
        if tool.name == name_of_tool:
            return tool
    raise ValueError(f"Name a tool | {name_of_tool}")
    # raised an error here, to follow up with the user input function
def is_tool_available(tools):
    while True:
        x = input("Enter tool name:")
        try:
            tool = tool_list(tools, x)
        except ValueError:
            print("Sorry, we don't have that tool. Did you misspell it? Make sure it's capitalized")
            #user might mispell the tool name or put it in lowercase like hammer or ladder or Pressure washer 
            y = input("press y to see the list of tools or press any other key to try again")
            # option to see the list of tools they can borrow (helps them with the name for correct input)
            if y == "y":
                for bbq in tools:
                    print(f'{bbq.name} | availablity: {bbq.tools_available}')
                    # if they want to see the list, prints out names of tools + availablity
            continue
            # continue so the program doesn't end
        print(f'{tool.name} | availablity: {tool.tools_available}')

# Help call this method PLEASE TINA

# ===== Step 4: Instantiate 2+ Objects, Confirm Independent Storage =====
# The same proof Day 13's lecture asked for, now on a class you designed
# yourself. Predict what each print() will show before you run it.


# TODO: Instantiate 2+ Objects, Confirm Independent Storage

# ===== Step 5: Justify Your Design Choice in 2-3 Sentences =====

# Your answer:
#
#

# ----- Share Out -----
# Last 15 minutes, back together as a class. Bring:
#
# Come ready to show your class and defend it. Specifically:
# - The attribute list you chose, and for each one, the phrase in the
#   coordinator's request it came from. If you can't point at a phrase for
#   an attribute, say so - that's a real finding, not a failure.
# - One attribute you considered and rejected, and why. - Your method: what
#   question does it answer, and why would the coordinator reach for it
#   first?
# - Anything you got stuck on. Designing from a paragraph with nobody to
#   check against is genuinely hard, and naming where it was hard is worth
#   more to the room than a tidy answer.
#
# Expect to be asked "why that attribute and not another?" - there is no
# single right list here, so the reasoning IS the answer.
#
# Be ready to answer "why did you do it that way?"

# Your notes for the share out:
#
#
