# Weather report in the terminal
# The user enters today's weather and the program prints a report + advice.

# -----------------------------
# Ask the user for the weather
# -----------------------------
city = input("City name: ")

temperature = float(input("Temperature (in Celsius): "))

condition = input(
    "Condition (sunny/cloudy/rainy/snowy): "
).strip().lower()

wind = float(input("Wind speed (km/h): "))

# -----------------------------
# Turn the temperature into a
# word (very cold, cold, mild, hot)
# -----------------------------
if temperature < 0:
    temp_word = "freezing"
elif temperature < 10:
    temp_word = "cold"
elif temperature < 20:
    temp_word = "mild"
elif temperature < 30:
    temp_word = "warm"
else:
    temp_word = "hot"

# -----------------------------
# Turn the wind into a word
# -----------------------------
if wind < 10:
    wind_word = "calm"
elif wind < 25:
    wind_word = "breezy"
else:
    wind_word = "windy"

# -----------------------------
# Work out the advice
# -----------------------------
advice = []

if condition == "sunny":
    advice.append("Wear sunscreen and sunglasses.")

elif condition == "cloudy":
    advice.append("Take a light jacket.")

elif condition == "rainy":
    advice.append("Bring an umbrella.")

elif condition == "snowy":
    advice.append("Wear warm boots and a coat.")

else:
    advice.append("Unknown condition - check it again.")

if temp_word == "freezing":
    advice.append("Wear a heavy coat, gloves and a hat.")
elif temp_word == "cold":
    advice.append("Wear a warm jacket.")
elif temp_word == "hot":
    advice.append("Drink plenty of water.")

if wind_word == "windy":
    advice.append("Hold onto your hat - it is windy!")

# -----------------------------
# Print the report
# -----------------------------
print()
print("============================================")
print("  WEATHER REPORT FOR", city.upper())
print("============================================")
print("  Temperature:", temperature, "C (" + temp_word + ")")
print("  Condition:  ", condition)
print("  Wind:       ", wind, "km/h (" + wind_word + ")")
print("--------------------------------------------")
print("  ADVICE:")

for tip in advice:
    print("   -", tip)

print("============================================")
