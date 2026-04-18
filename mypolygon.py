import turtle
import math

bob = turtle.Turtle()

def square(t, length):
   for i in range(4):
    t.fd(length)
    t.lt(90) 
   turtle.mainloop()



def polygon(t, n, length):
   angle = 360/n
   for i in range(n):
    t.fd(length)
    t.lt(angle) 
   turtle.mainloop()


def circle(t,r):
  circumference = 2 * math.pi * r
  n = 50
  length = circumference / n
  polygon(t,n,length)
