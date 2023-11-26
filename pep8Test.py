# This is a sample Python file to test PEP 8 compliance.

def calculate_square(number):
    return number**2


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
# Example usage
Num = 5
resUlt = calculate_square(Num)
print(resUlt)
person = Person("Alice", 30)
greeting = person.Greet()
print(greeting)
