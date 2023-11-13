import random

def choose_integer(min, max):
    """
    Random integer selection between the range defined by minimum and maximum value
    """
    return random.randint(min, max)


def choose_operator():
    """
    Random operator among the three choices 
    """
    return random.choice(['+', '-', '*'])


def calculation(number_1,number_2,operator):
    """
    Function to calculate result based on operator and integer
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+':
        result= number_1 + number_2
    elif operator == '-':
         result= number_1 - number_2
    else:
        result= number_1 * number_2
    return problem,result

def math_quiz():
    sum = 0
    count = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    """
    Loop to play game 3 times
    """
    for i in range(int(count)):
        number_1= choose_integer(1, 10)
        number_2= choose_integer(1, 5)
        operator = choose_operator()

        PROBLEM, ANSWER =calculation(number_1, number_2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)
        # Condition to check if the user answer is correct, as calculated by the program

        if not type(useranswer) is int:   
            raise TypeError("Only integers allowed")
        else:
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                sum += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        

    print(f"\nGame over! Your score is: {sum}/{int(count)56}")

if __name__ == "__main__":
    math_quiz()
