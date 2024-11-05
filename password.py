import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    # Define character sets for the password
    lower_case = string.ascii_lowercase  # a-z
    upper_case = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    special_characters = string.punctuation  # special symbols like !@#$%^&*

    # Create the base character pool
    char_pool = lower_case + upper_case + digits + special_characters

    # If complexity is 'low', exclude special characters
    if complexity == 'low':
        char_pool = lower_case + upper_case + digits
    # If complexity is 'medium', include only some special characters
    elif complexity == 'medium':
        char_pool = lower_case + upper_case + digits + "!@#$%^&*"

    # Generate a random password by selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Function to display the menu and get user input
def run_password_generator():
    print("--- Password Generator ---")

    # Prompt the user for the desired password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
            print("Password length should be at least 8 characters for security reasons.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Prompt the user for the desired complexity
    complexity = input("Enter complexity (low/medium/high): ").lower()
    if complexity not in ['low', 'medium', 'high']:
        print("Invalid complexity. Please choose from 'low', 'medium', or 'high'.")
        return

    # Generate the password based on the input
    password = generate_password(length, complexity)

    # Display the generated password
    print(f"\nYour generated password is: {password}")

# Run the program
if __name__ == "__main__":
    run_password_generator()
