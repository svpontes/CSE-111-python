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

#The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
t_width = int(input("What is the tire width? Please provide milimeters measure! "))
t_a_ratio = int(input("What is the tire aspect ratio ? "))
t_diameter = int(input("What is the  tire diameter? Please provide inches measure ? "))

#volume calc
t_volume = round(pi*t_width**2*t_a_ratio*(t_width*t_a_ratio+2540*t_diameter)/10000000000)

phone_number = ""
print()
print(f"The volume of the tire you choose is {t_volume:.2f} liters")
print()
ask = "Y".lower()

if t_volume == 39.92:
    print(f"The price for tire {t_width} {t_a_ratio}R {t_diameter} is U$ {tire_2056015}")
elif t_volume == 24.09:
    print(f"The price for tire {t_width} {t_a_ratio}R {t_diameter} is U$ {tire_1855014}")
else:
    print(f"The price for tire {t_width} {t_a_ratio}R {t_diameter} is U$ {others}")
ask = input(f"Would like to buy the tire {t_width} {t_a_ratio} {t_diameter}? Y or N ")
if ask == "y":
    phone_number = input("Please digit your phone number: ")
    print(f"Your phone number is {phone_number}")
else:
    print("Thank you!")
with open("volume.txt", "at") as tire_volume:
    print(f"Today {current_date_time:%Y-%m-%d}", file = tire_volume) 
    print(f"Width: {t_width} Aspect Ratio: {t_a_ratio} Diameter: {t_diameter} Volume: {t_volume:.2f} Phone Number:{phone_number}", file = tire_volume)
