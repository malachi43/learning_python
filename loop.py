

# while True:
#     line = input("> ")
#     if line == "done":
#         break
#     print(line)
# print("Done!")

name = "Malachi Uko"

# index = 0

# while index < len(name):
#     character = name[index]
#     print("char: ", character)
#     index = index + 1

def printInReverse(text):
    index = len(text) - 1
    while index >= 0:
        char = text[index]
        print(char)
        index = index - 1


printInReverse("Malachi")

for char in name:
    print("character: ", char)



prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O":
        print(letter + "u" + suffix)
    elif letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)
   