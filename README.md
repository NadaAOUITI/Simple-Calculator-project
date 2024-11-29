# Simple-Calculator-project
Python
Advanced Python Calculator
Overview
This project is an implementation of a calculator in Python. It offers two modes of calculation: direct calculation and guided calculation. The calculator supports the basic arithmetic operations: addition, subtraction, multiplication, and division. The program is robust, handling invalid inputs and zero-division errors with clear, user-friendly messages.

Features
Direct Calculation Mode: Users can input a simple arithmetic expression (e.g., 2+2), and the program will compute the result.
Guided Calculation Mode: Users input numbers and the operator separately, and the program computes the result.
Error Handling: The program handles invalid input types, unsupported operators, and zero-division errors gracefully.
Key Functions
calculator(x, sign, y)
This function takes two numbers (x, y) and an operator (sign), performing the appropriate operation:

Addition: +
Subtraction: -
Multiplication: *
Division: / (with zero-division handling)
Error Handling:

ValueError for invalid operators.
ZeroDivisionError for attempts to divide by zero.
calculdirect()
In this mode, the program processes a single-line operation, extracting the operands and operator to perform the calculation. It handles user input errors and formats them accordingly.

main()
The main entry point for the program, providing the user with an interactive menu for either direct calculation or guided calculation. The program loops until the user opts to exit.
