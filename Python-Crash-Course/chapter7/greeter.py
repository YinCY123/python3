name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello, " + name + '!')

# when you use the input() function, Python interprets everything
# the user enters as a string.

age = input("How old are you?")
age = int(age)
print(age > 10)