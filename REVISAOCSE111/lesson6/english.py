import random

quantity = 1
tense= ""
word= ""
preposition = ""

def main():
    
    get_determiner(quantity)
    get_noun(quantity)
    #get_preposition(quantity)
      
def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
         words = ["two", "some", "many", "the"]
         
    word = random.choice(words) 
    
    cap_word = word.capitalize()

    return cap_word
       
    
    print(f"{cap_word}")
    print(f"The chosen word: {cap_word}")


#test result_determiner = get_determiner(quantity)

def get_noun(quantity):
  
    if quantity == 1:
       words = ["bird", "boy", "car", "cat", "child",
       "dog", "girl", "man", "rabbit", "woman"]
    
    else:

       words = ["birds", "boys", "cars", "cats", "children",
       "dogs", "girls", "men", "rabbits", "women"]
    
    word = random.choice(words)
    cap_word = word.capitalize()

    return cap_word
    
    print(f"the noun is {cap_word}")

#test result_noun = get_noun(quantity)

def get_verb(tense, quantity):
    
    if tense == "past" and quantity == 1:
        verbs =["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    
    if tense == "present" and quantity != 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks","rusn", "sleeps", "talks", "walks", "writes"]
    
    else:
        tense =="future"
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
        verb = random.choice(verbs)
        
    return verb

"""def get_preposition(quantity):
    if quantity == 1:
        prepositions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except"]
    else:
        prepositions = ["for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    preposition = random.choice(prepositions)
    return preposition

def get_preposition_phrase(quantity):
    
    result_preposition = get_preposition
    result_determiner = get_determiner
    result_noun = get_noun"""



if __name__ == "__main__":
    main()