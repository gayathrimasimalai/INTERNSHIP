# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to display the menu
def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main function to run the calculator
def run_calculator():
    while True:
        show_menu()
        
        # Take user input for operation
        choice = input("Enter choice (1/2/3/4/5): ")
        
        # Check if user wants to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        # Check if the user selected a valid operation
        if choice in ['1', '2', '3', '4']:
            try:
                # Take user input for two numbers
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                # Perform the operation based on user choice
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                
                # Display the result
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select a valid option from the menu.")
        
# Run the calculator
if __name__ == "__main__":
    run_calculator()
