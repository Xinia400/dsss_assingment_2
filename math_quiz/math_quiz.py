import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer between min_value and max_value
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generate a random operator (+, -, *)
    """
    return random.choice(['+', '-', '*'])

def calculate_result(num1, num2, operator):
    """
    Calculate the result based on num1, num2, and the operator
    """
    expression = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return expression, result

def get_user_answer():
    """
    Get user input for the answer
    """
    while True:
        try:
            user_input = input("Your answer: ")
            user_answer = int(user_input)
            return user_answer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def math_quiz():
    score = 0
    total_questions = 8

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)
        operator = generate_random_operator()

        problem, answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        user_answer = get_user_answer()

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "_main_":
    math_quiz()
