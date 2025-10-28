def main():
    students = {
   
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Michelle Davis",
    "10-450-1203": "Jorge Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Michelle Davis"

    }
    #adiciona um item ao dicionario
    students ["44-039-4786"] = "Sergio Pontes"

    #remove um item do dicionario
    students.pop("42-039-4736")

    length = len(students)

    print(f"A quantidade de estudantes atual é de: {length}")

    print(students)

    id = input("Enter your id: ")

    if id in students:
        name = students[id]

        print(name)
    else:
        print("No such student")

if __name__ == "__main__":
    main()