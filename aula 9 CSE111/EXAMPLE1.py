# Example 1
"""
def main():
    # 
    #variavel = função           abre
    #           read_list (arquivo de texto)
    text_list = read_list("plants.txt")

    # Print a lsita toda
    print(text_list)


def read_list(filename):
    A função read_list lê o conteudo de um arquivo de texto e em uma lista e retorna a lista

    parâmetro (filename) : representa o arquivo de texto a ser abreto e lido
    
    Retorna: uma lista de strings
    
    #variávia text_list = [] lista vazia. Objetivo é colocar os itens do arquivo de texto nesta variavel
    text_list = []

    # with open file (filename, "rt) abre o arquivo de texto e no modo de leitura e armazena as referencias na variável text_file[]

    with open(filename, "rt") as text_file:

        # Lê o conteudo do texto
        # arquiva uma linha por vez.
        for line in text_file:

            # criamos a variavel clean_line parapara eliminar espacos vazios no começo e fim do texto com o método strip().
            clean_line = line.strip()

            # acrescentamos a linha do texto so final da lista com o método append(variavel clean_line).
            text_list.append(clean_line)

    # retorna a lista que contem as linhs do texto

if __name__ == "__main__":
    main()"""
# Example 1

def main():
    # Read the contents of a text file
    # named plants.txt into a list.
    text_list = read_list("plants.txt")

    # Print the entire list.
    print(text_list)


def read_list(filename):
    """Read the contents of a text file into a list and
    return the list. Each element in the list will contain
    one line of text from the text file.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    # Create an empty list named text_list.
    text_list = []

    # Open the text file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time. loop
        for line in text_file:

            # Remove white space, if there is any,
            # from the beginning and end of the line.
            clean_line = line.strip()

            # Append the clean line of text
            # onto the end of the list.
            text_list.append(clean_line)

    # Return the list that contains the lines of text.
    return text_list


# Call main to start this program.
if __name__ == "__main__":
    main()