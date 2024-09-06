
def main():
    while True:
        # Input numbers and operator
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        operator = input("Enter the operator (+, -, *, /): ").strip()

        # Perform the operation
        if operator == '+':
            result = add.add(num1, num2)
        elif operator == '-':
            result = subtract.subtract(num1, num2)
        elif operator == '*':
            result = multiply.multiply(num1, num2)
        elif operator == '/':
            result = divide.divide(num1, num2)
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")
            continue

        # Display the result
        print(f"The result is: {result}")

        # Ask if the user wants to quit
        quit_choice = input("Do you want to quit? (Y for yes, N for no): ").strip().upper()
        if quit_choice == 'Y':
            print("Thank you for using the calculator. Goodbye!")
            break
        elif quit_choice == 'N':
            continue
        else:
            print("Invalid choice. Assuming 'N' for no.")
            continue


if __name__ == "__main__":
    main()
