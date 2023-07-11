import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button_pin = 12

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class LightingGrid(GridLayout):
    def __init__(self, **kwargs):
        super(LightingGrid, self).__init__(**kwargs)
        self.cols = 1
        self.button = Button(text="Screen Lighting")
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        self.button.text = "Button Pressed"

class MyApp(App):
    def build(self):
        return LightingGrid()

def on_pushbutton_press(channel):
    if GPIO.input(button_pin) == GPIO.LOW:
        app.root.on_button_press(None)

GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=on_pushbutton_press, bouncetime=300)

if __name__ == '__main__':
    app = MyApp()
    app.run()
