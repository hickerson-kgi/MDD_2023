from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import RPi.GPIO as GPIO

# Set the GPIO pin number for the button
button_pin = 17  # Replace with the appropriate GPIO pin number you are using

# Setup GPIO mode and pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

class MyScreenApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        label = Label(text="Press the button to light up the screen", font_size='30sp')
        layout.add_widget(label)
        return layout

    def on_button_press(self, channel):
        # Here you can add code to control the screen's power or perform other screen-related actions
        Config.set('graphics', 'fullscreen', 'auto')
        Config.write()

if __name__ == '__main__':
    # Create an instance of the app
    app = MyScreenApp()

    # Add event detection for the button press
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=app.on_button_press, bouncetime=200)

    # Run the app
    app.run()

    # Clean up GPIO on app exit
    GPIO.cleanup()
