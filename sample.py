from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    sense.load_image("img/balena.png")
    time.sleep(10)
    sense.show_message("Dominc Walsh is a prawn")
    time.sleep(10)
    sense.clear()
