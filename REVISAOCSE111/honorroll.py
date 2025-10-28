
gpa = float(input("What is your gpa: "))

lowest_grade = float(input("enter your lowest grade: "))


if gpa >= 0.85:
    if lowest_grade >= 0.71:
        print("Well done!")

if gpa <= 0.7 and lowest_grade < 0.5:
    print("Almost there")

else:
    print("Sorry")