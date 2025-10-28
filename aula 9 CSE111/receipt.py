import csv
#creat an empty list of components groceries

# open the list of products

def main():
    i_product = 0
    name = 1
    price = 2

    products = read_products("products.csv", i_product)

    print(products)

def read_products(filename, key_column_index):

    dictionary = {}

    with open(filename, "rt") as csv_products_file:

        reader = csv.reader(csv_products_file)

        next(reader)

    for row in reader:

        key = row[key_column_index]
        dictionary[key] = row
    
    return dictionary    
       

if __name__ == "__main__":
    main()