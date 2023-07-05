
# main.py
# import the kivy module
import kivy
 
# It’s required that the base Class
# of your App inherits from the App class.
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
 
# This class stores the info of .kv file
# when it is called goes to my.kv file

#math equations
import random

import random

import random

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
        result = eval(equation)
        questions.append(equation)
        answers.append(result)

    return questions, answers


#def answer_equation(equation):
    # actually figure out the answer
    #return 'correct answer'


class MainWidget(GridLayout):

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        questions, answers = generate_equation()

        left_ids = ['a1_btn', 'b1_btn', 'c1_btn', 'd1_btn']
        for i in range(len(left_ids)):
            self.ids[left_ids[i]].text = str(questions[i])
        right_ids = ['a2_btn', 'b2_btn', 'c2_btn', 'd2_btn']
        random.shuffle(answers)
        for j in range(len(right_ids)):
            self.ids[right_ids[j]].text = str(answers[j])



    def generate(self, id):
        self.ids[id].background_color = (0, 1, .5, 1)
 
    def answer(self, id):
        self.ids[id].background_color = (1, 1, 1, 1)

 
# we are defining the Base Class of our Kivy App
class MindfulMatchup1App(App):
    def build(self):
        # return a MainWidget() as a root widget
        return MainWidget()
 
if __name__ == '__main__':
     
    # Here the class MyApp is initialized
    # and its run() method called.
    MindfulMatchup1App().run()

    # ids = { 'btn1' = 0 , 'btn2' = 1, 'btn3' = 2, 'btn4' = 3} ->make a dictionary
