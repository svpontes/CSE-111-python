"""
A paradigm is a way of thinking or a way of viewing the world

procedural
declarative
functional
object-oriented
PROCEDURAL example 1
"""

def main():
    number=[87, 95, 72, 92, 95, 88, 84]
    total = 0
    for x in number:
        total+= x
        average = total /len(number)
    print(F"the average : {average:.2f}")

if __name__ == "__main__":
    main()


