# Python Basics Introduction

Welcome to the Python Basics Introduction repository! This repository is designed to help beginners get started with Python programming by providing simple and clear examples of fundamental concepts such as if-else statements, loops, and object-oriented programming (OOP). Whether you are new to programming or looking to refresh your Python skills, this repository is a great place to start.

## Table of Contents

1. [Getting Started](#getting-started)
2. [If-Else Statements](#if-else-statements)
3. [Loops](#loops)
4. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
5. [Contributing](#contributing)
6. [License](#license)

## Getting Started

To get started with the examples, make sure you have Python installed on your machine. You can download the latest version of Python from the [official Python website](https://www.python.org/downloads/).

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/python-basics-introduction.git
```

Navigate to the project directory:

```bash
cd python-basics-introduction
```

Now, you are ready to explore the examples!

## If-Else Statements

In the `if_else_statements.py` file, you will find examples of if-else statements. Understanding conditional statements is crucial in programming, and these examples will help you grasp the basics.

```python
# Example: if-else statement
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## Loops

The `loops.py` file contains examples of loops in Python, including `for` and `while` loops. Loops are essential for repetitive tasks, and these examples will demonstrate their usage.

```python
# Example: for loop
for i in range(5):
    print(i)

# Example: while loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1
```

## Object-Oriented Programming (OOP)

Explore the `oop.py` file to learn about the basics of object-oriented programming in Python. Understanding OOP concepts like classes and objects is crucial for building scalable and modular code.

```python
# Example: Class and Object
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} is barking!")

# Creating an instance of the Dog class
my_dog = Dog("Buddy")
my_dog.bark()
```

## Contributing

If you find any issues or want to contribute by adding more examples or improving the existing ones, feel free to submit a pull request. Your contributions are highly appreciated!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Feel free to use the code in this repository for your own learning and projects.

Happy coding! 🚀
