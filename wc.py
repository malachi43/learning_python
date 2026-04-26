
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print("The current value of __name__ is: ", __name__)


"""
___name___ this variable is set when the program runs,
If the program is ran as a script the value of __name__ is "__main__"
"""
if __name__ == "__main__":
    print(linecount("words.txt"))