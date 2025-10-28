#example 5 aula 9
# utiliza-se o laço for para fazer um loop e iterar sobre os itens do dicionario

def main():

    alunos = {
        "10-123-4562": ["Sergio", "Pontes", "pontes_sergio@hotmail.com", 1669, 1000],
        "10-123-4563": ["Tatiana", "Pontes", "tatiana_lima@hotmail.com", 1929, 1000],
        "10-123-4564": ["Esther", "Esteves", "freeesther@gmail.com", 1904, 1000],
        "10-123-4565": ["Bernardo", "Lima", "frebernar@gmail.com", 2002, 1000]
    }

#método get() retorna None que é um valor padrão já estipulado. Nos testes é bem usado.    

    item = alunos.get("10-123-4569", None)
    print(item)
    if item is None: print(f"Retornou {item}, logo este item não existe ")

#posso pedir para exibir somente os valores e retornar como uma lista os itens do dicionario sem as chaves: método value

    for valor in alunos.values():
        print(valor)

        print()
        print()

# aqui retorna os itens com as chaves
# método item
    for item in alunos.items():
        print(item)
        print()
        print()

      #posso retornar a chave separada também.
       
    for item in alunos.items():
        chave, valor = item
        print(chave)
        print(valor)
    print()
    print()

    #posso imprimir itens separados também:

    for item in alunos.items():
        chave, valor = item
        name_index,sobrenome_index, email_index, ano_nasc_index, ordenado_index = valor

        print(email_index)

        print()
        print()

  



#retornar as chaves do dicionario:

    chave = alunos.keys()
    print(f" as chaves são {chave}")

    print()
    print()
    print()

    name_index = 0
    sobrenome_index = 1
    email_index = 2
    ano_nasc_index = 3
    ordenado_index = 4
#posso usar esse método para manipular algum item no dicionario através da chave.
#-----------------------------------------------
    print("-----------------------------------------")

    for chave in alunos.keys():
        if alunos[chave] [3] >= 1969:
            print(f"Os Alunos nascidos depois de 1969 são: {alunos[chave]}")
        elif alunos[chave] [4] <= 1000:
            alunos[chave][4] += 1000

            print()
            print()

      #quero manipular os ordenados:
             
    print("-----------------------------------------")
    print("-----------------------------------------")

    total = 0 #essa variável será utilizado para somar as idades 
#IMPORTANTE:  item é um método no formato

    for key, value in alunos.items():
        
        idades = value[ano_nasc_index]
        total += idades
    print(f"a soma das idades é de {total}")

if __name__ == "__main__":
    main()