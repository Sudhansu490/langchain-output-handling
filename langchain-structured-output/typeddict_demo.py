# TypedDict is a feature in Python that allows you to define a dictionary with a specific structure, 
# where the keys and their corresponding value types are explicitly defined.
# This can help with type checking and code clarity.

from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'nitish', 'age':'35'}
# we are assigning a string value to the 'age' key, which is expected to be an integer according to the TypedDict definition.

print(new_person)