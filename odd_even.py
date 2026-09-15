# ask for a number and check if it is odd or even
number = int(input("Enter a number: "))

# a number is even if dividing by 2 leaves no remainder
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
