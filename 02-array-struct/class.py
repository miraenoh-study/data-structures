class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# Create an instance
person = Person("James", 24, 1234.5)

# Access to an instance variable
print(person.name)