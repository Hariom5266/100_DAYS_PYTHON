# 🍵 , Hanji Kaise ho aap sabhi this is 17th day of #100Days_Of_Python I'm back and ready to code.let's start to do code.

# ====================== Quiz Game ====================== #

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question['text']
    question_answer=question['answer']
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
    
# print(question_bank)
# print(question_bank[0].text) # A slug's blood is green

quiz=QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed Quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

# use open trivia database for generate question
    




