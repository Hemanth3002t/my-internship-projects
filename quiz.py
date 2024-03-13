# Define a list of dictionaries to store questions, options, and correct answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
        "answer": "A"
    }
]

# Function to display the questions and options, and get user input
def display_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    return user_answer

# Function to check the user's answer and update the score
def check_answer(question, user_answer, score):
    if user_answer == question["answer"]:
        print("Correct!")
        return score + 1
    else:
        print("Incorrect. The correct answer is:", question["answer"])
        return score

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        user_answer = display_question(question)
        score = check_answer(question, user_answer, score)
        print()  # Add a newline for better readability
    print("Quiz completed! Your final score is:", score)

# Main function to start the quiz
def main():
    print("Welcome to the Basic Quiz Game!")
    print("You will be asked a series of questions. Choose the correct answer from the options provided.")
    print("Let's begin!")
    print()
    run_quiz(questions)

if __name__ == "__main__":
    main()
