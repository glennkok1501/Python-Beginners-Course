# File Handling and Exceptions

## Introduction
File handling and exception handling are essential aspects of Python programming. They allow us to work with external files and handle errors gracefully, preventing program crashes.

---

## 1. File Handling in Python
### Opening and Reading Files
Python provides the built-in `open()` function to work with files.

```python
# Opening a file and reading its content
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

### Using `with` Statement
Using the `with` statement ensures that the file is properly closed after use.

```python
# Reading a file using 'with' statement
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after this block
```

### Reading Line by Line
You can read files line by line using `readline()` or `readlines()`.

```python
# Using readline() to read one line at a time
with open("example.txt", "r") as file:
    first_line = file.readline()
    print("First Line:", first_line.strip())
```

```python
# Using readlines() to get a list of all lines
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```

### Writing to a File
You can write data to a file using `w` (write mode) or `a` (append mode).

```python
# Writing to a file (overwrites content)
with open("output.txt", "w") as file:
    file.write("Hello, this is a test file!\n")

# Appending to a file
with open("output.txt", "a") as file:
    file.write("This is an appended line.\n")
```

### Writing Multiple Lines Using `writelines()`
You can write multiple lines at once using `writelines()`.

```python
# Using writelines() to write multiple lines
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines_to_write)
```

### Additional File Modes
Python provides additional modes like `w+` and `a+`:

```python
# w+ mode: Write and read (overwrites existing content)
with open("output.txt", "w+") as file:
    file.write("New content written with w+ mode.\n")
    file.seek(0)  # Move to the beginning to read
    print(file.read())

# a+ mode: Append and read
with open("output.txt", "a+") as file:
    file.write("Additional content added with a+ mode.\n")
    file.seek(0)  # Move to the beginning to read
    print(file.read())
```

---

## 2. Exception Handling in Python
### What is Exception Handling?
Errors (also known as exceptions) can occur during program execution. Python provides a way to handle these errors gracefully using `try-except` blocks.

### Handling Exceptions with `try-except`

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
```

### Using `finally` to Ensure Cleanup
The `finally` block runs whether or not an exception occurs.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    file.close()
    print("File closed.")
```

### Raising Custom Exceptions
You can raise exceptions manually using the `raise` keyword.

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Valid age.")

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)
```

---

## 3. Summary
- File handling allows reading and writing to external files.
- Use `with open()` to ensure proper file closure.
- Use `readline()` to read a single line and `readlines()` to read all lines into a list.
- Use `writelines()` to write multiple lines at once.
- Exception handling prevents program crashes and provides meaningful error messages.
- Use `try-except` to catch errors and `finally` for cleanup.
- You can raise custom exceptions using `raise`.
- Use `w+` mode for writing and reading, overwriting existing content.
- Use `a+` mode for appending and reading without overwriting existing content.

---

## 4. Practice Exercises
1. Write a program that reads a file named `data.txt` and prints its content. Handle the `FileNotFoundError` exception.


```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")
```
---
2. Write a program that asks the user for a number, writes it to a file, and then reads it back.
```python
# Asking the user for a number and writing it to the file
number = input("Enter a number: ")

# Write the number to the file
with open("number.txt", "w") as file:
    file.write(number)

# Read the number from the file
with open("number.txt", "r") as file:
    content = file.read()
    print(f"The number from the file is: {content}")
```
---
3. Create a function that reads a file and counts the number of lines. If the file doesn’t exist, print an error message.
```python
try:
    with open("data.txt", "r") as file:
        lines = file.readlines()
        print(f"The number of lines in the file is: {len(lines)}")
except FileNotFoundError:
    print("Error: The file 'data.txt' does not exist.")
```
---
4. Implement a program that asks the user for two numbers, divides them, and handles `ZeroDivisionError` and `ValueError` exceptions.
```python
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
```
---
5. Write a program that asks the user for their age and raises a custom exception if the age is negative.
```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Age is valid.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as e:
    print(f"Error: {e}")
```
---
6. Experiment with `w+` and `a+` file modes. Write a program that writes and reads data using these modes.
```python
# w+ mode: Write and read (overwrites content)
with open("test_w_plus.txt", "w+") as file:
    file.write("Hello, w+ mode!")
    file.seek(0)  # Move to the beginning to read
    print("Content from w+: ", file.read())

# a+ mode: Append and read (does not overwrite)
with open("test_a_plus.txt", "a+") as file:
    file.write("Hello, a+ mode!\n")
    file.seek(0)  # Move to the beginning to read
    print("Content from a+: ", file.read())
```
---
7. **User Input and File Append:** Write a program that continuously asks the user for input and appends it to a file (`user_log.txt`). The program should stop taking input when the user types "exit".
```python
with open("user_log.txt", "a") as file:
    while True:
        user_input = input("Enter text to log (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            break
        file.write(user_input + "\n")
```
---
8. **Reading a CSV File:** Given a CSV file (`students.csv`) with columns `Name, Age, Grade`, write a program that reads the file and prints only the `Grade` column for each student.

```csv
Name,Age,Grade
Alice,12,A
Bob,14,B
Charlie,13,A
```

```python
# Example: Reading a specific column from a CSV file
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Grade"])  # Print only the Grade column
```