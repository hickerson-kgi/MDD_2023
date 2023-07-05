
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
def generate_equation():
    operators = ['+', '-', '*', '/']
    operator = random.choice(operators)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    equation = f"{num1} {operator} {num2}"
    return equation

# Example usage:
equation = generate_equation()
print("Generated equation:", equation)
result = eval(equation)
print("Result:", result)



class MainWidget(GridLayout):
    pass
 
# we are defining the Base Class of our Kivy App
class MindfulMatchup1App(App):
    def build(self):
        # return a MainWidget() as a root widget
        return MainWidget()
 
if __name__ == '__main__':
     
    # Here the class MyApp is initialized
    # and its run() method called.
    MindfulMatchup1App().run()