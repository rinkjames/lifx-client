import datetime
import pytz
from astral import Astral, Location, SUN_RISING, SUN_SETTING
import pifx

lifx = pifx.PIFX(api_key='c8a73e1cca19249bc29be8b043278188f3c46b8362b96abd7df4fc21f0c7c7c0')

#lifx.toggle_power() # toggle all lights
#lifx.toggle_power('label:Desk Lamp') # toggle light with label "Master Bedroom"
#lifx.set_state(color='blue', brightness='0.85') # set brightness to 85% and color to blue
#lifx.pulse_lights(color='red', duration=2.5) # pulse lights for 2.5 seconds
#lifx.set_state('label:Desk Lamp', color='hue:10 saturation:1 kelvin:3500', brightness=0.25, duration=2)
#lifx.state_delta('label:Desk Lamp', power='on', duration=5, hue=0, saturation=0, brightness=0.5, kelvin=4000)

l = Location()
l.name = 'Unit 1004 Greenmarket Place'
l.region = 'South Africa'
l.latitude = -33.922157
l.longitude = 18.420050
l.timezone = 'Africa/Johannesburg'
l.elevation = 32.26
l.solar_depression = 'nautical'

sun = l.sun()
blue_AM = l.blue_hour(direction=SUN_RISING)
gold_AM = l.golden_hour(direction=SUN_RISING)
blue_PM = l.blue_hour(direction=SUN_SETTING)
gold_PM = l.golden_hour(direction=SUN_SETTING)

#print('Information for %s/%s\n' % (l.name, l.region))

#timezone = l.timezone
#print('Timezone: %s' % timezone)

#print('Latitude: %.02f; Longitude: %.02f\n' % \
#(l.latitude, l.longitude))

now = pytz.timezone('Africa/Johannesburg').localize(datetime.datetime.now())

print('Dawn         %s' % str(sun['dawn']))
print('Sunrise      %s' % str(sun['sunrise']))
print('Noon         %s' % str(sun['noon']))
print('Sunset       %s' % str(sun['sunset']))
print('Dusk         %s' % str(sun['dusk']))
print('blue AM1     %s' % str(blue_AM[0]))
print('blue AM2     %s' % str(blue_AM[1]))
print('gold AM1     %s' % str(gold_AM[0]))
print('gold AM2     %s' % str(gold_AM[1]))
print('gold PM1     %s' % str(gold_PM[0]))
print('gold PM2     %s' % str(gold_PM[1]))
print('blue PM1     %s' % str(blue_PM[0]))
print('blue PM2     %s' % str(blue_PM[1]))
print('now          %s' % str(now))

def datetime_almost_equal(datetime1, datetime2, seconds=60):
    dd = datetime1 - datetime2
    sd = (dd.days * 24 * 60 * 60) + dd.seconds
    return abs(sd) <= seconds

print(now)
#print(blue[0])

print( datetime_almost_equal(now, blue_AM[0], seconds=90) )

if datetime_almost_equal(now,blue_AM[0],seconds=90):
    lifx.set_state('label:Desk Lamp', color='hue:10 saturation:1 kelvin:3500', brightness=0.25, duration=2)
elif datetime_almost_equal(now,gold_AM[0],seconds=90):
    lifx.set_state('label:Desk Lamp', color='hue:10 saturation:1 kelvin:3500', brightness=0.25, duration=2)
elif datetime_almost_equal(now,gold_AM[1],seconds=90):
    lifx.set_state('label:Desk Lamp', color='hue:10 saturation:1 kelvin:3500', brightness=0.25, duration=2)
