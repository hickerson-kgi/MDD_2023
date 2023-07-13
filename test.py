#start code
#Imported modules
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import random
from kivy.graphics import Color
from kivy.clock import Clock
###ADDED CODE-aTTEMPTING SCORE ONCE ALL COLORS ARE PRESSED
from kivy.uix.button import Button


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


# MainWidget represents the main widget of the application
class MainWidget(GridLayout):
    game_duration = 0
    game_timer = None
    # ADDED CODE FOR SCORE COUNT
    false_count = 0  # Counter for 'false' inputs
    correct_count = 0  # Counter for 'CORRECT!' inputs
    def __init__(self, **kwargs):

        super(MainWidget, self).__init__(**kwargs)
        self.questions, self.answers = generate_equation()

        self.matching_colors = [(1, 0, 0, 1), (1, 1, 0, 1), (0, 0, 1, 1),
                                (0, 1, 0, 1)]  # Store random matching colors for button pairs
        self.matches = 0

        self.left_ids = ['0q_btn', '1q_btn', '2q_btn', '3q_btn']
        for i in range(len(self.left_ids)):
            self.ids[self.left_ids[i]].text = str(self.questions[i])

        self.right_ids = ['0a_btn', '1a_btn', '2a_btn', '3a_btn']
        self.answer_order = [0, 1, 2, 3]
        random.shuffle(self.answer_order)
        for j in range(len(self.right_ids)):
            self.ids[self.right_ids[j]].text = str(self.answers[self.answer_order[j]])

        for id in self.left_ids:
            self.ids[id].background_color = (0.5, 0.5, 0.5, 1)

        for id in self.right_ids:
            self.ids[id].background_color = (0.5, 0.5, 0.5, 1)

        self.selected_question = False
        self.selected_answer = False
        ###AddedCode- Start the game timer
        Clock.schedule_interval(self.update_timer, 1)

    # Function to handle button click events
    def generate(self, id):
        # print('prev:', self.selected_question, self.selected_answer)

        # indicates left side, i.e. question
        if id[1] == 'q':
            self.selected_question = id

            # for i in self.left_ids:
            # self.ids[i].background_color = (0.5, 0.5, 0.5, 1)

            self.ids[id].background_color = (0.9, 0.9, 0.9, 1)

        # indicates right side, i.e. answer
        if id[1] == 'a':
            self.selected_answer = id

            # for i in self.right_ids:
            #     self.ids[i].background_color = (0.5, 0.5, 0.5, 1)

            self.ids[id].background_color = (0.9, 0.9, 0.9, 1)

        print('curr:', self.selected_question, self.selected_answer)

        # if there are now two selections, question and answer
        if (self.selected_question != False) and (self.selected_answer != False):

            q_index = int(self.selected_question[0])
            a_button = int(self.selected_answer[0])
            a_index = self.answer_order[a_button]

            print(q_index, a_button, a_index)
            # Deterimine if the question and answer are a matching pair
            if q_index == a_index:
                print('CORRECT!')
                ########   ADDED CODE FOR SCORE COUNT
                self.correct_count += 1 # Increment correct count
                # change BOTH buttons to color
                current_color = self.matching_colors[self.matches]
                self.ids[str(q_index) + 'q_btn'].background_color = current_color  # question button
                self.ids[str(a_button) + 'a_btn'].background_color = current_color  # answer button

                self.matches += 1
                self.matches = self.matches % 4

            else:
                self.selected_question = False
                self.selected_answer = False
                # #ADDED CODE FOR SCORE COUNT
                self.false_count += 1  # Increment false count
            self.selected_question = False
            self.selected_answer = False
        # AddedCode Display the game duration after button push
        print("Game Duration:", self.game_duration,"seconds")
        # Update the false count button text
        self.ids.false_count_btn.text = f"False Count: {self.false_count}"
        ###Added Code
        # Check if all matches have been made
        if self.matches == 4:
            self.print_score()  # Call the print_score() method
    ###Added Code-sCORE AFTER 4 COLORS MATCH



    ###Added Code
    def on_start(self):
        # start the game timer
        self.reset_timer()
        # Start the game timer
        self.game_timer = Clock.schedule_interval(self.update_timer, 1)
    ###Added Code
    def on_stop(self):
        # Stop the game timer
        if self.game_timer:
            self.game_timer.cancel()
        self.reset_timer()

    ###Added Code
    def update_timer(self, dt):
        self.game_duration += 1

    # Function to reset button colors after an incorrect match
    def reset_colors(self, dt):
        self.selected_question.background_color = (1, 1, 1, 1)
        self.selected_answer.background_color = (1, 1, 1, 1)
        self.selected_question = None
        self.selected_answer = None

    def answer(self, id):
        self.ids[id].background_color = (1, 1, 1, 1)


    #Added code- reset timer for the clock
    def reset_timer(self):
        self.game_duration = 0
        if self.game_timer:
            self.game_timer.cancel()

    def restart_game(self):
        self.reset_timer() #Added code-Reset the game timer
        questions, answers = generate_equation()
        self.answer_order = [0, 1, 2, 3]

        ##### ADDED CODE FOR SCORE COUNT
        self.false_count = 0  # Reset false count
        self.correct_count = 0  # Reset correct count

        # Update the false count button text
        self.ids.false_count_btn.text = f"False Count: {self.false_count}"

        #ADDED CODE- Reset the game logic
        self.selected_question = False
        self.selected_answer = False
        self.matches = 0

        #Reset button properties
        for i in range(len(self.left_ids)):
            btn = self.ids[self.left_ids[i]]
            btn.text = str(questions[i])
            btn.background_color = (0.5, 0.5, 0.5, 1)

        random.shuffle(self.answer_order)
        for j in range(len(self.right_ids)):
            btn = self.ids[self.right_ids[j]]
            btn.text = str(answers[self.answer_order[j]])
            btn.background_color = (0.5, 0.5, 0.5, 1)

        MainWidget.prev_btn = None


#ADDED CODE- Displays print of score
    def print_score(self):
        print("Score:")
        print("False inputs:", self.false_count)
        print("Correct inputs:", self.correct_count)

class MindfulMatchup1App(App):
    def build(self):
        return MainWidget()


# Run the Kivy application
if __name__ == '__main__':
    MindfulMatchup1App().run()

#end code