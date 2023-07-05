# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import kivy
import kivy
import kivy

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import random

def generate_equations(num_equations):
    equations = []

    for _ in range(num_equations):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])

        equation = f"{num1} {operator} {num2}"
        equations.append(equation)

    return equations

def get_solutions(equations):
    solutions = []
    for equation in equations:
        result = eval(equation)
        if result >= 0 and isinstance(result, int):
            solutions.append(str(result))
    return solutions

class MainWidget(GridLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.cols = 2  # Set the number of columns for the grid layout
        self.equation_buttons = []  # Store equation buttons separately
        self.solution_buttons = []  # Store solution buttons separately
        self.selected_buttons = []  # Store the currently selected buttons

        equations = generate_equations(4)  # Specify the number of equations (2x4 grid)
        solutions = get_solutions(equations)

        # Create equation buttons
        for equation in equations:
            button = Button(text=equation)
            self.equation_buttons.append(button)
            button.bind(on_release=self.selected)
            self.add_widget(button)

        # Create solution buttons
        for solution in solutions:
            button = Button(text=solution)
            self.solution_buttons.append(button)
            button.bind(on_release=self.selected)
            self.add_widget(button)

    def selected(self, button):
        if button in self.selected_buttons:
            self.selected_buttons.remove(button)
            button.text = button.text
            button.background_color = (1, 1, 1, 1)
        else:
            self.selected_buttons.append(button)
            button.text = '10'
            button.background_color = (0, 1, 0.5, 1)

        if len(self.selected_buttons) == 2:
            button1, button2 = self.selected_buttons

            if button1.text == button2.text:
                button1.background_color = (random.random(), random.random(), random.random(), 1)
                button2.background_color = button1.background_color
                self.selected_buttons = []
            else:
                button1.background_color = (1, 1, 1, 1)
                button2.background_color = (1, 1, 1, 1)
                button1.text = button1.text
                button2.text = button2.text
                self.selected_buttons.remove(button1)
                self.selected_buttons.remove(button2)

class MindfulMatchup1App(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MindfulMatchup1App().run()

