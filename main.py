import locationGetter as lg
import weatherGetter as wg

print "hello"
a = 5 * 6

print a

# TODO: make sure spaced names are formatted correctly,
# e.g."Merthyr Tydfil" -> "Merthyr%20Tydfil
# browser does this anyway, will check on it

location_getter = lg.LocationGetter()
weather_getter = wg.WeatherGetter()
weather_getter.set_location("London", "UK")
weather_getter.get_weather()