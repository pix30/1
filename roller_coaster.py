# check if the rider is tall enough for the roller coaster
min_height = 48
height = int(input("Enter your height in inches: "))

if height >= min_height:
    print("You are tall enough to ride. Enjoy!")
else:
    print("Sorry, you need to be at least", min_height, "inches to ride.")
