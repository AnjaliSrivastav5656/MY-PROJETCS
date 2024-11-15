"""
Quiz Application in Python
"""

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("Welcome to the Quiz!")
        for idx, (question, options, correct_option) in enumerate(self.questions):
            print(f"\nQuestion {idx + 1}: {question}")
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            try:
                answer = int(input("Enter your choice (1/2/3/4): "))
                if answer == correct_option:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer was: {options[correct_option - 1]}")
            except ValueError:
                print("Invalid input! Skipping this question.")

        print(f"\nQuiz Finished! Your score is {self.score}/{len(self.questions)}")

# Define questions as tuples: (question, [options], correct_option_index)
quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
    ("Which programming language is known as the 'Swiss Army Knife'?", ["Python", "C++", "Java", "Ruby"], 1),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"], 1),
    ("What is the smallest prime number?", ["0", "1", "2", "3"], 3)
]

# Create a Quiz instance and start the quiz
if __name__ == "__main__":
    quiz = Quiz(quiz_questions)
    quiz.start()
