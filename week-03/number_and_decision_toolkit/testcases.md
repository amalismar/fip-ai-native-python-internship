# Test Cases for the Toolkit

## ToolKit Menu

| Test ID | Test Description             | Input         | Expected Result                                            | Actual Result | Status |
| ------- | ---------------------------- | ------------- | ---------------------------------------------------------- | ------------- | ------ |
| TC01    | Display the main menu        | Run `main.py` | Four options are displayed                                 |               |        |
| TC02    | Select the calculator        | `1`           | Calculator opens                                           |               |        |
| TC03    | Select the converter         | `2`           | Unit converter opens                                       |               |        |
| TC04    | Select the decision checker  | `3`           | Decision checker opens                                     |               |        |
| TC05    | Select Exit                  | `4`           | Program exits with a thank-you message                     |               |        |
| TC06    | Enter an invalid menu choice | `9`           | Error message appears and the main menu is displayed again |               |        |

## Calculator

| Test ID | Test Description             | Input                               | Expected Result                                    | Actual Result | Status |
| ------- | ---------------------------- | ----------------------------------- | -------------------------------------------------- | ------------- | ------ |
| TC07    | Addition                     | Operation `1`, numbers `5` and `3`  | Result is `8`                                      |               |        |
| TC08    | Subtraction                  | Operation `2`, numbers `10` and `4` | Result is `6`                                      |               |        |
| TC09    | Multiplication               | Operation `3`, numbers `5` and `4`  | Result is `20`                                     |               |        |
| TC10    | Division                     | Operation `4`, numbers `10` and `2` | Result is `5`                                      |               |        |
| TC11    | Division by zero             | Operation `4`, numbers `10` and `0` | Error message says division by zero is not allowed |               |        |
| TC12    | Invalid calculator operation | Operation `7`                       | Error message asks the user to choose from 1 to 4  |               |        |
| TC13    | Invalid calculator number    | Enter `hello` for a number          | Error message asks the user to enter numbers only  |               |        |

## Unit Converter

| Test ID | Test Description               | Input      | Expected Result                               | Actual Result | Status |
| ------- | ------------------------------ | ---------- | --------------------------------------------- | ------------- | ------ |
| TC14    | Convert meters to feet         | `5` meters   | `5 meters = 16.4042 feet`                          |               |        |
| TC15    | Convert kilograms to pounds       | `45` kilograms | `45 kilograms = 99.2079 pounds`                        |               |        |
| TC16    | Convert Celcius to Fahrenheit    |`4` celcius     | `4.0` celcius = 39.2 Fahrenheit     |
| TC17    | Enter invalid measurement text | `hello`    | Error message asks the user to enter a number |               |        |

## Decision Checker

| Test ID | Test Description             | Input   | Expected Result                                     | Actual Result | Status |
| ------- | ---------------------------- | ------- | --------------------------------------------------- | ------------- | ------ |
| TC18    | Check even or odd | `8`     | `8` is even                         |               |        |
| TC19    | Check positive number  | `-3`    | Number is negative 
| TC20    | Check zero                   | `0`     | Number is zero                              |               |        |
| TC21    | Check negative  | `7`     | Number is positive                       |               |        |
| TC22    | Check for number greater than 10     | `95`   | number is  greater than 10 |               |        |
| TC23    | Enter invalid text           | `hello` | Error message asks the user to enter a whole number |               |        |

## Continue using the toolkit or Exit

| Test ID | Test Description                                | Input                                                                   | Expected Result                                       | Actual Result | Status |
| ------- | ----------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------- | ------------- | ------ |
| TC24    | Return to main menu after using a feature       | Enter `1` at the follow-up prompt                                       | Main menu appears again                               |               |        |
| TC25    | Exit after using a feature                      | Enter `2` at the follow-up prompt                                       | Program exits with a thank-you message                |               |        |
| TC26    | Enter an invalid follow-up choice               | Enter `9` at the follow-up prompt                                       | Error message appears and the prompt repeats          |               |        |
| TC27    | Return to main menu after invalid feature input | Enter invalid data in a feature, then enter `1` at the follow-up prompt | Main menu appears again                               |               |        |
| TC28    | Exit directly from the main menu                | Enter `4` at the main menu                                              | Program exits without displaying the follow-up prompt |               |        |

## 3. Testing Summary
* Total test cases: 28
* Passed: To be completed after testing
* Failed: To be completed after testing
* Pending: To be completed after testing

