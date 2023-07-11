import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button_pin = 12

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class LightingGrid(GridLayout):
    def button_pressed(self, button):
        if button.text == "Button 1":
            self.parent.on_button_press("red")

class LightingScreen(Screen):
    def __init__(self, **kwargs):
        super(LightingScreen, self).__init__(**kwargs)
        self.add_widget(LightingGrid())

    def on_button_press(self, color):
        self.ids.light_button.background_color = color

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LightingScreen(name="lighting"))
        return sm

def on_pushbutton_press(channel):
    if GPIO.input(button_pin) == GPIO.LOW:
        app.root.get_screen("lighting").on_button_press("red")

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=on_pushbutton_press, bouncetime=300)

if __name__ == '__main__':
    app = MyApp()
    app.run()







<LightingGrid>:
    cols: 2
    Button:
        text: "Button 1"
        on_press: root.button_pressed(self)
    Button:
        text: "Button 2"
        on_press: root.button_pressed(self)
    Button:
        text: "Button 3"
        on_press: root.button_pressed(self)
    Button:
        text: "Button 4"
        on_press: root.button_pressed(self)

<LightingScreen>:
    BoxLayout:
        orientation: 'vertical'
        LightingGrid:

        Button:
            id: light_button
            text: "Light"
            size_hint_y: None
            height: dp(50)
            background_color: 0, 0, 0, 1  # Initial color is black

