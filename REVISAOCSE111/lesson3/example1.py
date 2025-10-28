from datetime import datetime

#function that print the current date
def print_time():
    print(datetime.now())
    print()
#function get the fist letter of a name
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("Enter first name: ")
#variable       recebe= 0 posição, 1 first character
first_name_initial = first_name[0:1]

last_name = input("Enter the last name: ")
last_name_initial=get_initial(last_name)


print(f"Initials are: {first_name_initial} and {last_name_initial}")

def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("first name: ")

first_name_initial = get_initial(first_name)
#chamando a função def get_initial(name)

last_name = input("last name: ")
last_name_initial = get_initial(last_name)

print(f"{first_name_initial}  {last_name_initial}")

print_time()