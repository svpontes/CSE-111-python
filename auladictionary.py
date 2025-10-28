bad_guys = {
    #key: "values",
    "daredevil" : "kingpin",
    "x-men": "apocalyptise",
    "batman": "bane"
}

print(bad_guys)

print(bad_guys["daredevil"])

#adicionar um nova chave key e um valor para essa chave:
bad_guys["deadpool"] = "evil deadpool"

#mudar o valor de uma determinada:

bad_guys["x-men"] = "juggernaut"

#deletar uma chave automaticamentye deleta seu valor

del bad_guys["deadpool"]

print(bad_guys)


#outro importante conceito relativo a dicionarios:
#ele não usa index como em listas mas podemos
#atribuir números como keys ou chaves
#observe que os numeros não precisam estar entre aspas

dicionario = {

    0 : "name",
    1 : "endereço",
    3 : "cep",
    4 : "email",
    5 : "sexo"
}

print(dicionario[0])

# neste caso necessita estar entre aspas porque há o caracter - separando os numeros
def main():

    address = {

        "42-039-4736" : "Clint Huish",
        "61-315-0160" : "Michelle Davis",
        "10-450-1203" : "Jorge Soares",
        "15-421-2310" : "Abdu Ali",
        "07-103-5621" : "Michelle Davis"
        }


#se eu pedir um bad_guy que não está no dicionario
#o python retorna uma menssagem de erro de exceção

print(bad_guys["avengers"])

#aqui será o erro
