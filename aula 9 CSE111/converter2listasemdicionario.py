#exemplo 7 da aula 9

def main():

    #a primeira lista contem o id de 5 alunos:

    id = ["101","110","120","130","140", "150"]

    nomes = ["Sergio Pontes", "Tatina Lima", "Bernardo Esteves", "Murilo Pontes", "Esther Esteves"]

    #Usar dict e zip para converter as listas em dicionario:

    alunos = dict(zip(id, nomes))

    print(alunos)

    # agora o inverso: converter o dicionario em 2 listas que vou chamar de id_inverso e alunos_inverso

    id_inverso = list(alunos.keys())

    print(id_inverso)

    alunos_inverso = list(alunos.values())
    print(alunos_inverso)


if __name__ == "__main__":
    main()