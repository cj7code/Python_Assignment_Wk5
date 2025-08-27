# Assignment 1: Design Your Own Class (Python)

## Overview
This assignment demonstrates the use of **Object-Oriented Programming (OOP)** concepts in Python.  
A simple example of **Students** is used to meet all required deliverables.

---

## Deliverables Met ✅
1. **Class created** – `Person` (parent) and `Student` (child).  
2. **Attributes & methods** – `name`, `__age`, `course`, `introduce()`, `study()`.  
3. **Constructors** – used to initialize each object with unique values.  
4. **Inheritance** – `Student` inherits from `Person`.  
5. **Polymorphism** – `introduce()` method is overridden in `Student`.  
6. **Encapsulation** – private attribute `__age` with getter (`get_age`) and setter (`set_age`).  

---

## Code Example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # Encapsulation: private attribute

    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

    def introduce(self):
        return f"My name is {self.name}, and I am {self.__age} years old."

class Student(Person):  # Inheritance
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    
    def introduce(self):  # Polymorphism
        return f"I am {self.name}, {self.get_age()} years old, studying {self.course}."

    def study(self):
        return f"{self.name} is studying hard!"

# Example usage
student1 = Student("Alice", 20, "Nursing")
print(student1.introduce())
print(student1.study())
print("Old age:", student1.get_age())
student1.set_age(21)
print("New age:", student1.get_age())
Sample Output
pgsql
Copy code
I am Alice, 20 years old, studying Nursing.
Alice is studying hard!
Old age: 20
New age: 21
How to Run 🖥️
Follow these steps to run the program:

Open a text editor

Examples: Notepad, VS Code, PyCharm

Copy the code

Paste the provided Python code into a new file

Save the file

Save it as student.py

Open a terminal/command prompt

On Windows: Press Win + R, type cmd, and press Enter

On Mac/Linux: Open the Terminal app

Navigate to the folder where the file is saved:

bash
Copy code
cd Desktop
Run the program

On Mac/Linux:

bash
Copy code
python3 student.py
On Windows:

bash
Copy code
python student.py

@ 2025 Joseph - PLP Academy
