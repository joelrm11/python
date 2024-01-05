import math
def areaofCircle(r):
    return math.pi*r*r

def areaofrec(l,b):
    return l*b

def makesquare(x):
    return x**2

def checkprime(n):
    for i in range(2,n//2):
        if i%2==0:
            return False
    return True

def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
