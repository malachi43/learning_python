import turtle


# a = int(input("Enter value for a:\n"))
# b = int(input("Enter value for b:\n"))
# c = int(input("Enter value for c:\n"))
# n = int(input("Enter value for n:\n"))

def check_fermat(a,b,c,n):
    if n <= 2:
        result = (a ** n) + (b ** n)
        if result == (c ** n):
            print("Holy smokes, Fermat was wrong!")            
    else:
        print("No that doesn't work.")


    

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t,length,n - 1)
    t.rt(2 * angle)
    draw(t,length,n - 1)
    t.lt(angle)
    t.bk(length * n)


def compare(x,y):
    if x >  y:
        return 1
    elif x < y:
        return -1
    else:
        return 0



def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num -1) + fibonacci(num - 2)
    
def factorial(num):
    if not isinstance(num, int):
        print("Factorial is only defined for integers")
        return None
    elif num < 0:
        print("Factorial is only defined for positive integers.")
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
print(factorial(-5))

print("malachi"[1:-1])

animal = "monkey"

print("animal: ",animal[:])
