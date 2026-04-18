x = 39
if x > 0:
    print(str(x) + " is positive.")


# An if condition cannot have an empty body, the reason we use the pass statement
if x < 0:
    pass #TODO: need to handle negative values.


if x % 2 == 0:
    print(str(x) + " is even")
else:
    print(str(x) + " is odd.")


y = 107

if x > y:
    print(str(x) + " is greater than " + str(y))
elif x < y:
    print(str(y) + " is greater than " + str(x))
else:
    print(str(x) + " and " + str(y) + " are equal.")



# Nested conditionals

if x == y:
    print(str(x) + " and " + str(y) + " are equal.")
else:
    if x > y:
       print(str(x) + " is greater than " + str(y))
    else:
       print(str(y) + " is greater than " + str(x))


# Using logical operator

n = 9
if 0 < n and n < 10:
    print(str(n) + " is a single positive digit.")


# Simplified version
if 0 <  n < 10:
    print(str(n) + " is a positive single-digit number.")


# RECURSION

def countdown(n):
    if( n <= 0):
        print("BlastOff!!!")
    else:
        print(n)
        countdown(n - 1)


def print_n(s, n):
    if n <= 0:
        return
    else:
        print(s)
        print_n(s, n - 1)

