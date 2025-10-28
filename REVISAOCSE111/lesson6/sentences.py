import random

# Write a Python program that generates simple English sentences. During this lesson, you will write and test functions that generate sentences with three parts:

# a determiner (sometimes known as an article)
# a noun
# a verb
words = ["boy", "girl", "cat", "dog", "bird", "house"]
word = random.choice(words)
cap_word = word.capitalize()
tenses = ["past", "present", "future"]


tenses = ["past", "present", "future"]
quantity = 1
def main():

    determiner = get_determiner(quantity)
    print(determiner)

    noun = get_noun(quantity)
    print(noun)
    
    verb = get_verb(quantity, tenses)
    print(verb)

    print()

    print(f"{determiner} {noun} {verb}")

def get_determiner(quantity):#Return a randomly chosen determiner like (the , a , one two, some many).
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]
    
    word = random.choice(words)
    
    return word


def get_noun(quantity):

    if quantity == 1:  #will return single nouns
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    else: #will return plural nouns
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    
    for tense in tenses:

        if tense == "past":
            words = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
        
        if tense == "present" and quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
        if tense == "present" and quantity != 1:
            words = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
        if tense == "future":
            words = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"] 
    
    word = random.choice(words)
    return word
    
if __name__ == "__main__":
    main()