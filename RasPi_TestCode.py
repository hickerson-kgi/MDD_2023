import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

button_pin = 16
button_pin2= 26
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)


class LightingScreen(Screen):
    def __init__(self, **kwargs):
        super(LightingScreen, self).__init__(**kwargs)

        self.button1 = Button(text="Button 1")
        self.button1.bind(on_press=self.on_button1_press)
        self.add_widget(self.button1)

        self.button2 = Button(text="Button 2")
        self.button2.bind(on_press=self.on_button2_press)
        self.add_widget(self.button2)

    def on_button1_press(self, instance):
        self.button1.text = "Button 1 Pressed"

    def on_button2_press(self, instance):
        self.button2.text = "Button 2 Pressed"
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
