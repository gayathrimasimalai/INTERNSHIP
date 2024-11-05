import random

# Function to display the game instructions
def show_instructions():
    print("""
--- Rock, Paper, Scissors Game ---
Choose one of the following:
1. Rock
2. Paper
3. Scissors
    """)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to play a round
def play_round():
    # Display instructions
    show_instructions()

    # Get the user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Validate the user's input
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Computer's random choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Display the choices
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")

    # Determine and display the result
    result = determine_winner(user_choice, computer_choice)
    print(result)

    return result

# Function to play multiple rounds with score tracking
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        # Play a round
        result = play_round()

        # Update scores based on the result
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        # Display the current scores
        print(f"\nCurrent Score: You - {user_score} | Computer - {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing! Final Score:")
            print(f"Final Score: You - {user_score} | Computer - {computer_score}")
            break

# Run the game
if __name__ == "__main__":
    play_game()
