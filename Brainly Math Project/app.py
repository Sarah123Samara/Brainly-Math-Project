print()
print("-" * 18)
print("WELCOME TO BRAINLY")
print("-" * 18)


def print_menu():
    menu_options = """
    
    \n--MENU--\n
    
    \r1)Even or Odd
    \r2)Prime or Not
    \r3)Calculator
    \r4)Quick Calculator
    \r5)Sequeces to a Specified Limit
    \r6)Square/Cube a Number
    \r7)Quit
    """
    print(menu_options)
    return [str(i) for i in range(1, 8)]


def menu():
    while True:
        options = print_menu()
        try:
            choice = input("what would you like to do? ").strip()
            if choice in options:
                return choice
            else:
                print("invalid input, enter a number from 1-7")
        except ValueError:
            print("invalid input, please enter an option from 1-7")


def even_or_odd():
    while True:
        try:
            user_input = input("enter a number (press enter to return to the menu): ")

            if not user_input:
                print("returning to the menu")
                return

            num = int(user_input)

            if num % 2 == 0:
                print(f"number {num} is an even number")
            elif num % 2 != 0:
                print(f"number {num} is an odd number")
            else:
                print("invalid input please enter a number")
        except ValueError:
            print("invalid input please enter a valid integer")


def is_prime():
    while True:
        try:
            user_input = input("Enter a number (press enter to return to the menu):")

            if not user_input:
                print("returning to the menu")
                return

            num = int(user_input)

            if num < 2:
                print(f"{num} is not a prime number")
                continue

            prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        except ValueError:
            print("Invalid input, please enter a number.")


def calculate():
    while True:
        try:
            user_input1 = input(
                "Enter the first number for the calculation (press enter to return to the menu): "
            )
            if not user_input1:
                print("returning to the menu")
                return

            user_input2 = input("Enter the second number for the calculation: ")

            num1 = int(user_input1)
            num2 = int(user_input2)

            adding_num = num1 + num2
            minusing_num = num1 - num2
            multiplying_num = num1 * num2
            dividing_num = num1 / num2

            print(f"\rAddition Result: {adding_num}")
            print(f"\rSubstraction Result: {minusing_num}")
            print(f"\rMultiplication Result: {multiplying_num}")
            print(f"\rDivision Result: {dividing_num}")
        except ValueError:
            print("invalid input, please enter valid numbers")


def quick_calculator_menu():
    menu_options = """
    
    \r1)Addition
    \r2)Substraction
    \r3)Multiplication
    \r4)Division
    
    """
    print(menu_options)
    return menu_options


def quick_calculator():
    while True:
        try:
            options = quick_calculator_menu()

            choice = input(
                "what would you like to do (press enter to return to the menu): "
            ).strip()
            if not choice:
                print("returning to the menu")
                return

            if choice == "1":
                add_num()
            elif choice == "2":
                substract_num()
            elif choice == "3":
                multiply_num()
            elif choice == "4":
                divide_num()
            else:
                print("invalid option, please enter a number from the above")
        except ValueError:
            print("invalid input please enter valid numbers")


def add_num():
    while True:
        try:
            user_input1 = input(
                "Enter the first number (press enter to return to the menu): "
            )

            if not user_input1:
                print("returning to the menu")
                return

            user_input2 = input("Enter the second number: ")

            num1 = float(user_input1)
            num2 = float(user_input2)

            adding_num = num1 + num2
            print(f"\rAddition Result: {adding_num}")
        except ValueError:
            print("invalid input, please enter valid numbers")


def substract_num():
    while True:
        try:
            user_input1 = input(
                "Enter the first number (press enter to return to the menu): "
            )

            if not user_input1:
                print("returning to the menu")
                return

            user_input2 = input("Enter the second number: ")

            num1 = float(user_input1)
            num2 = float(user_input2)

            minus_num = num1 - num2
            print(f"\rSubstraction Result: {minus_num}")
        except ValueError:
            print("invalid input, please enter valid numbers")


def multiply_num():
    while True:
        try:
            user_input1 = input(
                "Enter the first number (press enter to return to the menu): "
            )

            if not user_input1:
                print("returning to the menu")
                return

            user_input2 = input("Enter the second number: ")

            num1 = float(user_input1)
            num2 = float(user_input2)

            times_num = num1 * num2
            print(f"\rMultiplication Result: {times_num}")
        except ValueError:
            print("invalid input, please enter valid numbers")


def divide_num():
    while True:
        try:
            user_input1 = input(
                "Enter the first number (press enter to return to the menu): "
            )

            if not user_input1:
                print("returning to the menu")
                return

            user_input2 = input("Enter the second number: ")

            num1 = float(user_input1)
            num2 = float(user_input2)

            division_num = num1 / num2
            print(f"\rDivision Result: {division_num}")
        except ValueError:
            print("invalid input, please enter valid numbers")


def sequence_choosing_menu():
    menu_options = """
    
    \r1) Fibonacci Sequence
    \r2) Arithmatic Sequence
    \r3) Geometric Sequence
    """
    print(menu_options)
    return menu_options


def sequence_choosing():
    while True:
        try:
            options = sequence_choosing_menu()

            choice = input(
                "What would you like to do (press enter to return to the menu): "
            ).strip()
            if not choice:
                print("returning to the menu")
                return

            if choice == "1":
                fibonacci_sequence()
            elif choice == "2":
                arithmatic_sequence()
            elif choice == "3":
                geometric_sequence()
            else:
                print("Invalid input, please enter an option from the above.")

        except ValueError:
            print("Invalid input, please enter an option from the above.")


def fibonacci_sequence_math(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def fibonacci_sequence():
    while True:
        try:
            user_input1 = input(
                "Enter the limit for the Fibonacci Sequence (press enter to return to the menu):"
            )
            if not user_input1:
                print("Returning to the menu")
                return

            fib_limit = int(user_input1)

            if fib_limit < 2:
                print(
                    "Invalid input please enter a sequence limit that is greater than 1"
                )
                continue

            fib_sequence = fibonacci_sequence_math(fib_limit)
            print(f"Fibonacci Sequence: {fib_sequence}")

        except ValueError:
            print("Invalid input, please enter integers.")


def arithmatic_sequence_math(limit, common_diff):
    sequence = [0]
    while sequence[-1] + common_diff < limit:
        sequence.append(sequence[-1] + common_diff)
    return sequence


def arithmatic_sequence():
    while True:
        try:
            user_input1 = input(
                "Enter the limit for the Arithmatic Sequence (press enter to return to the menu):"
            )
            if not user_input1:
                print("Returning to the menu")
                return
            user_input2 = input("Enter the common difference for the sequence: ")

            ari_limit = int(user_input1)
            ari_diff = int(user_input2)

            if ari_limit < 2:
                print(
                    "Invalid input please enter a sequence limit that is greater than 1"
                )
                continue

            if ari_diff < 1:
                print(
                    "Invalid input, please enter a common difference that is greater than zero."
                )
                continue

            ari_sequence = arithmatic_sequence_math(ari_limit, ari_diff)
            print(f"Arithmatic Sequence: {ari_sequence}")

        except ValueError:
            print("Invalid input, please enter integers.")


def geometric_sequence_math(limit, ratio):
    sequence = [1]
    while sequence[-1] * ratio < limit:
        sequence.append(sequence[-1] * ratio)
    return sequence


def geometric_sequence():
    while True:
        try:
            user_input1 = input(
                "Enter the limit for the geometric sequence (press enter to return to the menu):"
            )
            if not user_input1:
                print("returning to the menu")
                return
            user_input2 = input("Enter the common ratio for the sequence:")

            geo_limit = int(user_input1)
            geo_ratio = int(user_input2)

            if geo_limit < 2:
                print(
                    "Invalid input please enter a sequence limit that is greater than 1"
                )
                continue

            if geo_ratio < 2:
                print(
                    "Invalid input please enter a common ratio that is greater than 1"
                )
                continue

            geo_sequence = geometric_sequence_math(geo_limit, geo_ratio)
            print(f"Geometric Sequence: {geo_sequence}")

        except ValueError:
            print("Invalid input, please enter integers.")


def square_cube_choosing_menu():

    menu_options = """
    
    \r1) Square a Number
    \r2) Cube a Number
    
    """
    print(menu_options)
    return menu_options


def square_cube_choosing():
    while True:
        try:

            options = square_cube_choosing_menu()

            user_input = input(
                "What would you like to do (press enter to return to the menu): "
            ).strip()

            if not user_input:
                print("Returning to the menu")
                return

            if user_input == "1":
                square_number()
            elif user_input == "2":
                cube_number()
            else:
                print("Invalid input, please enter an option from the above")

        except ValueError:
            print("Invalid input, please enter an option from the above")


def square_number_math(num):
    number = num * num
    return number


def square_number():
    while True:
        try:

            user_input = input(
                "Enter a number (press enter to return to the menu): "
            ).strip()

            if not user_input:
                print("Returning to the menu")
                return

            num_square = int(user_input)

            if num_square < 0:
                print("Invalid input please enter a positive integer")
                continue

            square = square_number_math(num_square)
            print(f"The square of {num_square} is {square}")

        except ValueError:
            print("Invalid input, please enter an integer")


def cube_number_math(num):
    number = num * num * num
    return number


def cube_number():
    while True:
        try:

            user_input = input(
                "Enter a number (press enter to return to the menu): "
            ).strip()

            if not user_input:
                print("Returning to the menu")
                return

            num_cube = int(user_input)

            if num_cube < 0:
                print("Invalid input please enter a positive integer")
                continue

            cube = cube_number_math(num_cube)
            print(f"The cube of {num_cube} is {cube}")

        except ValueError:
            print("Invalid input, please enter an integer")


def app():
    app_running = True
    while app_running:
        menu_choice = menu()

        if menu_choice == "1":
            even_or_odd()
        elif menu_choice == "2":
            is_prime()
        elif menu_choice == "3":
            calculate()
        elif menu_choice == "4":
            quick_calculator()

        elif menu_choice == "5":
            sequence_choosing()

        elif menu_choice == "6":
            square_cube_choosing()

        else:
            menu_choice = "7"
            print("\nThank You for using Brainly!\nHave a nice day\n")
            app_running = False


if __name__ == "__main__":
    app()
