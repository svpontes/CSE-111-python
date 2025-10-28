import random

quantity = 1
"""
def get_determiner():
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
         words = ["two", "some", "many", "the"]

    word = random.choice(words) 
    cap_word = word.capitalize()
    return cap_word
    
    print(f"{cap_word}")"""

def get_noun():
    if quantity == 1:
       words = ["bird", "boy", "car", "cat", "child",
       "dog", "girl", "man", "rabbit", "woman"]
    
    else:

       words = ["birds", "boys", "cars", "cats", "children",
       "dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)
    cap_word = word.capitalize()

    
    
    print(f"the noun is {cap_word}")
get_noun()