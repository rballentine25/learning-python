import math

def areaOfCircle(radius):
    area = math.pi * (radius**2)
    return area

radius = input("enter the radius of the circle as an integer: ")

try: 
    radius = int(radius)
    print("your circle has an area of", areaOfCircle(radius))
except:
    print("your number was not an integer.")


