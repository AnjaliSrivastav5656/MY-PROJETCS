import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors Game!")
    print("Choose one: Rock, Paper, or Scissors")
    
    # Choices for the game
    choices = ["Rock", "Paper", "Scissors"]
    
    # Get player's choice
    player_choice = input("Your choice: ").capitalize()
    if player_choice not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        return

    # Get computer's random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()
