from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import random
from kivy.graphics import Color
from kivy.clock import Clock
import RPi.GPIO as GPIO
import board
import neopixel


# Configure GPIO pins
GPIO.setmode(GPIO.BCM)
button1_pin = 16
button2_pin = 22
button3_pin = 25
button4_pin = 6
button5_pin = 24
button6_pin = 4
button7_pin = 23
button8_pin = 17



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

        #self.pin_list = [16,22,25,6,24,4,23,17]
        self.matching_colors_neo_r = [255, 255, 0, 0]
        self.matching_colors_neo_g = [0, 255, 255, 255]
        self.matching_colors_neo_b = [255, 0, 255, 0]

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
            self.light_button(k, 0, 0, 0)

        for l in self.right_ids:
            self.ids[l].background_color = (0.5, 0.5, 0.5, 1)
            self.light_button(l, 0, 0, 0)

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
                    self.light_button(self.selected_question, 0, 0, 0)


            self.selected_question = id

            # highlight selected answer if it is not matched yet
            if self.ids[id].background_color == [0.5, 0.5, 0.5, 1]:
                self.ids[id].background_color = (0.9, 0.9, 0.9, 1)
                self.light_button(id, 255, 255, 255)

        # indicates right side, i.e. answer
        if id[1] == 'a':
            # Unhighlights previous answer if a new answer is selected
            if self.selected_answer != False:
                if self.ids[str(self.selected_answer[0]) + 'a_btn'].background_color == [0.9, 0.9, 0.9, 1]:
                    self.ids[str(self.selected_answer[0]) + 'a_btn'].background_color = (0.5, 0.5, 0.5, 1)
                    self.light_button(str(self.selected_answer[0]) + 'a_btn', 0, 0, 0)


            self.selected_answer = id

            # highlight selected answer if it is not matched yet
            if self.ids[id].background_color == [0.5, 0.5, 0.5, 1]:
                self.ids[id].background_color = (0.9, 0.9, 0.9, 1)
                self.light_button(id, 255, 255, 255)

        # if there are now two selections, question and answer
        if (self.selected_question != False) and (self.selected_answer != False):
            q_index = int(self.selected_question[0])
            a_button = int(self.selected_answer[0])
            a_index = self.answer_order[a_button]

            # Determine if the selected question and answer are both matched already
            self.qcolored = False
            self.acolored = False

            for i in range(len(self.matching_colors)):
                if tuple(self.ids[str(q_index) + 'q_btn'].background_color) == self.matching_colors[i]:
                    self.qcolored = True
                if tuple(self.ids[str(a_button) + 'a_btn'].background_color) == self.matching_colors[i]:
                    self.acolored = True

            # only change color of buttons that have not been matched already
            if (self.acolored == False) and (self.qcolored == False):

                # Deterimine if the question and answer are a matching pair
                if q_index == a_index:
                    # change BOTH buttons to color
                    current_color = self.matching_colors[self.matches]
                    current_neo_r = self.matching_colors_neo_r[self.matches]
                    current_neo_g = self.matching_colors_neo_g[self.matches]
                    current_neo_b = self.matching_colors_neo_b[self.matches]

                    self.ids[str(q_index) + 'q_btn'].background_color = current_color  # question button
                    self.ids[str(a_button) + 'a_btn'].background_color = current_color  # answer button
                    self.light_button(str(q_index) + 'q_btn', current_neo_r, current_neo_g, current_neo_b)
                    self.light_button(str(a_button) + 'a_btn', current_neo_r, current_neo_g, current_neo_b)

                    self.matches += 1
                    self.matches = self.matches % 4

                else:
                    self.ids[str(q_index) + 'q_btn'].background_color = (0.5, 0.5, 0.5, 1)
                    self.ids[str(a_button) + 'a_btn'].background_color = (0.5, 0.5, 0.5, 1)
                    self.light_button(str(q_index) + 'q_btn', 0, 0, 0)
                    self.light_button(str(a_button) + 'a_btn', 0, 0, 0)

                    self.selected_question = False
                    self.selected_answer = False

            elif (self.acolored == True) and (self.qcolored == False):
                self.ids[str(q_index) + 'q_btn'].background_color = (0.5, 0.5, 0.5, 1)
                self.light_button(str(q_index) + 'q_btn', 0, 0, 0)
                self.selected_question = False
                self.selected_answer = False

            elif (self.qcolored == True) and (self.acolored == False):
                self.ids[str(a_button) + 'a_btn'].background_color = (0.5, 0.5, 0.5, 1)
                self.light_button(str(a_button) + 'a_btn', 0, 0, 0)
                self.selected_question = False
                self.selected_answer = False

            else:
                self.selected_question = False
                self.selected_answer = False


    def light_button(self, id, r, g, b):

        if id[1] == 'q':
            neo_id = int(id[0])

        else:
            neo_id = int(id[0]) + 4

        neo_pin = board.D18
        num_pins = 96
        pixels = neopixel.NeoPixel(neo_pin, num_pins)

        for i in range(12):
            pixel_index = neo_id * 12 + i
            pixels[pixel_index] = (r, g, b)


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
            self.light_button(self.left_ids[i], 0, 0, 0)

        random.shuffle(self.answer_order)
        for j in range(len(self.right_ids)):
            btn = self.ids[self.right_ids[j]]
            btn.text = str(answers[self.answer_order[j]])
            btn.background_color = (0.5, 0.5, 0.5, 1)
            self.light_button(self.right_ids[j], 0, 0, 0)


# Function to handle button click events
def button_callback(channel):
    if channel == button1_pin:
        App.get_running_app().root.generate('0q_btn')  # Replace with the corresponding button ID
    elif channel == button2_pin:
        App.get_running_app().root.generate('1q_btn')  # Replace with the corresponding button ID
    elif channel == button3_pin:
        App.get_running_app().root.generate('2q_btn')  # Replace with the corresponding button ID
    elif channel == button4_pin:
        App.get_running_app().root.generate('3q_btn')  # Replace with the corresponding button ID
    elif channel == button5_pin:
        App.get_running_app().root.generate('0a_btn')  # Replace with the corresponding button ID
    elif channel == button3_pin:
        App.get_running_app().root.generate('1a_btn')  # Replace with the corresponding button ID
    elif channel == button4_pin:
        App.get_running_app().root.generate('2a_btn')  # Replace with the corresponding button ID
    elif channel == button5_pin:
        App.get_running_app().root.generate('3a_btn')  # Replace with the corresponding button ID


# Set up button event detection
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button5_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button6_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button7_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button8_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button4_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button5_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button6_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button7_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button8_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)

# Run the Kivy application
class Demi(App):
    def build(self):
        return MainCode()


if __name__ == '__main__':
    Demi().run()
