from sense_hat import SenseHat
import time
from weather import Weather, Unit
import datetime
from random import choice
from time import sleep

sense = SenseHat()

while True:

    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('barcelona')
    condition = location.condition
    x = str(condition.text)
    y = str(condition.temp)

    sense.load_image("img/balena.png")
    time.sleep(2)
    sense.show_message("I'm always free :)")
    time.sleep(2)

    for event in sense.stick.get_events():
        sense.show_message(y + " Degrees")
        sense.show_message(x)

