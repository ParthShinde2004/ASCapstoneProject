"""This is a capstone project for AS Level Computer Science. The program will check your understanding on Stacks
& Queues (plus other topics) and add all the user's score to a separate file."""


# Class for questions so that the code is much more efficient and smaller
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# An array with all questions
question_prompts = [
    "Question 1", "Question 2", "Question 3"
]

# Used the class to make a array with the questions and answers
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]


# Main quiz function
def run_quiz(questions):
    name = str(input("What is your name?"))
    highscorefile = open("highscore.txt", "a")
    score = 0
    for question in questions: # Loops through all the questions
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    highscorefile.write("\n" + "Name: " + name + ", Score:" + str(score))
    print(score)


run_quiz(questions)
