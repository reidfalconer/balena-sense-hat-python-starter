from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    sense.load_image("img/balena.png")
    time.sleep(3)
    sense.show_message("DOM WALSH IS A PAISANO")
    time.sleep(3)
    sense.clear()
