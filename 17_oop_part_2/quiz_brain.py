from question_model import Question


class QuizBrain:
    def __init__(self, databank):
        self.question_number = 0
        self.score = 0
        self.populate_list(databank)

    def populate_list(self, databank):
        """Void. Arg `databank` = [ {'text': '...', 'answer':
        'True'/'False'}, ... ]
        Create a new attr (`self.question_list` = []),
        then populate the new attr with `Question`,
        with arg text and answer from `databank`"""
        self.question_list = []
        for question in databank:
            self.question_list += [
                Question(question["text"], question["answer"])
            ]

    def still_has_question(self):
        """Return bool."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Return `string`, increase `self.number` by one.
        Return input with question that pulled from
        `self.question list` index `self.question_number`"""
        self.question_number += 1
        q_index = self.question_number - 1
        question = self.question_list[q_index]
        input_answer = (
            input(
                f"\nQ.{self.question_number}: {question.text} (True/False)?: "
            )
            .strip()
            .capitalize()
        )
        self.check_answer(input_answer, question.answer)
        print(f"Your current score: {self.score}/{self.question_number}")

    def check_answer(self, input_answer, q_answer):
        """Void. Increase `self.score` by one
        if arg `input_answer` == arg 'q_answer'"""
        if input_answer == q_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was: '{q_answer}'")
