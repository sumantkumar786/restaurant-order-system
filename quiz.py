print("**************")
print("WELCOME TO MY QUIZ GAME")

question_bank = [
    {"text": "Who developed the Python programming language?",
     "answer": "C"},
    {"text": "Which of the following is the correct extension for a standard Python script file?",
     "answer": "C"},
    {"text": "Which of the following data types is mutable in Python",
     "answer": "B"},
    {"text": "Which method is used to add an element to the very end of a list",
     "answer": "D"},
    {"text": "What is the correct arithmetic operator used for exponentiation (power) in Python",
     "answer": "B"}

]

options = [["A. Wick van Rossum", "B. Rasmus Lerdorf", "C. Guido van Rossum", "D. Niene Stom"],
           ["A. .python", "B. .pl", "C. .py", "D. .p"],
           ["A. String", "B. List", "C. Tuple", "D. Integer"],
           ["A. insert()", "B. add()", "C. push()", "D. append()"],
           ["A. ^", "B. **", "C. ^^", "D. *"]

]

score = 0

def check_answer(user_guess,correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False

for question_num in range(len(question_bank)):
    print("-----------------------")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess = input("Enter your answer").upper()
    is_correct = check_answer(guess,question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")
        print(f"The correct answer is {question_bank[question_num]["answer"]}")

print("Your final score is :" , score)

