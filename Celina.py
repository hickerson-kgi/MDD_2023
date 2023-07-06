
# This is the main Python script.
# This is the main Python script.
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color
from kivy.lang import Builder
from kivy.clock import Clock

import random

def generate_equations(num_equations):
    equations = []

    while len(equations) < num_equations:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])

        equation = f"{num1} {operator} {num2}"
        equations.append(equation)

    return equations

def get_solutions(equations):
    solutions = []

    while len(solutions) < len(equations):
        result = eval(equations[len(solutions)])
        if result >= 0 and isinstance(result, int):
            solutions.append(str(result))

    return solutions

class MainWidget(GridLayout):
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.cols = 2  # Set the number of columns for the grid layout
        self.equation_buttons = []  # Store equation buttons separately
        self.solution_buttons = []  # Store solution buttons separately
        self.selected_equation = None  # Store the currently selected equation button
        self.selected_solution = None  # Store the currently selected solution button
        self.matching_colors = []  # Store random matching colors for button pairs

        equations = generate_equations(4)  # Specify the number of equations
        solutions = get_solutions(equations)

        # Create equation buttons in the first column
        for equation in equations:
            button = Button(text=equation)
            self.equation_buttons.append(button)
            button.bind(on_release=self.select_equation)
            self.add_widget(button)

        # Create solution buttons in the second column
        for solution in solutions:
            button = Button(text=solution)
            self.solution_buttons.append(button)
            button.bind(on_release=self.select_solution)
            self.add_widget(button)

        # Generate random matching colors for button pairs
        self.matching_colors = [Color(random.random(), random.random(), random.random(), 1) for _ in range(len(equations))]

    def select_equation(self, button):
        if self.selected_equation and self.selected_solution:
            # If a correct match was made, prevent further selections
            if self.selected_equation.background_color == (0, 1, 0, 1):
                return

        if self.selected_equation == button:
            # Deselect the button
            self.selected_equation.background_color = (1, 1, 1, 1)
            self.selected_equation = None
        else:
            if self.selected_equation:
                self.selected_equation.background_color = (1, 1, 1, 1)
            self.selected_equation = button
            button.background_color = (0, 0.7, 1, 1)

        self.check_solution()

    def select_solution(self, button):
        if self.selected_solution and self.selected_equation:
            # If a correct match was made, prevent further selections
            if self.selected_equation.background_color == (0, 1, 0, 1):
                return

        if self.selected_solution == button:
            # Deselect the button
            self.selected_solution.background_color = (1, 1,1, 1, 1, 1)
            self.selected_solution = None
        else:
            if self.selected_solution:
                self.selected_solution.background_color = (1, 1, 1, 1)
            self.selected_solution = button
            button.background_color = (0, 0.7, 1, 1)

        self.check_solution()

    def check_solution(self):
        if self.selected_equation and self.selected_solution:
            equation_text = self.selected_equation.text
            solution_text = self.selected_solution.text

            num1, operator, num2 = equation_text.split(' ')
            expected_result = eval(f"{num1} {operator} {num2}")

            if str(expected_result) == solution_text:
                # Correct match
                matching_color_equation = self.matching_colors[self.equation_buttons.index(self.selected_equation)]
                self.selected_equation.background_color = matching_color_equation.rgba
                matching_color_solution = self.matching_colors[self.solution_buttons.index(self.selected_solution)]
                self.selected_solution.background_color = matching_color_solution.rgba
                self.selected_equation = None
                self.selected_solution = None
            else:
                # Incorrect match
                self.selected_equation.background_color = (1, 0, 0, 1)
                self.selected_solution.background_color = (1, 0, 0, 1)
                Clock.schedule_once(self.reset_colors, 1)  # Reset colors after 1 second

    def reset_colors(self, dt):
        self.selected_equation.background_color = (1, 1, 1, 1)
        self.selected_solution.background_color = (1, 1, 1, 1)
        self.selected_equation = None
        self.selected_solution = None

class MindfulMatchup1App(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MindfulMatchup1App().run()
