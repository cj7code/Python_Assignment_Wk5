# Assignment 1: Design Your Own Class
# Topic: Students

# Parent class (represents a general person)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age    # Encapsulation: private attribute (cannot be accessed directly outside)


    # Getter method to access private age
    def get_age(self):
        return self.__age
    

    # Setter method to safely change private age
    def set_age(self, new_age):
        if new_age > 0:      # small validation
            self.__age = new_age
        else:
            print("Age must be positive!")


    def introduce(self):
        return f"My name is {self.name}, and I am {self.__age} years old."


# Child class (Student inherits from Person)
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


    # Polymorphism: overriding parent's method
    def introduce(self):
        return f"I am {self.name}, {self.get_age()} years old, studying {self.course}."

    def study(self):
        return f"{self.name} is studying hard!"


# Creating objects
student1 = Student("Mapesho", 19, "Nursing")


# Testing methods
print(student1.introduce())       # Uses overridden introduce()
print(student1.study())


# Encapsulation in action
print("Old age:", student1.get_age())  
student1.set_age(20)              # Safely update age
print("New age:", student1.get_age())
