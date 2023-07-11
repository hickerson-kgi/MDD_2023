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
        self.add_widget(Button(text="Screen Lighting"))

def on_pushbutton_press(channel):
    app.root.current = "lighting"

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LightingScreen(name="lighting"))
        return sm

GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=on_pushbutton_press, bouncetime=300)

if __name__ == '__main__':
    app = MyApp()
    app.run()
