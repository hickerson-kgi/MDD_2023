
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import random
from kivy.graphics import Color
from kivy.clock import Clock


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

    def __init__(self, **kwargs):
        self.selected_question = None  # Store the currently selected equation button
        self.selected_answer = None  # Store the currently selected solution button
        self.matching_colors = []  # Store random matching colors for button pairs

        super(MainWidget, self).__init__(**kwargs)
        self.questions, self.answers = generate_equation()
        answer_order = [0, 1, 2, 3]

        left_ids = ['1a_btn', '1b_btn', '1c_btn', '1d_btn']
        for i in range(len(left_ids)):
            self.ids[left_ids[i]].text = str(self.questions[i])
        right_ids = ['2a_btn', '2b_btn', '2c_btn', '2d_btn']
        random.shuffle(answer_order)
        for j in range(len(right_ids)):
            self.ids[right_ids[j]].text = str(self.answers[answer_order[j]])

    def generate(self, id):
        if id.startswith("1"):
            self.selected_question = id
        else:
            self.selected_answer = id

        self.matching_colors = [Color(random.random(), random.random(), random.random(), 1) for _ in
                                range(len(self.questions))]

        if self.questions.index(self.selected_question.text) == self.answers.index(self.selected_answer.text):
            matching_color_equation = self.matching_colors[self.questions.index(self.selected_question.text)]
            self.selected_equation.background_color = matching_color_equation.rgba
            matching_color_solution = self.matching_colors[self.answers.index(self.selected_answer.text)]
            self.selected_solution.background_color = matching_color_solution.rgba
            self.selected_equation = None
            self.selected_solution = None
        else:
            # Incorrect match
            self.selected_question.background_color = (1, 0, 0, 1)
            self.selected_answer.background_color = (1, 0, 0, 1)
            Clock.schedule_once(self.reset_colors, 1)  # Reset colors after 1 second

    def reset_colors(self, dt):
            self.selected_equation.background_color = (1, 1, 1, 1)
            self.selected_solution.background_color = (1, 1, 1, 1)
            self.selected_equation = None
            self.selected_solution = None

    def answer(self, id):
        self.ids[id].background_color = (1, 1, 1, 1)

    def restart_game(self):
        questions, answers = generate_equation()
        answer_order = [0, 1, 2, 3]

        left_ids = ['1a_btn', '1b_btn', '1c_btn', '1d_btn']
        for i in range(len(left_ids)):
            btn = self.ids[left_ids[i]]
            btn.text = str(questions[i])
            btn.background_color = (0.5, 0.5, 0.5, 1)

        right_ids = ['2a_btn', '2b_btn', '2c_btn', '2d_btn']
        random.shuffle(answer_order)
        for j in range(len(right_ids)):
            btn = self.ids[right_ids[j]]
            btn.text = str(answers[answer_order[j]])
            btn.background_color = (0.5, 0.5, 0.5, 1)

        MainWidget.prev_btn = None


class MindfulMatchup1App(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MindfulMatchup1App().run()
