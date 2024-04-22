# def greet():
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice outside {name}?")
# greet()

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice outside {name}?")

# name = input("What is your name? ")
# greet_with_name(name)

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# name = input("What is your name? ")
# location = input("What is your location? ")

# greet_with(name, location)

def greet_with(name = "Gunnar", location = "Reykjavik"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with()