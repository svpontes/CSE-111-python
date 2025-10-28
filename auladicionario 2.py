def main():
    students = {
        #key              value
        "42-039-4736" : "Clint Huish",
        "61-315-0160" : "Michelle Davis",
        "10-450-1203" : "Jorge Soares",
        "15-421-2310" : "Abdu Ali",
        "07-103-5621" : "Michelle Davis"
        }
    print(students["42-039-4736"])
    print(students)

    #adicionar um studante:

    students["81-298-9238"] = "Sergio Pontes"

    print(students)

    #remover um estudante:

    del students["07-103-5621"]
    # ou pode deletar usandoa funcao pop

    students.pop("81-298-9238")
    print(students)

    #usar len para achar quantos itens exutem no dicionario de students

    lenght = len(students)

    print(f"the length of students is {lenght}")

    #utilizando a função if no dicionarios de estudantes

    #quero saber se um determinado chave que vou chamar de id atraves de uma  variável
    students["01-522-065"] ="Sergio Pontes"

    print(students["01-522-065"])

    id = input("Enter your student Id: ")
    if id in students:
        name = students[id] # a variavel name recebe
                            # o input id e depois de
                            # analizado po if responde
                            # retornando o nome do aluno aparitr do dicionario students onde o id est+a relacionado 
        print(name)
    else:

        print("Não há aluno com esse Id")

if __name__ == "__main__":
    main()

    