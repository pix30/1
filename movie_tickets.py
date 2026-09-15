# Get user input
age = int(input("Enter your age: "))
is_weekend_str = input("Is it the weekend? (yes/no): ")

ticket_price = 0

# --- YOUR CODE GOES HERE ---
# weekend tickets cost more than weekday tickets
if is_weekend_str == "yes":
    ticket_price = 15
else:
    ticket_price = 10

# seniors and children get $2 off on any day
if age >= 65 or age <= 12:
    ticket_price = ticket_price - 2


print(f"Your ticket price is: ${ticket_price}")
