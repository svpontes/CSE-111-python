"""
A common task for many knowledge workers is to use a number, key,
or ID to look up information about a person. For example, a
knowledge worker may use a phone number or e-mail address as a key
to find (or look up) additional information about a customer.
During this activity, your team will write a Python program that
uses a student's I-Number to look up the student's name.
"""
import csv


def main():
    # The column headings and indexes.
    I_NUMBER = 0
    NAME = 1

    students = read_dict("students.csv", I_NUMBER)
  
    inumber = str(input("Please enter an I-Number (xx-xxx-xxxx): "))
   
    inumber = inumber.replace("-", "")

   
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            # Esse Else corresponde ao I-number correto, assim ele encontra o numero digitado pelo usuario na lista de I-numbers.
            if inumber not in students:
                print("No such student")
            else:
                # Retorna o nome do estudante que corresponde ao nome que o usuário digitou ni I-number input
                value = students[inumber]
                name = value[NAME]

                # Print the student name.
                print(name)


def read_dict(filename, key_column_index):
    """Lê o conteudo do e retorna um dicionario.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains the contents of the CSV file.
    """
    # cria um dicionario vazio
    # armazena dos dados do arquivo csv
    dictionary = {}

    # Abre o arquivo csv para leitura e Open a CSV file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(text_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in reader:

            # From the current row, retrieve
            # the column that contains the key.
            key = row[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row

    # Return the dictionary.
    return dictionary


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()