from sense_hat import SenseHat
import time
from weather import Weather, Unit

sense = SenseHat()
sense.set_rotation(270)

number = [
0,1,1,1, # Zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, # One
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, # Two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, # Three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, # Four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, # Five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, # Six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, # Seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, # Eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, # Nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

hour_color = [255,0,0] # Red
minute_color = [0,255,255] # Cyan
empty = [0,0,0] # Black

clock_image = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

while True:
    hour = time.localtime().tm_hour + 2
    minute = time.localtime().tm_min

    weather = Weather(unit=Unit.CELSIUS)
    location = weather.lookup_by_location('barcelona')
    condition = location.condition
    x = str(condition.text)
    y = str(condition.temp)

    # Map digits to the clock_image array
    pixel_offset = 0
    index = 0
    for index_loop in range(0, 4):
        for counter_loop in range(0, 4):
            if (hour >= 10):
                clock_image[index] = number[int(hour/10)*16+pixel_offset]
            clock_image[index+4] = number[int(hour%10)*16+pixel_offset]
            clock_image[index+32] = number[int(minute/10)*16+pixel_offset]
            clock_image[index+36] = number[int(minute%10)*16+pixel_offset]
            pixel_offset = pixel_offset + 1
            index = index + 1
        index = index + 4

    # Color the hours and minutes
    for index in range(0, 64):
        if (clock_image[index]):
            if index < 32:
                clock_image[index] = hour_color
            else:
                clock_image[index] = minute_color
        else:
            clock_image[index] = empty

    # Display the time
    sense.low_light = True # Optional

    if hour == 16 and minute == 20:
        sense.load_image("img/balena.png")
        time.sleep(30)
        sense.show_message("4:20 Blaze it")
    else:
        sense.set_pixels(clock_image)
    
    time.sleep(1)

    for event in sense.stick.get_events():
        sense.show_message(y + " Degrees")
        sense.show_message(x)
        #sense.show_message("")