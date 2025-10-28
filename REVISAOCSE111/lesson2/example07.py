import math

number = float(input("enter a number: "))

root = math.sqrt(number)

print(f"The square of the number is {root:.2f}")

if root < 100:
    print("The square root is less than 100")
elif root >100:
    print("The square root is more than 100")
else:
    print("The square root is exactly 100")


    