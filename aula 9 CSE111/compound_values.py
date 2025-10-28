#listas compostas são aquelas formadas por várias strings dentro de uma mesma linha

#indexar items da lista:
#exemplo "10-123-4562" : ["Sergio", "Pontes", "pontes_sergio@hotmail.com", 69]

#   "id" : "nome", "sobrenome", "email", "ano_nasc"

def main():

    alunos = {
        "10-123-4562": ["Sergio", "Pontes", "pontes_sergio@hotmail.com", 1669],
        "10-123-4563": ["Tatiana", "Pontes", "tatiana_lima@hotmail.com", 1979],
        "10-123-4564": ["Esther", "Esteves", "freeesther@gmail.com", 2004],
        "10-123-4565": ["Bernardo", "Lima", "frebernar@gmail.com", 2002]
    }
    print (alunos)

    #index dos itens do dicionario:

    nome_index = 0
    sobrenome_index = 1
    email_index = 2
    ano_nasc_index = 3

    #utilizando id como indice para pesquisa de um input: vou susar uma variável chamada "id"
    
    id = input("Favor digite sei ID: ")
    if id in alunos:
        value = alunos[id]
        nome = value[nome_index]
        sobrenome = value[sobrenome_index]
        email = value[email_index]
        nascimento = value[ano_nasc_index]

        print(f"seu nome é: {nome} {sobrenome}\n Email: {email}\nNascido a: {nascimento}")
    else:
        print("No such student")


# encontrar um item na lista:
    print(alunos["10-123-4563"])

    value = alunos["10-123-4562"]
    print(value)


if __name__ == "__main__":
    main()