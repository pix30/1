# define a function that takes parameters
def greet(name, age):
    print("Hello " + name + "! You are " + str(age) + " years old.")


# define a function that returns a value
def add(a, b):
    return a + b


# call the functions with different arguments
greet("Zicheng", 15)
greet("Alex", 16)

total = add(4, 7)
print("4 + 7 =", total)


# count the number of vowels in a string
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


print(count_vowels("Hello World"))
print(count_vowels("Python"))
print(count_vowels("Zicheng Huang"))


total = add(4, 7)
print("4 + 7 =", total)

