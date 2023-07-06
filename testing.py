
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
###Added Code
from kivy.clock import Clock
import random


def generate_equation():
    questions = []
    answers = []
    for _ in range(4):
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        equation = f"{num1} {operator} {num2}"
        evaluate = eval(equation)
        result = round(evaluate, 3)
        questions.append(equation)
        answers.append(result)

    return questions, answers


class MainWidget(GridLayout):
    prev_btn = None  # Initialize prev_btn with None
    ###ADdedCode- initalize game duration to 0
    game_duration = 0
    game_timer = None

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        questions, answers = generate_equation()
        answer_order = [0, 1, 2, 3]

        left_ids = ['a1_btn', 'b1_btn', 'c1_btn', 'd1_btn']
        for i in range(len(left_ids)):
            self.ids[left_ids[i]].text = str(questions[i])
        right_ids = ['a2_btn', 'b2_btn', 'c2_btn', 'd2_btn']
        random.shuffle(answer_order)
        for j in range(len(right_ids)):
            self.ids[right_ids[j]].text = str(answers[answer_order[j]])
        ###AddedCode- Start the game timer
        Clock.schedule_interval(self.update_timer, 1)
    ###Added Code
    def on_start(self):
        # Start the game timer
        self.game_timer = Clock.schedule_interval(self.update_timer, 1)
    ###Added Code
    def on_stop(self):
        # Stop the game timer
        self.game_timer.cancel()
    ###Added Code
    def update_timer(self, dt):
        self.game_duration += 1

    def generate(self, id):
        btn = self.ids[id]
        btn_text = btn.text
        if MainWidget.prev_btn is not None:
            prev_btn = MainWidget.prev_btn
            prev_btn_index = list(self.ids.values()).index(prev_btn)
            btn_index = list(self.ids.values()).index(btn)
            if prev_btn_index == btn_index:
                prev_btn.background_color = (0, 1, 0.5, 1)
                btn.background_color = (0, 1, 0.5, 1)
        MainWidget.prev_btn = btn
        # AddedCode Display the game duration after button push
        print("Game Duration:", self.game_duration)

    def answer(self, id):
        self.ids[id].background_color = (1, 1, 1, 1)

    def restart_game(self):
        # Reset the game state here
        questions, answers = generate_equation()
        answer_order = [0, 1, 2, 3]

        left_ids = ['a1_btn', 'b1_btn', 'c1_btn', 'd1_btn']
        for i in range(len(left_ids)):
            self.ids[left_ids[i]].text = str(questions[i])
        right_ids = ['a2_btn', 'b2_btn', 'c2_btn', 'd2_btn']
        random.shuffle(answer_order)
        for j in range(len(right_ids)):
            self.ids[right_ids[j]].text = str(answers[answer_order[j]])

class MindfulMatchup1App(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MindfulMatchup1App().run()
