# Pydantic is a data validation and settings management library for Python, based on Python type annotations. It allows you to define data models with type hints and automatically validates the data against those types.

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# BaseModel is the main class provided by Pydantic that you can inherit from to create your own data models. It provides various features like data validation, serialization, and more.
# EmailStr is a special type provided by Pydantic that validates whether a given string is a valid email address.
# Field is a function that allows you to provide additional metadata and validation rules for model fields.

class Student(BaseModel):

    name: str = 'nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'32', 'email':'abc@gmail.com'}  # here age is a string, but Pydantic will automatically convert it to an integer if possible

student = Student(**new_student)

student_dict = dict(student)
# here we are converting the Pydantic model instance to a dictionary using the built-in dict() function. This allows us to easily access the model's data in a standard Python dictionary format.

print(student_dict['age'])

student_json = student.model_dump_json()
# here we are converting the Pydantic model instance to a JSON string using the model_dump_json() method. This allows us to easily serialize the model's data to a JSON format, which can be useful for APIs or data storage.