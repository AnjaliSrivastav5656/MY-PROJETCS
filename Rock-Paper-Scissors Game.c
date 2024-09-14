#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to get computer's choice
int getComputerChoice() {
    return rand() % 3; // Returns 0, 1, or 2
}

// Function to get the choice name
const char* getChoiceName(int choice) {
    switch (choice) {
        case 0: return "Rock";
        case 1: return "Paper";
        case 2: return "Scissors";
        default: return "Unknown";
    }
}

// Function to determine the winner
const char* determineWinner(int userChoice, int computerChoice) {
    if (userChoice == computerChoice) {
        return "It's a tie!";
    }
    if ((userChoice == 0 && computerChoice == 2) || // Rock beats Scissors
        (userChoice == 1 && computerChoice == 0) || // Paper beats Rock
        (userChoice == 2 && computerChoice == 1)) { // Scissors beats Paper
        return "You win!";
    }
    return "Computer wins!";
}

// Main function
int main() {
    int userChoice, computerChoice;
    srand(time(NULL)); // Seed for random number generation

    printf("Rock-Paper-Scissors Game\n");
    printf("Enter your choice:\n");
    printf("0 - Rock\n");
    printf("1 - Paper\n");
    printf("2 - Scissors\n");
    printf("Your choice: ");
    scanf("%d", &userChoice);

    // Validate user choice
    if (userChoice < 0 || userChoice > 2) {
        printf("Invalid choice! Please enter 0, 1, or 2.\n");
        return 1;
    }

    // Get computer's choice
    computerChoice = getComputerChoice();

    // Display choices
    printf("You chose: %s\n", getChoiceName(userChoice));
    printf("Computer chose: %s\n", getChoiceName(computerChoice));

    // Determine and display the winner
    printf("%s\n", determineWinner(userChoice, computerChoice));

    return 0;
}
