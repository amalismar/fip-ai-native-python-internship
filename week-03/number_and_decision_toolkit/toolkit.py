#Project 1

# Calculator function
def calculator():
    print("Welcome to Calculator!")
    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter your choice (1-4): ").strip()

    if operation not in ['1', '2', '3', '4']:
        print("Invalid choice. Please try again.")
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '1':
        result = num1 + num2
        print(f"The result of addition {num1} + {num2} is: {result}")

    elif operation == '2':
        result = num1 - num2
        print(f"The result of subtraction {num1} - {num2} is: {result}")

    elif operation == '3':
        result = num1 * num2
        print(f"The result of multiplication {num1} * {num2} is: {result}")

    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")


# Unit Converter function
def unit_converter():
    print("Welcome to Unit Converter!")
    print("Please select a conversion type:")
    print("1. Length (meters to feet)")
    print("2. Weight (kilograms to pounds)")
    print("3. Temperature (Celsius to Fahrenheit)")

    conversion_type = input("Enter your choice (1-3): ").strip()

    if conversion_type not in ['1', '2', '3']:
        print("Invalid choice. Please try again.")
        return

    value = float(input("Enter the value to convert: "))

    if conversion_type == '1':
        result = value * 3.28084
        print(f"{value} meters is equal to {result} feet.")

    elif conversion_type == '2':
        result = value * 2.20462
        print(f"{value} kilograms is equal to {result} pounds.")

    elif conversion_type == '3':
        result = (value * 9/5) + 32
        print(f"{value} Celsius is equal to {result} Fahrenheit.")


# Decision Checker function
def decision_checker():
    print("Welcome to Decision Checker!")
    print("Please select a decision type:")
    print("1. Even or Odd")
    print("2. Positive, negative or zero")
    print("3. Greater than 10")

    decision_type = input("Enter your choice (1-3): ").strip()

    if decision_type not in ['1', '2', '3']:
        print("Invalid choice. Please try again.")
        return

    try:
        number = int(input("Enter a number: "))

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    if decision_type == '1':
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")

    elif decision_type == '2':
        if number > 0:
            print(f"{number} is positive.")
        elif number < 0:
            print(f"{number} is negative.")
        else:
            print(f"{number} is zero.")

    elif decision_type == '3':
        if number > 10:
            print(f"{number} is greater than 10.")
        else:
            print(f"{number} is not greater than 10.")


# Next Step Function
def continue_or_end():
    print("Would you like to continue using the toolkit or exit?")
    print("1. Continue")
    print("2. Exit")

    while True:
        choice = input("Enter your choice (1-2): ").strip()

        if choice == '1':
            return True  # Continue using the toolkit
        elif choice == '2':
            print("Exiting the toolkit. Thank you for using it!")
            return False  # Exit the toolkit
        else:
            print("Invalid choice. Please try again. Select from 1 to 2.")

 # Main function to run the toolkit
def main():
    tools = [
        "Calculator",
        "Unit Converter",
        "Decision Checker",
        "Exit"
    ]

    
    while True:
        print("Welcome to Number and Decisions Toolkit!")

        for number in range(len(tools)):
                print(f"{number + 1}. {tools[number]}")  #displaying the tools with their corresponding numbers
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("Calculator selected.")
            calculator()

        elif choice == '2':
            print("Unit Converter selected.")
            unit_converter()

        elif choice == '3':
            print("Decision Checker selected.")
            decision_checker()
        
        elif choice == '4':
            print("Exiting the toolkit. Thank you for using it!")
            break

        else:
            print("Invalid choice. Please try again. Select from 1 to 4.")
            continue  # Skip the rest of the loop and prompt for input again

        if not continue_or_end():
            break  # Exit the main loop if the user chooses to exit

if __name__ == "__main__":   #makes sure the main function is called when the script is run directly
    main()