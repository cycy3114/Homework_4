import sys
from calculator import add  # import other functions if needed

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
        sys.exit(1)

    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        operation = sys.argv[3].lower()

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            from calculator.calculation import subtract
            result = subtract(a, b)
        elif operation == "multiply":
            from calculator.calculation import multiply
            result = multiply(a, b)
        elif operation == "divide":
            from calculator.calculation import divide
            result = divide(a, b)
        else:
            print("Invalid operation. Choose from: add, subtract, multiply, divide.")
            sys.exit(1)

        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid number.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
