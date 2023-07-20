
import RPi.GPIO as GPIO
import board
import neopixel


# Configure GPIO pins
GPIO.setmode(GPIO.BCM)
button1_pin = 23
button2_pin = 24
button3_pin = 12
button4_pin = 16
button5_pin = 17
button6_pin = 22
button7_pin = 5
button8_pin = 13
button9_pin = 26

class MainCode(GridLayout):
    # Function to handle button click events
    def generate(self, id):
        # indicates left side, i.e. question
        self.neo_pin = board.D10
        self.num_pins = 96
        self.pixels = neopixel.NeoPixel(self.neo_pin, self.num_pins)


        print("Button pressed", id)
        light_button(id, 255, 255, 255)


    def light_button(self, id, r, g, b):

        if id[1] == 'q':
            neo_id = int(id[0])

            for i in range(12):
                pixel_index = ((3 - neo_id) * 12) + i
                self.pixels[pixel_index] = (r, g, b)

        else:
            neo_id = int(id[0]) + 4

            for i in range(12):
                pixel_index = neo_id * 12 + i
                self.pixels[pixel_index] = (r, g, b)


# Function to handle button click events
def button_callback(channel):
    if channel == button1_pin:
        App.get_running_app().root.generate('0q_btn')  # Replace with the corresponding button ID
    elif channel == button2_pin:
        App.get_running_app().root.generate('1q_btn')  # Replace with the corresponding button ID
    elif channel == button3_pin:
        App.get_running_app().root.generate('2q_btn')  # Replace with the corresponding button ID
    elif channel == button4_pin:
        App.get_running_app().root.generate('3q_btn')  # Replace with the corresponding button ID
    elif channel == button5_pin:
        App.get_running_app().root.generate('0a_btn')  # Replace with the corresponding button ID
    elif channel == button6_pin:
        App.get_running_app().root.generate('1a_btn')  # Replace with the corresponding button ID
    elif channel == button7_pin:
        App.get_running_app().root.generate('2a_btn')  # Replace with the corresponding button ID
    elif channel == button8_pin:
        App.get_running_app().root.generate('3a_btn')  # Replace with the corresponding button ID
    elif channel == button9_pin:
        App.get_running_app().root.generate('reset')  # Reset game


# Set up button event detection
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button5_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button6_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button7_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button8_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button9_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(button1_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button2_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button3_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button4_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button5_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button6_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button7_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button8_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
GPIO.add_event_detect(button9_pin, GPIO.FALLING, callback=button_callback, bouncetime=200)
