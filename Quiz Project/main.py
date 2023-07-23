from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
	qu_text = question["text"]
	qu_answer = question["answer"]
	new_question = Question(qu_text, qu_answer)
	question_bank.append(new_question)
	
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()
	
print(f"You have completed the quiz")
print(f"Your final score was : {quiz.score}/{quiz.question_number}.")
