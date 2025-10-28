import csv


def main():

    inumber = 0
    name = 1

    students = read_dict("students.csv", inumber)

    inumber = str(input("Enter your 9 digits Number Id: "))
    
    inumber = inumber.replace("-", "")
    
    lenght_entered_student_id = len(inumber)
    
    if not inumber.isdigit():
        print("Invalid character in I-Number")
                
    else:
               
        if lenght_entered_student_id < 9:
            print(f"You entered {lenght_entered_student_id} number(s). Please enter 9 digits students Number Id: ")    
        
        elif lenght_entered_student_id > 9:
                print(f"You digit {lenght_entered_student_id} number(s), please enter the 9 digits Students Number Id: ")
        
        else:
            if inumber in students:
                value = students[inumber]
                name = value[name]
                print(f"I-NUMBER: {value} STUDENT: {name}")
           
            else:
                print("No such Student!")    
    
    
def read_dict (filename, key_id_column_index):

    dictionary = {}

    with open(filename, mode="rt") as students_csv_file:

        reader = csv.reader(students_csv_file)

        next(reader)
    
        for row in reader:
            key = row[key_id_column_index]

            dictionary[key] = row
    
    return dictionary

if __name__ == "__main__":
    main()