"""
The code below format a string for presentation
"""

age = 34
print(f"Your age is {age}")

final_greeting_template = "How are you, {} and {name}?"

name = "Giovani"
giovani_greeting = final_greeting_template.format(name, name="Gabriel")
print(giovani_greeting)

bob_greeting = final_greeting_template.format("Bob", name="Bruna")
print(bob_greeting)