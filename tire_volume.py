from math import pi
from datetime import datetime

"""Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.
v is the volume in liters,
π is the constant PI which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches. 

Gets the current date from the computer's clock.
Opens a text file named volumes.txt for appending.
Appends to the end of the volumes.txt file one line of text that contains the following five values:
current date
width of the tire
aspect ratio of the tire
diameter of the wheel
volume of the tire"""
tire_2056015 = 59.99
tire_1855014 = 39.99
others = 79.99
 
current_date_time = datetime.now()
print(f"{current_date_time:%Y-%m-%d}")
print()
w = int(input("What is the tire width ? "))
a = int(input("What is the tire aspect ratio ? "))
d = int(input("What is the  tire diameter ? "))
v = round(pi*w*w*a*(w*a+2540*d)/10000000000,2)
phone_number = ""
print()
print(f"The volume of the tire you choose is {v:.2f} liters")
print()
ask = "Y".lower()

if v == 39.92:
    print(f"The price for tire {w} {a}R {d} is U$ {tire_2056015}")
elif v == 24.09:
    print(f"The price for tire {w} {a}R {d} is U$ {tire_1855014}")
else:
    print(f"The price for tire {w} {a}R {d} is U$ {others}")
ask = input(f"Would like to buy the tire {w} {a} {d}? Y or N ")
if ask == "y":
    phone_number = input("Please digit your phone number: ")
    print(f"Your phone number is {phone_number}")
else:
    print("Thank you!")
with open("volume.txt", "at") as tire_volume:
    print(f"Today {current_date_time:%Y-%m-%d}", file = tire_volume) 
    print(f"Width: {w} Aspect Ratio: {a} Diameter: {d} Volume: {v:.2f} Phone Number:{phone_number}", file = tire_volume)
