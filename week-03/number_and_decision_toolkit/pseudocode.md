# Main Toolkit
START

- Create a list that contains the four number and decesions toolkit functions

REPEAT
- Display the Welcome message
- Display the menu options
- Ask user to select a choice in the options

IF the choice is 1
- Open Calculator

ELSE IF the choice is 2
- Open Unit Converter

ELSE IF the choice is 3
- Open Decision Maker

ELSE IF the choice is 4:
- Display exit message
- Exit the loop

Else
- Display invalid choice message

# CALCULATOR
START
- Display the four operations
- Ask user to select one of them

IF the operation is invalid
- Display an error message
- Ask if to return to toolkit or exit

ELSE;
- Ask for two numbers
- Convert the inputs to integers

IF the inputs are invaid:
- Display an error message
- Return to toolkit

IF addition is selected:
- Add the two numbers

ELSE IF subtraction is selected:
- Subtract the second from the first

ELSE IF multiplication is selected:
- Multiply the two numbers

ELSE IF division is selected:
- IF the second number is zero:
    - Display error
- ELSE 
    - Divide the first number by the second

- Display the result after calculation
END CALCULATOR

# Unit Converter
START UNIT CONVERTER
- Display the three conversion types
- Ask user to select one

IF the conversion type is invalid
- Display an error message
- Ask to return to toolkit or exit

ELSE 
- Ask user to input the value to convert

IF choice is 1
- Convert their input value from meters to feet

ELSE IF choice is 2
- Convert their input value from kilograms to pounds

ELSE IF choice is 3
- Convert their input value from celcius to fahrenheit

- Display results after conversion
END UNIT CONVERTER

# DECISION CHECKER
START DECISION CHECKER
- Display three decion types
- Ask user to select a choice

IF the decision checker choice is invalid
- Display an error message
- Ask to return to toolkit or exit

IF choice is 1:
- Ask user to enter a number
- Display the answer
- Ask to continue or exit toolkit

ELSE IF choice is 2
- Ask user to enter a number
- Display the answer
- Ask to continue or exit toolkit

ELSE IF choice is 3
- Ask user to enter a number
- Display the answer
- Ask to continue or exit toolkit

END DECISION CHECKER
