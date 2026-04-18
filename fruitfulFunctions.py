import math

def area(radius):
    return math.pi * (radius ** 2)

def calculate_distance(x1,x2,y1,y2):
    change = ( (x2 - x1) ** 2 ) + ((y2 - y1) ** 2)
    return math.sqrt(change)

print(calculate_distance(x1 = 2, x2 = 5, y1 = 4, y2= 8))