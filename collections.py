

def main():
    
    apple_tree_data = [
        [2012, 2.7, 6.6, 70.5], #onde: 2012 year_planted/ 2.7 height/ 3.6 girth / 70.5 fruit_amount
        [2012, 2.4, 3.7, 81.3],
        [2015, 2.3, 3.6, 62.7],
        [2016, 2.1, 2.7, 42.1]
    ]
    
    year_planted_index = 0
    height_index = 1
    girth_index = 2
    fruit_amount_index = 3

    one_tree = apple_tree_data[2]

    height = one_tree[height_index]

    print (f"Heigth : {height}")


if __name__ == "__main__":
    main()
