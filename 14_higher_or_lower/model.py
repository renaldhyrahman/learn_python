from game_data import data as GAME_DATA
from dataclasses import dataclass
import random

# #######################################

@dataclass
class Player:
    score = 0

# #######################################

class Model:
    def __init__(self):
        self.player = Player()
        self.QUESTIONS = GAME_DATA.copy()
        self.MAX_SCORE = 20
        self.past_question = []
        self.current_question = []

    def is_used_question(self, question):
        """question: self.QUESTIONS[<randomize>],
        return: bool"""
        if not len(self.past_question): return False
        return True if question in self.past_question else False

    def create_question(self):
        """return: [question_1, question_2]"""
        question_1, question_2 = [None, None]
        while (question_1 == question_2
               or self.is_used_question(question_1)
               or self.is_used_question(question_2)):
            question_1 = random.choice(self.QUESTIONS)
            question_2 = random.choice(self.QUESTIONS)
        self.current_question = [question_1, question_2]
        self.past_question += [question_1, question_2]
        return self.current_question

    def reset(self):
        self.past_question = []
        self.player = Player()

    def check_answer(self, is_answer_a):
        """is_answer_a: bool,
        return bool"""
        question_1 = self.current_question[0]
        question_2 = self.current_question[1]
        is_a_correct = True if question_1["follower_count"] > question_2["follower_count"] else False
        if is_answer_a == is_a_correct:
            self.player.score += 1
            return True
        else: return False
