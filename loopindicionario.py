
def main():
    # Create a dictionary with student IDs as the keys
    # and student data stored in a list as the values.
    students = {
        "42-039-4736": ["Clint", "Huish", "hui20001@byui.edu", 16],
        "61-315-0160": ["Michelle", "Davis", "dav21012@byui.edu", 3],
        "10-450-1203": ["Jorge", "Soares", "soa22005@byui.edu", 15],
        "75-421-2310": ["Abdul", "Ali", "ali20003@byui.edu", 5],
        "07-103-5621": ["Michelle", "Davis", "dav19008@byui.edu", 0],
        "81-298-9238": ["Sama", "Patel", "pat21004@byui.edu", 8]
    }

    # index da lista de itens.
    given_name_index = 0
    surname_index = 1
    email_index = 2
    credits_index = 3

    total = 0

    # para cada item na na lista adicionar o numero de de credito que cda estudadnte conquistou
    for key, value in students.items():
        

        # recupera o numero de credito da lista  de value list.
        credits = value[credits_index]

        # adiciona o numero de creditos para  total.
        total += credits

    print(f"Total credits earned by all students: {total}")


# Call main to start this program.
if __name__ == "__main__":
    main()