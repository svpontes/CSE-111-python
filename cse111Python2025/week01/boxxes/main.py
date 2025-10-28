from functions import calcItensPerBox

def main():
    #parameter for function calcItensPerBox
    num_of_items = int(input("Type the number of items: "))
    num_of_items_per_boxes = int(input("Type the number of boxes: "))

    #call or invoke the function
    result = calcItensPerBox(num_of_items, num_of_items_per_boxes)
    print(f"For {num_of_items} items, packing {num_of_items_per_boxes}, you will need {result} boxes.")

if __name__ == "__main__":
    main()