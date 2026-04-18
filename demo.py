import math;


def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("This is a cool lyrics")
    print("This is another lyrics")

def print_twice(arg):
    print(arg)
    print(arg)

def cat_twice(line1, line2):
    cat = line1 + " " + line2
    print_twice(cat)

name = "Eric, the half bee."

arg1 = "Ting tang"
arg2 = "Ding dang"


def right_justify(s):
    print("The length of " + s + " is " + str(len(s)))
    newValue = (" " * 70) + s
    print(newValue)


def print_spam(s):
    print(s)


def do_twice(f,value):
    print_twice(value)
    print_twice(value)


