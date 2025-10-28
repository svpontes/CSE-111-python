def main():

    students = {
        
        #STUDENT id      givenName, surname, email, credits
        "42-039-4736": ["Clint", "Hushi", "hui2001@byui.edu", 16],

        "61-315-0160": ["Michelle", "Davis", "davis21555@byu.edu", 20],

        "21-169-0712": ["Sergio", "Pontes", "vieirasergio@byui.edu", 25]


    }

    #maneira mais fácil de encontrar os itnes em um diciionario. Vamos indexar os itens em variaveis:
def consulta():
    
    given_name_index = 0
    surname_index= 1
    email_index = 2
    credits_index = 3
    #supomos que o imput foi a chave 42-039-4736   
    id = input("Enter the id number: ")
    #id representa a chave key "42-039-4736"
    #se 42-039-4736 in (existir) em students(dicionario
    if id in students:
        #variavel value recebe os valores da chave 42-039-4736 do dicionario students
        value = students[id]
       #variavel = dicionario[chave] 

        print(value)
        #            "42-039-4736" 
        #variavel = #student[id]  [0]
        given_name = value[given_name_index]
        
        #variáveçl surname =recebe value(que representa porque ja recebeu id(chave) do dicionario students[surname_index é o indexer 0]portanto vai mostar o valor da posição ZERO)
        surname = value[surname_index]

        print(f"The first name is {given_name} and last name {surname}")
    else:
        print("No such student")
    
if __name__ == "__main__":
    main()



