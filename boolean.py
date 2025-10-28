gpa = float(input("Qual o GPA do aluno? "))
lowest_grade = float(input("Qual a lowest grade do aluno? "))
if gpa >= 0.85 and lowest_grade >= 0.70:
    honour = True
else:
    honour = False

if honour:
    print("Well Done!")