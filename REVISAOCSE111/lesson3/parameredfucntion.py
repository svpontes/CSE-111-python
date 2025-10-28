#Functions can accept multiple parameters

def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input("first name: ")

first_name_initial = get_initial(first_name, True) #False means the force_uppercase will not return upper letter

print(first_name_initial)
