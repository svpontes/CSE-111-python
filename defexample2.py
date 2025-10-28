#essa função get_initial(name) name aqui é o parâmetro que será armazenado na variável initial retornado (return)
# o que está sendo pedido dentro do colchete ou seja 0 é a primeira letra do intervalo 0:1
def get_initial(name):
    initial = name[0:1].upper()
    return initial
first_name = input("enter your first name: ")
first_name_initial = get_initial(first_name)

midlle_name = input("enter your midlle name: ")
midlle_name_initial = get_initial(midlle_name)

last_name = input("enter your last name ")
last_name_initial = get_initial(last_name)

def get_email(email): # função para pegar o email do cliente, armazenar na variável client_email e retornar em letras minusculas
    client_email = email
    return client_email.lower() 

email_entered = input("enter your email ") #variavel criada para receber o email do cleinte
emailfromclient = get_email(email_entered) #variável que recebe (armazena o email digitado) e chama a função get_email


print("Your initials are: " + first_name_initial + midlle_name_initial + last_name_initial)
print("your email is: " + emailfromclient)