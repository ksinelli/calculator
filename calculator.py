import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def select_operation():
    print("+")
    print("-")
    print("*")
    print("/")
    return input("Pick an operation: ")

def get_first_number():
    return float(input("What's the first number?: "))

def get_second_number():
    return float(input("What's the next number?: "))

def perform_calculation(n1, n2, symbol):
    if symbol == "+":
        return add(n1, n2)
    elif symbol == "-":
        return subtract(n1, n2)
    elif symbol == "*":
        return multiply(n1, n2)
    elif symbol == "/":
        if n2 == 0:
            print("Cannot divide by zero.")
            start_program()
        return divide(n1, n2)

def print_result(n1, n2, symbol, n3):
    print(f"{n1} {symbol} {n2} = {n3}")

def start_program():
    first_number = get_first_number()
    continue_program(first_number)

def continue_program(number_one):
    operation = select_operation()

    number_two = get_second_number()

    result = perform_calculation(number_one, number_two, operation)

    print_result(number_one, number_two, operation, result)

    choose_whether_to_continue(result)

def choose_whether_to_continue(previous_result):
    should_continue = input(
        f"Type 'y' to continue calculating with {previous_result}, or type 'n' to start a new calculation: ").lower()
    if should_continue == 'n':
        start_program()
    elif should_continue == 'y':
        continue_program(previous_result)

start_program()