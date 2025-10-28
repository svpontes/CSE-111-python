import math

def main():
    print("enter the length of each side: ")
    side1 = float(input())
    side2 = float(input())
    side3 = float(input())
    triangarea = triangle_area(side1,side2, side3)
    print(f"the area is {triangarea}")

def triangle_area(a, b, c):
    s = (a+b+c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

main()