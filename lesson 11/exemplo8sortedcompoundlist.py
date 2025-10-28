# utilizando a função key é possível classificar uma lista ordenada com uma chave que não está na lista. Considere a lista composta de alunos no exemplo abaixo. O nome e sobrenome estão armazenados separadamente. é comum uma lista de nomes começar com sobrenome e depois o nome. Podemos escrever uma função que combina nome e sobrenome que passaram a ser a chave.
"""def main():
# [given_name, surname, reading_level]
    alunos =[
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8]
    ]

    nome_index = 0
    sobrenome_index = 1

    #definir a chave atravé de uma pequena função lambda:

    nome_e_sobrenome_lista = lambda alunos:f"{alunos[sobrenome_index]}, {alunos[nome_index]}"

    lista_classificada = sorted(alunos, key=nome_e_sobrenome_lista)

    for alunos in nome_e_sobrenome_lista:
        print(alunos)

if __name__ == "__main__":
    main()""" 

# Example 8

def main():
    # Create a list that contains data about young students.
    students = [
        # [given_name, surname, reading_level]
        ["Robert", "Smith", 6.7],
        ["Annie", "Smith", 6.2],
        ["Robert", "Lopez", 7.1],
        ["Sean", "Li", 5.6],
        ["Sofia", "Lopez", 5.3],
        ["Lily", "Harris", 6.7],
        ["Alex", "Harris", 5.8]
    ]

    GIVEN_INDEX = 0
    SURNAME_INDEX = 1

    # Define a lambda function that combines
    # a student's surname and given name.
    combine_names = lambda student_list: \
        f"{student_list[SURNAME_INDEX]}, {student_list[GIVEN_INDEX]}"

    # Sort the list by the combined key of surname, given_name.
    sorted_list = sorted(students, key=combine_names)

    # Print the list.
    for student in sorted_list:
        print(student)


# Call main to start this program.
if __name__ == "__main__":
    main()