# Using python as a calculator.
# Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following:
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division


status = False
while status == False:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    if num_1 >= num_2:
        try:
            print("Addition: ", (num_1 + num_2))
            print("Subtraction: ", num_1 - num_2)
            print("Division: ", num_1 / num_2)
            print("Division: ", num_1 * num_2)
            print("Exponent (Power): ", num_1 ** num_2)
            print("Modulus: ", num_1 % num_2)
            print("Floor division: ", num_1 // num_2)
            status = True
        except ZeroDivisionError:
            print("ZeroDivisionError,try again", )
    else:
        try:
            print("Addition: ", num_2 + num_1)
            print("Subtraction: ", num_2 - num_1)
            print("Division: ", num_2 / num_1)
            print("Division: ", num_2 * num_1)
            print("Exponent (Power): ", num_2 ** num_1)
            print("Modulus: ", num_2 % num_1)
            print("Floor division: ", num_2 // num_1)
            status = True
        except ZeroDivisionError:
            print('ZeroDivisionError,try again')





