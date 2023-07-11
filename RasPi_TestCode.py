import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button1_pin = 12
button2_pin = 16

GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class LightingGrid(GridLayout):
    def button_pressed(self, button):
        self.parent.on_button_press(button.text)

class LightingScreen(Screen):
    def __init__(self, **kwargs):
        super(LightingScreen, self).__init__(**kwargs)
        self.add_widget(LightingGrid())

    def on_button_press(self, button_text):
        if button_text == "Button 1":
            self.ids.light_button1.background_color = (1, 0, 0, 1)  # Set background color to red
            self.ids.light_button2.background_color = (0, 0, 0, 1)  # Reset background color
        elif button_text == "Button 2":
            self.ids.light_button1.background_color = (0, 0, 0, 1)  # Reset background color
            self.ids.light_button2.background_color = (1, 0, 0, 1)  # Set background color to red
        else:
            self.ids.light_button1.background_color = (0, 0, 0, 1)  # Reset background color
            self.ids.light_button2.background_color = (0, 0, 0, 1)  # Reset background color

    def light_button_pressed(self, button):
        button.background_color = (1, 0, 0, 1)  # Set background color to red

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LightingScreen(name="lighting"))
        return sm

def on_pushbutton1_press(channel):
    if GPIO.input(button1_pin) == GPIO.LOW:
        app.root.get_screen("lighting").on_button_press("Button 1")  # Set Button 1 as pressed
    else:
        app.root.get_screen("lighting").on_button_press("")  # Reset button state

def on_pushbutton2_press(channel):
    if GPIO.input(button2_pin) == GPIO.LOW:
        app.root.get_screen("lighting").on_button_press("Button 2")  # Set Button 2 as pressed
    else:
        app.root.get_screen("lighting").on_button_press("")  # Reset button state

GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback=on_pushbutton1_press, bouncetime=300)
GPIO.add_event_detect(button2_pin, GPIO.BOTH, callback=on_pushbutton2_press, bouncetime=300)

if __name__ == '__main__':
    app = MyApp()
    app.run()




<LightingGrid>:
    cols: 2
    Button:
        id: button1
        text: "Button 1"
        on_press: root.button_pressed(self)
    Button:
        id: button2
        text: "Button 2"
        on_press: root.button_pressed(self)
    Button:
        id: button3
        text: "Button 3"
        on_press: root.button_pressed(self)
    Button:
        id: button4
        text: "Button 4"
        on_press: root.button_pressed(self)

<LightingScreen>:
    BoxLayout:
        orientation: 'vertical'
        LightingGrid:

        BoxLayout:
            Button:
                id: light_button1
                text: "Light 1"
                on_press: root.light_button_pressed(self)
            Button:
                id: light_button2
                text: "Light 2"
                on_press: root.light_button_pressed(self)
