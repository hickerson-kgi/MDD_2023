import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button_pin = 12

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class LightingScreen(Screen):
    def __init__(self, **kwargs):
        super(LightingScreen, self).__init__(**kwargs)
        self.button = Button(text="Screen Lighting")
        self.button.bind(on_press=self.on_button_press)
        self.add_widget(self.button)

    def on_button_press(self, instance):
        self.button.text = "Button Pressed"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LightingScreen(name="lighting"))
        return sm

def on_pushbutton_press(channel):
    if GPIO.input(button_pin) == GPIO.LOW:
        app.root.get_screen("lighting").on_button_press(None)

GPIO.add_event_detect(button_pin, GPIO.BOTH, callback=on_pushbutton_press, bouncetime=300)

if __name__ == '__main__':
    app = MyApp()
    app.run()
