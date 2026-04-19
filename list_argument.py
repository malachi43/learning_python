letters = ["a","b","c","d"]

# When you pass a list to a function, the function gets a reference to the list. If the function modifies the list, the caller sees the change. 
def delete_head(arg):
    del arg[0]

print("letters: ", letters)
delete_head(letters) # The list letters is mutated
print("letters: ", letters)

#This returns a new list while the original list is not mutated.
def tail(arg):
    return arg[1:]


print("tail: ", tail(letters))
print("letters: ", letters)

m1 = [10,11,12]
m2 = 97
#m1.append(m2) # or this m1 = m1 + [x] or this m1 += [x] = [10,11,12,97]
m1 = m1 + [97] # [10,11,12,97]
print("new value of m1: ", m1)

# If you want to use a method like sort that modifies the argument, but you need to keep the original list as well, you can make a copy.
t1 = [3,2,1]
t2 = t1[:]
t2.sort()
print("t1: ", t1)
print("t2: ",t2)

# object: Something a variable can refer to. An object has a type and a value. 
# equivalent: Having the same value.
# identical: Being the same object (which implies equivalence).
# reference: The association between a variable and its value.
# aliasing: A circumstance where two or more variables refer to the same object.