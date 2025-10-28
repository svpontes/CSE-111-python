"""def main():
    colors =["red", "orange", "yellow", "green", "blue"]
    for color in colors:
        print(color)

    colors.insert(0, "white")
    print(colors)

    i = colors.index("yellow")
    colors[i] = "black"

    print(colors)"""""
    

def main():
        
    apple_tree_data = [
    [2012, 2.7, 3.6, 70.5],
    [2012, 2.4, 3.7, 81.3],
    [2015, 2.3, 3.6, 62.7],
    [2016, 2.1, 2.7, 42.1]
    ]
    
    year_planted_index = 0

    height_index = 1

    girth_index = 2

    fruit_amount_index = 3
    
    #devolve uma lista interna da LISTA COMPOSTA
    control_tree_number_one = apple_tree_data[2]
    
    #devolve um VALOR da LISTA INTERNA
    height = control_tree_number_one[height_index]

    print(height)
    print(control_tree_number_one)
    print(height_index)

if __name__ == "__main__":
    main()

