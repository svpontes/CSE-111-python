import math
#functions details:

#LOCAL Scope --> When it inside a function
#GLOBAL Scope --> Outside the all functions
#example:
"""
discount = 0.10 Observe the variable (discount) its outside the all functions

def main()
    x = 1   observe that the variable x its inside the function
"""

def main():

    radius = float(input("enter the radius of a circle: "))
    area = circle_area(radius)
    print(f"the area is: {area:.1f}")

def circle_area(radius):
    area = math.pi * radius * radius
    return area
if __name__ == "__main__":
    main()