def main():
    fruitlist = [
        "banana",
        "apple",
        "orange",
        "grape",
        "kiwi",
        "watermelon",
        "mango",
        "papaya",
        "guava",
        "pear"
    ]
    for fruit in fruitlist:
        print(fruit)
    
            
    for i in range(len(fruitlist)):
        fruitlist.append(i)
        print(fruitlist[i-1])

if __name__ == "__main__":
    main()

