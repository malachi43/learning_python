eng2sp = dict()
eng2sp["one"] = "uno"
print(eng2sp)
dictionary = {"one": "uno", "two": "dos", "three": "tres"}
print(dictionary)
print(dictionary["two"])
print("number of keys in dictionary: ", len(dictionary))
print("is 'three' in dictionary: ", "three" in dictionary)
print("is 'four' in dictionary: ", "four" in dictionary)

print("values in dictionary: ", dictionary.values())
print("is 'uno' in values: ", "uno" in dictionary.values())


def histogram(c):
    d = dict()
    for item in c:
       d[item] = d.get(item, 0) + 1
    return d

print(histogram("mississippi"))

def print_histogram(dictionary):
    for key in dictionary:
        print("key:", key, ", value: ", dictionary[key])
        # print("key:", key, ", value: ", dictionary.get(key))



print_histogram(histogram("parrot"))


def return_key_from_value(dictionary, value):
    key_list = []
    for key in dictionary:
        if dictionary[key] == value:
            key_list.append(key)
    return key_list


def find_key_from_value(dictionary, value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    """
    The raise statement causes an exception; in this case it causes a LookupError, 
    which is a built-in exception used to indicate that a lookup operation failed.
    """    
    raise LookupError("value: " + str(value) + " does not appear in dictionary") 


l_one = histogram("parrot")
print(return_key_from_value(l_one, 1))

find_key_from_value(l_one, 2)

# Map frequencies to keys
def inverse_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print("inverse_dict: ", inverse_dict(histogram("parrot")))


known = {0: 0, 1: 1}
def fibonacci(n):
    if n in known:
        return known[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = result
    return result


test_num = 100
print("fibonacci of " + str(test_num) + " is = ",fibonacci(test_num))


count = 0
lookup = {0:0,1:1}
def global_variable():
    global count # The global keyword allow the count to refer to the global count variable declared outside the function and not create a local one.
    count = count + 12
    print("lookup; ", lookup)
    print("new count value: ", count)

global_variable()