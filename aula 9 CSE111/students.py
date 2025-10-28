import csv

def main():
    #INDEXes of items in the columns in "students.csv"
    ID_NUMBER_INDEX = 0
    NAME_INDEX = 1

    #read the contents of "students.csv" into dictionary called students.
    #ID_NUMBER_INDEX is the key

    students = read_dict("students.csv", ID_NUMBER_INDEX)

    print(students)

def read_dict(filename, key_student_id_number_index):
    #this function read the content of students.csv file into a dictionary and return the dictionary

    #parameter key_column_index works as the key in the dictionary

    #DICTIONARY = {} this empty list will store the data from students.csv
    dictionary = {}

    with open(filename, "rt") as arquivo_csv:

        leitor = csv.reader(arquivo_csv,  key_student_id_number_index, delimiter=",")

        next(leitor)

        
        for coluna in leitor:
            
            key = coluna[key_student_id_number_index]
            dictionary[key] = coluna
            name = coluna[1]
            dictionary[name] = coluna
            
            student_id = input("Enter your 9 Digits Student ID, please:(xx-xxx-xxxx) ")
            student_id = student_id.replace("-", "")
            #identifica o tamanho do input student_id
            lenght_entered_student_id = len(student_id)
            
            if not student_id.isdigit():
                print("Invalid character for Student Id ")
            
                if lenght_entered_student_id < 9:
                    print(f"You digit{lenght_entered_student_id}, please complete enter the 9 digits")
                elif lenght_entered_student_id > 9:
                    print(f"You digit {lenght_entered_student_id}, please digit only 9 digits")
                elif lenght_entered_student_id == key:
                    print(f"I-NUMBER: {student_id} #STUDENT: {coluna}")
                else:
                    print("No such Student!")
        coluna.close()    
                        
                            
    print(f"items {dictionary}")
    return dictionary



if __name__ == "__main__":
    main()