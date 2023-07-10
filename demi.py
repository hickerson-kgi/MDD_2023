from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import random
from kivy.graphics import Color
from kivy.clock import Clock

# Function to generate random arithmetic equations
def generate_equation():

    questions = []
    answers = []
    unique_results = set()  # Keep track of unique results

    while len(questions) < 4:
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        equation = f"{num1} {operator} {num2}"
        evaluate = eval(equation)
        result = round(evaluate, 3)

        if result not in unique_results:
            unique_results.add(result)
            questions.append(equation)
            answers.append(result)

    return questions, answers


# MainCode represents the main code of the application
class MainCode(GridLayout):

    def __init__(self, **kwargs):

        super(MainCode, self).__init__(**kwargs)
        self.questions, self.answers = generate_equation()

        self.matching_colors = [(1, 0, 0.5, 1), (1, 1, 0, 1), (0, 0, 1, 1), (0, 1, 0, 1)]  # Store random matching colors for button pairs
        self.matches = 0

        self.left_ids = ['0q_btn', '1q_btn', '2q_btn', '3q_btn']
        for i in range(len(self.left_ids)):
            self.ids[self.left_ids[i]].text = str(self.questions[i])

        self.right_ids = ['0a_btn', '1a_btn', '2a_btn', '3a_btn']
        self.answer_order = [0, 1, 2, 3]
        random.shuffle(self.answer_order)
        for j in range(len(self.right_ids)):
            self.ids[self.right_ids[j]].text = str(self.answers[self.answer_order[j]])

        for k in self.left_ids:
            self.ids[k].background_color = (0.5, 0.5, 0.5, 1)

        for l in self.right_ids:
            self.ids[l].background_color = (0.5, 0.5, 0.5, 1)

        self.selected_question = False
        self.selected_answer = False

    # Function to handle button click events
    def generate(self, id):
        # indicates left side, i.e. question
        if id[1] == 'q':

            # Unhighlights previous question if a new question is selected
            if self.selected_question != False:
                if self.ids[self.selected_question].background_color == [0.9, 0.9, 0.9, 1]:
                    self.ids[self.selected_question].background_color = (0.5, 0.5, 0.5, 1)

            self.selected_question = id

            # highlight selected answer if it is not matched yet
            if self.ids[id].background_color == [0.5, 0.5, 0.5, 1]:
                self.ids[id].background_color = (0.9, 0.9, 0.9, 1)

        # indicates right side, i.e. answer
        if id[1] == 'a':

            # Unhighlights previous answer if a new answer is selected
            if self.selected_answer != False:
                if self.ids[str(self.selected_answer[0]) + 'a_btn'].background_color == [0.9, 0.9, 0.9, 1]:
                    self.ids[str(self.selected_answer[0]) + 'a_btn'].background_color = (0.5, 0.5, 0.5, 1)

            self.selected_answer = id

            # highlight selected answer if it is not matched yet
            if self.ids[id].background_color == [0.5, 0.5, 0.5, 1]:
                self.ids[id].background_color = (0.9, 0.9, 0.9, 1)

        # if there are now two selections, question and answer
        if (self.selected_question != False) and (self.selected_answer != False):

            q_index = int(self.selected_question[0])
            a_button = int(self.selected_answer[0])
            a_index = self.answer_order[a_button]

            # Determine if the selected question and answer are both matched already
            self.colored = False

            for i in range(len(self.matching_colors)):
                if tuple(self.ids[str(q_index) + 'q_btn'].background_color) == self.matching_colors[i]:
                    self.colored = True
                if tuple(self.ids[str(a_button) + 'a_btn'].background_color) == self.matching_colors[i]:
                    self.colored = True

            # only change color of buttons that have not been matched already
            if self.colored == False:

                # Deterimine if the question and answer are a matching pair
                if q_index == a_index:
                    # change BOTH buttons to color
                    current_color = self.matching_colors[self.matches]
                    self.ids[str(q_index) + 'q_btn'].background_color = current_color  # question button
                    self.ids[str(a_button) + 'a_btn'].background_color = current_color  # answer button

                    self.matches += 1
                    self.matches = self.matches % 4

                else:
                    self.ids[str(q_index) + 'q_btn'].background_color = (0.5, 0.5, 0.5, 1)
                    self.ids[str(a_button) + 'a_btn'].background_color = (0.5, 0.5, 0.5, 1)
                    self.selected_question = False
                    self.selected_answer = False

            self.selected_question = False
            self.selected_answer = False

    def restart_game(self):
        questions, answers = generate_equation()
        self.answer_order = [0, 1, 2, 3]

        self.selected_question = False
        self.selected_answer = False
        self.matches = 0

        for i in range(len(self.left_ids)):
            btn = self.ids[self.left_ids[i]]
            btn.text = str(questions[i])
            btn.background_color = (0.5, 0.5, 0.5, 1)

        random.shuffle(self.answer_order)
        for j in range(len(self.right_ids)):
            btn = self.ids[self.right_ids[j]]
            btn.text = str(answers[self.answer_order[j]])
            btn.background_color = (0.5, 0.5, 0.5, 1)

        MainCode.prev_btn = None


# Function to generate random arithmetic equations
class Demi(App):
    def build(self):
        return MainCode()


# Run the Kivy application
if __name__ == '__main__':
    Demi().run()