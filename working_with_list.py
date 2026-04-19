

list1 = [5,4,3,2,1]
list1[2] = 17

# replaces 2 element from index 2 through 4
list1[2:4] = [19,17] 


for i in range(len(list1)):
    list1[i] = list1[i] * 3

list1.sort()
# Add new list to existing list
list1.extend([99,88,77,55]) 


def add_all(t):
    total = 0
    for num in t:
        total += num
    return total


print("total: ",add_all([1,2,3,4,5]))

print("sum: ", sum([1,2,3,4,5]))



def capitalize_all(sentence):
    res = []
    for s in sentence:
        res.append(s.capitalize())
    return res
sentence = ["i","love","to","code."]


capitalized = capitalize_all(sentence)
print("capitalized: ", capitalized)

t = ["a","b","c"]
del t[2]
x = t.pop(1)
print("x: ", x)
print("t: ",t)

m = ["a","b","c","d","e","f"]
m.remove("a")
print("m: ",m)
del m[1:5]
print("m: ", m)

name = "malachi"
name_list = list(name)
print("name_list: ", name_list)


s = "The dog jumped over the fox."
t1 = s.split()
print("t1: ", t1)
delimiter = " __|__ "
new_str = delimiter.join(t1)
print("new string: ", new_str)

firstname = "chibuike"
first_name = "chibuike"
# "firstname is first_name" - this notation is used to check whether the two variables(firstname and first_name) refer to the same object.
print("is firstname variable equal to first_name variable: ", firstname is first_name)

# The association of a variable with an object is called a reference.
# An object with more than one reference has more than one name, so we say that the object is aliased.
n1 = [1,2,3]
n2 = n1
n1[0] = 19

# If the aliased object is mutable, changes made with one alias affect the other:
print("n2: ", n2) #The element at index n2[0] is change because both n1 and n2 reference the same object.

print("n2 is n1: ", n2 is n1)