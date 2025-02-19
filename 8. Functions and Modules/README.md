# Functions and Modules

## Introduction
Functions and modules are essential building blocks of Python programming. They help make code reusable, organized, and easier to maintain.

---

## 1. Functions in Python
### What is a Function?
A function is a reusable block of code that performs a specific task. Functions help break down a program into smaller, manageable parts.

### Defining a Function
In Python, a function is defined using the `def` keyword.

```python
# Example of a simple function
def greet():
    print("Hello, welcome to Python!")

# Calling the function
greet()
```

### Function with Parameters
Functions can take inputs, known as **parameters**, to perform operations dynamically.

```python
# Function with parameters
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python!")

# Calling the function
greet_user("Alice")
```

### Function with Return Value
A function can return a value using the `return` statement.

```python
# Function that returns a value
def add_numbers(a, b):
    return a + b

# Using the function
result = add_numbers(5, 3)
print("Sum:", result)
```


```python
# Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(4))  # Defaults to square
print(power(4, 3))  # Raises to the power of 3
```

```python
# Function with variable arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5))
```

---

## 2. Modules in Python
### What is a Module?
A module is a file that contains Python code (functions, variables, and classes) that can be reused in different programs. Python has built-in modules, and you can also create your own.

### Importing Modules
You can import a module using the `import` keyword.

```python
# Importing the built-in math module
import math

# Using the sqrt function from the math module
print(math.sqrt(16))
```

### Using the Random Module
Python provides the `random` module to generate random numbers and choices.

```python
import random

# Generate a random integer between 1 and 10
print(random.randint(1, 10))

# Choose a random element from a list
choices = ["apple", "banana", "cherry"]
print(random.choice(choices))
```

### Creating Your Own Module
You can create your own module by writing Python code in a separate `.py` file and importing it.

1. **Create a file named `my_module.py`** and add the following code:

```python
# my_module.py

def square(num):
    return num ** 2
```

2. **Use the module in another script:**

```python
# Importing the custom module
import my_module

# Using the function from the module
print(my_module.square(4))
```

### Importing Specific Functions
Instead of importing the whole module, you can import specific functions.

```python
from math import sqrt

print(sqrt(25))  # No need to use math.sqrt()
```

### Aliasing Modules
You can give a module an alias using `as`.

```python
import math as m

print(m.pi)  # Using alias instead of math.pi
```

---

## 3. Summary
- Functions help organize and reuse code efficiently.
- Functions can take parameters and return values.
- Functions can return multiple values, have default arguments, and accept variable arguments.
- Modules allow code to be reused across multiple files.
- Python has built-in modules like `math` and `random`, and you can create your own.

---

## 4. Practice Exercises
1. Write a function called `multiply` that takes two numbers as parameters and returns their product.
2. Create a module called `math_operations.py` with functions for addition, subtraction, multiplication, and division.
3. Import and use your `math_operations` module in another script.
4. Write a function that takes a list of numbers and returns the largest and smallest numbers in the list.
5. Create a function that simulates rolling two dice and returns their sum. Use the `random` module to generate the dice rolls.
6. Write a function that asks the user for their name and age, then prints a message saying how old they will be in 5 years.

```python
# Example of input-based function
def future_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello {name}, in 5 years you will be {age + 5} years old.")

future_age()
```