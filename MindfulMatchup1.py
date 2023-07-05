
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


def generate_equation():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    equation = f"{num1} {operator} {num2}"
    result = eval(equation)
    return equation, result

    equations = []
    for _ in range(4):
        equation, result = generate_equation()
        equations.append(equation)
        equations.append(result)

    # Print the list with alternating equation and result
    for i in range(0, len(equations), 2):
        equation = equations[i]
        result = equations[i + 1]

    return equations



#def answer_equation(equation):
    # actually figure out the answer
    #return 'correct answer'


class MainWidget(GridLayout):

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        ids = ['a1_btn', 'a2_btn']
        for id in ids:
            self.ids[id].text = str(generate_equation())

    def generate(self, id):
        self.ids[id].text = str(generate_equation())
        self.ids[id].background_color = (0, 1, 0.5, 1)
 
    def answer(self, id):
        equation = self.ids[id].text
        self.ids[id].text = answer_equation(equation)

 
# we are defining the Base Class of our Kivy App
class MindfulMatchup1App(App):
    def build(self):
        # return a MainWidget() as a root widget
        return MainWidget()
 
if __name__ == '__main__':
     
    # Here the class MyApp is initialized
    # and its run() method called.
    MindfulMatchup1App().run()