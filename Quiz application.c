#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to show the quiz questions and calculate the score
void startQuiz() {
    int score = 0;
    char answer;
    
    printf("Welcome to the Quiz!\n\n");

    // Question 1
    printf("1. What is the capital of France?\n");
    printf("a) Paris\nb) London\nc) Berlin\nd) Rome\n");
    printf("Enter your answer (a/b/c/d): ");
    scanf(" %c", &answer);
    if (answer == 'a') {
        score++;
        printf("Correct!\n\n");
    } else {
        printf("Wrong! The correct answer is a) Paris\n\n");
    }

    // Question 2
    printf("2. Who wrote the Harry Potter series?\n");
    printf("a) J.K. Rowling\nb) J.R.R. Tolkien\nc) George R.R. Martin\nd) Agatha Christie\n");
    printf("Enter your answer (a/b/c/d): ");
    scanf(" %c", &answer);
    if (answer == 'a') {
        score++;
        printf("Correct!\n\n");
    } else {
        printf("Wrong! The correct answer is a) J.K. Rowling\n\n");
    }

    // Question 3
    printf("3. Which planet is known as the Red Planet?\n");
    printf("a) Earth\nb) Venus\nc) Mars\nd) Jupiter\n");
    printf("Enter your answer (a/b/c/d): ");
    scanf(" %c", &answer);
    if (answer == 'c') {
        score++;
        printf("Correct!\n\n");
    } else {
        printf("Wrong! The correct answer is c) Mars\n\n");
    }

    // Question 4
    printf("4. What is the largest mammal?\n");
    printf("a) Elephant\nb) Blue Whale\nc) Giraffe\nd) Polar Bear\n");
    printf("Enter your answer (a/b/c/d): ");
    scanf(" %c", &answer);
    if (answer == 'b') {
        score++;
        printf("Correct!\n\n");
    } else {
        printf("Wrong! The correct answer is b) Blue Whale\n\n");
    }

    // Question 5
    printf("5. Who painted the Mona Lisa?\n");
    printf("a) Leonardo da Vinci\nb) Pablo Picasso\nc) Vincent van Gogh\nd) Michelangelo\n");
    printf("Enter your answer (a/b/c/d): ");
    scanf(" %c", &answer);
    if (answer == 'a') {
        score++;
        printf("Correct!\n\n");
    } else {
        printf("Wrong! The correct answer is a) Leonardo da Vinci\n\n");
    }

    // Display final score
    printf("You scored %d out of 5.\n", score);
}

// Main function
int main() {
    int choice;

    // Main menu
    do {
        printf("===== Quiz Application =====\n");
        printf("1. Start Quiz\n");
        printf("2. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                startQuiz();
                break;
            case 2:
                printf("Thank you for playing!\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }

    } while (choice != 2);

    return 0;
}
