# Class for questions so that the code is much more efficient and smaller
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# An array with all questions (Add more questions if you want)
question_prompts = [
    "What is a stack?\nA - It follows a FILO methodology\nB - It follows a FIFO methodology\nC - It follows a FIFA methodology\nD - It doesn't follow Methodology",  
    "What is a queue?\nA - It follows a FILO methodology\nB - It follows a FIFO methodology\nC - It follows a FIFA methodology\nD - It doesn't Methodology", 
    "What does the pop() function do?\nA - This increments the stacknum by 1\nB - this decrements the stack num by 1\nC - This takes the element that is next to come out, out\nD - This takes out all the addresses",
    "What does the push() function do?\nA - This put an address into the storage method\nB - This puts 10 addresses in\nC - The ACU is incremented by 1\nD - The ACU is decremented by 1",
]

# Used the methods from the class to make a array with the questions and answers
questions = [
    Question(question_prompts[0], "A"), # Make sure to add answers if you have added new questions
    Question(question_prompts[1], "B"),
    Question(question_prompts[2], "C"),
    Question(question_prompts[3], "A")
]


# Main quiz function
def run_quiz(questions):
    name = str(input("What is your name?"))
    highscorefile = open("highscore.txt", "a")
    score = 0
    for question in questions: # Loops through all the questions
        answer = input(question.prompt)
        if answer.upper() == question.answer:
            score += 1
    highscorefile.write("\n" + "Name: " + name + ", Score:" + str(score) + "/" + str(len(questions)))
    highscorefile.close()
    print(score)

run_quiz(questions)