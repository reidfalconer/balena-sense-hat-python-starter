from sense_hat import SenseHat
import time
from weather import Weather, Unit
import datetime
from random import choice
from time import sleep


sense = SenseHat()

sense.show_message("Ask a question", scroll_speed=0.06)
sleep(3)

replies = ['Signs point to yes',
        'Without a doubt',
        'You may rely on it',
        'Do not count on it',
        'Looking good',
        'Cannot predict now',
        'It is decidedly so',
        'Outlook not so good'
        ]

while True:


    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2 :
        sense.show_message(choice(replies))
    else:
        sense.clear()

    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('barcelona')
    condition = location.condition
    x = str(condition.text)
    y = str(condition.temp)

    #sense.load_image("img/balena.png")

    for event in sense.stick.get_events():
        sense.show_message(y + " Degrees")
        sense.show_message(x)

