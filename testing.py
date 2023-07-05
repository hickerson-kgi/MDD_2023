# main.py
import kivy
import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

def generate_equation():
    equations = []
    for _ in range(4):
        operators = ['+', '-', '*', '/']
        operator = random.choice(operators)
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        equation = f"{num1} {operator} {num2}"
        result = eval(equation)
        equations.append((equation, result))
    return equations

class MainWidget(GridLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        equations = generate_equation()
        buttons = [
            ('a1_btn', 'a1_result'),
            ('a2_btn', 'a2_result'),
            ('b1_btn', 'b1_result'),
            ('b2_btn', 'b2_result'),
            ('c1_btn', 'c1_result'),
            ('c2_btn', 'c2_result'),
            ('d1_btn', 'd1_result'),
            ('d2_btn', 'd2_result')
        ]
        for button_id, result_id in buttons:
            equation, result = equations.pop(0)
            self.ids[button_id].text = equation
            self.ids[result_id].text = str(result)

    def generate(self, id):
        equations = generate_equation()
        for button_id, result_id in buttons:
            equation, result = equations.pop(0)
            self.ids[button_id].text = equation
            self.ids[result_id].text = str(result)
            self.ids[result_id].background_color = (1, 1, 1, 1)

    def answer(self, id):
        equation = self.ids[id].text
        result = str(eval(equation))
        self.ids[id.replace('btn', 'result')].text = result

class MindfulMatchup1App(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MindfulMatchup1App().run()
