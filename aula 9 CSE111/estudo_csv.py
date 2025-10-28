# sintaxe:
#    dictionay_name = {
#         "id": "student", where:
#       id is a KEY : student is a VALUE
#       }
def main():

    students = {    
        "ID":"name",
        "1001":"Sergio Pontes",
        "1021":"Tatiana Lima",
        "1031":"Bernardo Esteves",
        "1041":"Murilo Pontes",
        "1051":"Esther Lima"
        }
    
#PRINT retorna o dicionario inteiro
    print(students)

#for loop Variável que chamei de "id" no dicionario "students" retorna todas as chaves "KEYS" no print
    for id in students:
        print(id)

# print na KEY (chave) retorna o VALUE (valor)
    print(students["1001"])

    print(students["1031"])

# PRINT de quantos alunos cadastros com "len"    

    print(f"The amount of students registered is: {len(students)}")

# utilizar um input para achar um aluno pelo id
    id = input("Enter id Number: ")
    if id in students:
        name = students[id]
        print(name) 

if __name__ == "__main__":
    main()

"""
se id 1001 estiver dentro do dicionario students
variavel name recebe o valor de 1001 do dicionario students
"""