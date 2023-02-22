def beräknaArea(sida1, sida2):
    area = sida1*sida2
    return area
    beräknaArea(3, 9)
print(beräknaArea(3, 9))

def alternativtBeräknaArea(sida1, sida2):
    print(sida1*sida2)
    alternativtBeräknaArea(3, 15)
print(alternativtBeräknaArea())

def adderaSiffror(siffra1, siffra2):
    summa = siffra1+siffra2
    return summa

def adderaEnSidaTillArea(x, y):
    a = x*y+y
    return a

def adderaSidorna(x, y):
    print(x+y)

def triangelArea(x, y):

    print(x * y /2)
    triangelArea(5, 10)

#import numpy as np låt denna vara, återkommer till import
#def funktion(a, b):
# c = np.sqrt(a*a + b*b)
# return c
#funktion(3, 4)

#input(())