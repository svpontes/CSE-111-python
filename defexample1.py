#first letter of the name
def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].lower()#os números dentro dos colchetes determinan o intervalo
    else:
        initial = name[0:1]    
    return initial

#ask for the name and return initials

first_name = input("enter your first name: ")
first_name_initial = get_initial(first_name)
last_name = input("enter your last name: ")
last_name_initial = get_initial(last_name)

print("Your initials are: " + first_name_initial + last_name_initial)