POSITIVE = 1
NEGATIVE = -1 

def main():
    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:")
    print()
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement")
    print("A means you strongly agree with the statement.")
    print()
    """
    MINHA IDEIA INICIAL
    D = "strongly disagree"
    d = "desagree"
    a = "agree"
    A = "strongly agree"

    strongly_desagree = 0
    disagree = 1
    agree = 2
    strongly_agree = 3
    """
    question_score = 0
    question_score += question("1. I feel that I am a person of worth, at least on an equal plane with others.\n Enter D, d, a or A: ", POSITIVE )
    print()
    question_score += question("I feel that I have a number of good qualities.\nEnter D, d, a, or A: ", POSITIVE)
    print()
    question_score += question("3. All in all, I am inclined to feel that I am a failure.\nEnter D, d, a, or A: ", NEGATIVE)
    print()
    question_score += question("4. I am able to do things as well as most other people.\nEnter D, d, a, or A: ", POSITIVE)
    print()
    question_score += question("5. I feel I do not have much to be proud of.\nEnter D, d, a, or A: ", NEGATIVE)
    print()
    question_score += question("6. I take a positive attitude toward myself.\nEnter D, d, a, or A: ", POSITIVE)
    print()
    question_score += question("7. On the whole, I am satisfied with myself.\nEnter D, d, a, or A: ", POSITIVE)
    print()
    question_score += question("8. I wish I could have more respect for myself.\nEnter D, d, a, or A: ", NEGATIVE)
    print()
    question_score += question("9. I certainly feel useless at times.\nEnter D, d, a, or A: ", NEGATIVE)
    print()
    question_score += question("10. At times I think I am no good at all.\nEnter D, d, a, or A: ", NEGATIVE)
    print()
    print(f"Your score is {question_score}.")

    analisys_result = high_or_low_self_steem(question_score)
   

def high_or_low_self_steem(question_score):
    
    question_result = question_score

    if question_result > 15:
        print("Your self steem is high!. ")
    else:
        print("Your self steem is low!. ")
    return question_result

def question(statement, positive_or_negative):
    print(statement)
    answer = input("Enter D, d, a, or A: ")
    if answer == "D":
      question_score = 0
    elif answer == "d":
        question_score = 1
    elif answer == "a":
        question_score = 2
    elif answer == "A":
        question_score = 3
    if positive_or_negative == NEGATIVE:
        question_score = 3 - question_score
    return question_score

if __name__ == "__main__":
    main()

