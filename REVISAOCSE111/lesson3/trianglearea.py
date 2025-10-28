import math
def main():
    #lenght of each side
    side1 =float(input("side 1: "))
    side2=float(input("side 2: "))
    side3=float(input("side 3: "))

    triang_area = triangle_area(side1, side2, side3)

    print(f"the triangle area is: {triang_area:.2f}")

#compute and return the area of a triangle with side lenghts, a, b and c
# 
def triangle_area(a,b,c):
    sides = (a+b+c)/2
    area = math.sqrt(sides*(sides-a)*(sides-b)*(sides-c))
    return area

if __name__ == "__main__":
    main()
