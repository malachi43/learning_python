"""
A tuple is a sequence of values. The values can be any type, and they are indexed by integers, so in that respect tuples are a lot like lists. 
The important difference is that tuples are immutable.
"""
t1 = "a","b","c","d","e"
t2 = ("a","b","c","d","e")
print(type(t1))
print(type(t2))
# type(t1) is equal to type(t2)
# To create a tuple with a single element, you have to include a final comma: e.g t1 = "a",
t3 = "a", #the trailing comma makes it a tuple and not a str.
print(type(t3))
t4 = tuple() # this creates an empty tuple.
print(type(t4))

"""
If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of the sequence. See example below
"""

t5 = tuple("malachi")
print(t5) # -> ('m', 'a', 'l', 'a', 'c', 'h', 'i')
letter_c = t5[4]
chi = t5[4:7] # this creates a new tuple ->  ('c', 'h', 'i')
name = ("O",) + t5[2:4]
print("name: ",name) # ->  ('O', 'l', 'a') this a new tuple

"""
The relational operators work with tuples and other sequences; 
Python starts by comparing the first element from each sequence. 
If they are equal, it goes on to the next elements, and so on, until it finds elements that differ. 
Subsequent elements are not considered (even if they are really big). See example below:
"""
print((0,1,2) < (0,3,4))
print((0,1,2_000_000) < (0,3,4))



"""
For tuple assignment, the right side can be any kind of sequence(string,list or tuple), see example below:
"""
list1, list2, list3 = [2,4], [6,4], [9,5]
print("list1 -> ", list1, " list2 -> ",list2, " list3 -> ", list3)
username, domain = "johndoe@gmail.com".split("@")
print("username -> ", username, "domain ->", domain)


quotient, remainder = divmod(7,3)
print("quotient -> ",quotient, "remainder -> ", remainder)

# We can return multiple values from a function in the form a tuple.

"""
Functions can take a variable number of arguments. 
A parameter name that begins with * gathers arguments into a tuple. See example below:
"""
def min_max(*args):
    return ( min(*args), max(*args) )


min, max = min_max(9,66,34,2,1,44,43,77,56,34,21)
print("minimun value is: ", min)
print("maximum value is: ", max)

"""
The complement of gather is scatter. If you have a sequence of values and you want to pass it to a function as multiple arguments, you can use the * operator. 
For example, divmod takes exactly two arguments; it doesn't work with a tuple:
"""
values = (13,3)
ans = divmod(*values)
print("ans: ",ans)

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print("total_sum of [1,2,3,4,5,6,7,8,9,10] -> ",sum_all(1,2,3,4,5,6,7,8,9,10))

letters = "abcdef"  # this is a sequence
index = [1,2,3,4,5] # this is a sequence
zipper_result = zip(letters, index) # it interleaves both sequence as a pair, zipper_result is an iterator
print("zipper_result",zipper_result)

# The sequence with the minimum length determines the number of pairs
for (a_letter, an_index) in zipper_result: # we used tuple assignment in this case (a_letter, an_index)
    print("a_letter: ", a_letter)
    print("an_index: ", an_index)
    print("-------------")


# We can convert an iterator in a list using this expression list(iterator). See example below:

an_iterator = zip("LAGOS","lagos")
for item in list(an_iterator):
    print(item) # each item is a tuple


array = dict()
array["a"] = "apple"
array["b"] = "ball"

for item in array.items():
    print("item: ",  item)