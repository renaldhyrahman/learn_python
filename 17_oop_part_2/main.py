from data import question_data, question_from_api
from quiz_brain import QuizBrain

def opentb_formatter(dict_data):
  """Return dict. Arg `json` from opentdb.com api"""
  result = []
  for data in dict_data['results']:
    result += [{
      'text': data['question'],
      'answer': data['correct_answer']
    }]
  return result

def app(data):
  quiz = QuizBrain(data)
  while quiz.still_has_question(): quiz.next_question()
  print("\nYou've completed the quiz.")
  print(f"Your final score: {quiz.score}/{quiz.question_number}")

# app(question_data)
app(opentb_formatter(question_from_api))

# Note:
# This app doesn't handle edge cases input such as: 't', 'f', etc
# Api for more question: opentdb.com/api_config.php
