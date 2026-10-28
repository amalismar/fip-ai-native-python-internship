"""Main entry point for the application."""
    #This module serves as the main entry point for the application. It imports and utilizes various utility functions from the utility_package to perform tasks such as age calculation, basic arithmetic operations, and password validation and generation.

from utility_package import (
    calculate_age, 
    add,
    subtract, 
    multiply, 
    divide, 
    check_password_strength, 
    generate_random_password)

def main():
    """Main function to demonstrate the utility functions."""

    print("Welcome to the Utility Functions Demonstration!")
    print("--------------------------------------------------")

    print("\n1. BASIC CALCULATOR :")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))

    print("\n2. PASSWORD VALIDATION AND GENERATION :")
    print("Password Strength Check for 'Password123!':", check_password_strength("Password123!"))
    print("Generated Random Password of length 12:", generate_random_password(12))

    print("\n3. AGE CALCULATION :")
    print("Age for birth date 1990-01-01:", calculate_age(1990, 1, 1))

if __name__ == "__main__":     #this condition checks if the script is being run directly (not imported as a module) and calls the main function to execute the demonstration of utility functions.
    main()