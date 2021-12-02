from math import pi
import time
import thread
def Area():
    try:
        r = float(input ("Input the radius of the circle : "))
        print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
        time.sleep(0.3)
    except:
        print("hoo")

def Multi():
    try:
        x=int(input("enter 1st number"))
        y=int(input("enter 2st number"))
        print('multiplication is',x*y)
        time.sleep(0.5)
    except:
        print("hiii")

def Div():
    try:
        n1=int(input("enter d1"))
        n2=int(input("enter d2"))
        print('Division is' , n1/n2)
    except:
        print("helo")
    
        
        
t1=time.time()
Area()
Multi()
Div()

