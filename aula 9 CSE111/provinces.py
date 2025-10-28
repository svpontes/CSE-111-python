from EXAMPLE1 import read_list


def main():
    arquivo_province = read_list("provinces.txt")
     

def read_list(filename):

    linhas_do_texto = []
    

    with open(filename, "rt") as arquivo_de_texto:

        for linhas in arquivo_de_texto:

            limpa_linha = linhas.strip()

            linhas_do_texto.append(limpa_linha)
    
    linhas_do_texto.remove("Alberta")
    linhas_do_texto.pop()
    number_elements = len(linhas_do_texto)

    while "AB" in linhas_do_texto:

        linhas_do_texto.remove("AB")
    
    print(linhas_do_texto)
    print()
    print(f" The number of elements in the list is {number_elements}")
    print()
    return linhas_do_texto


if __name__ == "__main__":
    main()

