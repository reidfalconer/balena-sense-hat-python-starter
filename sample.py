from sense_hat import SenseHat
import time
from weather import Weather, Unit

sense = SenseHat()
while True:

    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('barcelona')
    condition = location.condition
    x = str(condition.text)
    y = str(condition.temp)
    
    sense.load_image("img/balena.png")
    time.sleep(3)
    
    for event in sense.stick.get_events():
        sense.show_message(y + " Degrees")
        




