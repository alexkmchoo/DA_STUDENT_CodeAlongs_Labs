#!/usr/bin/env python3
"""Day 4 code-along: Local vs. Global Variables & Scope. Run: python3 <file>"""

# ===== 1. Local Scope, Live =====
# Find out if a variable made inside a function exists outside it.
# TODO: run it, read the NameError, then comment out the raising line
# DISCUSS: Order: A: total disappears. B: make_total() runs. C: total = 100.
# Your answer:
#
print('----- 1. Local Scope, Live -----')
<<<<<<< HEAD
samsung = 70
def make_total():
    x = 100
    return x * samsung
    
phone = make_total()
print(phone)
    #return x 
    #print(x)
#print(x)
#print(make_total())  
#print(x)

# TODO: define make_total() with a local variable total set
# to 100, returning it, then try printing total outside the
# function and watch what happens

# DISCUSS: Now try a new function. set_x() runs and sets x = 5 inside it, but
#          print(x) outside raises NameError. Why?
def set_x():
    x = 5
    print(x)

set_x()

# Your answer:
# because print exists inside the function, if you set it outside python can't read it
# it cant read what x is since it is outside the function
=======
# TODO: define make_total(): set a local total to 100 and return it
# TODO: print total outside the function and see what happens

# DISCUSS: set_x() sets x = 5, but print(x) outside raises NameError. Why?
# Your answer:
#
>>>>>>> upstream/main


# ===== 2. Reading a Global, Live =====
# Price a $100 item with 8% tax, using a tax rate stored outside the function.
print('----- 2. Reading a Global, Live -----')
<<<<<<< HEAD
tax_rate = 0.08
def price_with_tax(price):
    x = price + (price * tax_rate)
    return x 

print(price_with_tax(100))

# TODO: define tax_rate as a global, then write
# price_with_tax(price) that reads it without taking it as
# a parameter
=======
# TODO: define tax_rate as a global
# TODO: write price_with_tax(price) that reads tax_rate directly
>>>>>>> upstream/main

# DISCUSS: Move price_with_tax to a file with no tax_rate. Why does it break?
# Your answer:
<<<<<<< HEAD
# it doesn't have a global variable to call to, since in our function we have a global variable tax_rate
=======
>>>>>>> upstream/main
#


# ===== 3. Refactor: Global to Parameter =====
# Pass the tax rate in as a parameter. It should still print 108.0.
print('----- 3. Refactor: Global to Parameter -----')
<<<<<<< HEAD
# TODO: rewrite price_with_tax so tax_rate is a parameter
# instead of a global it secretly reads
#tax_rate = 0.08
def price_with_tax(price, c_tax_rate):
   return price + (c_tax_rate * price ) 

print(price_with_tax(20000, 1.1))
=======
# TODO: rewrite price_with_tax to take tax_rate as a parameter
tax_rate = 0.08
>>>>>>> upstream/main
