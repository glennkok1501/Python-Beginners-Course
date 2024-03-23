# Data Types
There are commonly 3 data types in Python:      
1. [Strings](##Strings)
2. [Integers](##Integers)
3. [Floats](##Floats)

The type can be shown using the `type()` function   
```py
>>> type(1)   
<class 'int'>   

>>> type("hello world")   
<class 'str'>   

>>> type(1.0)   
<class 'float'>
```   

## Strings
In Python, a string is a sequence of characters enclosed within either single quotes `'`, double quotes `" "`, or triple quotes `''' '''` or `""" """`. Strings are immutable, meaning they cannot be changed after creation. They support various operations and methods for manipulation and are commonly used for representing text data in programs.

### Index
Indexing in Python allows you to access individual elements within data structures like lists, tuples, strings, or arrays using their position or index, starting from 0 and supporting negative indices for accessing elements from the end.   
```py
my_string = "Python"

# Access the first character
print(my_string[0])   # Output: "P"

# Access the third character
print(my_string[2])   # Output: "t"

# Access the last character using negative indexing
print(my_string[-1])  # Output: "n"
```   

### Slice
Slicing in Python enables extracting a portion of a sequence, such as a list, tuple, or string, by specifying start, stop, and optionally step parameters, providing a concise way to manipulate and access subsets of data efficiently.      
```py
my_string = "Hello, World!"

# Extract characters from index 1 to 5 (exclusive)
print(my_string[1:5])   # Output: "ello"

# Extract characters from index 7 onwards
print(my_string[7:])    # Output: "World!"

# Extract characters up to index 5 (exclusive)
print(my_string[:5])    # Output: "Hello"

# Reverse the string
print(my_string[::-1])  # Output: "!dlroW ,olleH"
```

### String Methods in Python    
- lower(): Converts all characters in a string to lowercase.
- upper(): Converts all characters in a string to uppercase.
```py
my_string = "Hello, World!"

# Convert string to lowercase
print(my_string.lower())  # Output: "hello, world!"

# Convert string to uppercase
print(my_string.upper())  # Output: "HELLO, WORLD!"
```

- isdigit(): Returns True if all characters in the string are digits. Otherwise, returns False.
```py
my_string = "12345"

# Check if string consists of digits only
print(my_string.isdigit())  # Output: True

my_string = "123abc"

# Check if string consists of digits only
print(my_string.isdigit())  # Output: False
```

- count(substring): Returns the number of occurrences of the specified substring in the string.
```py
my_string = "Python is fun to learn. Python is powerful."   

# Count occurrences of a substring
print(my_string.count("Python"))  # Output: 2
```

- find(substring): Returns the lowest index of the first occurrence of the specified substring in the string. If not found, returns -1.
```py
my_string = "Python is fun to learn."

# Find the index of the substring
print(my_string.find("fun"))  # Output: 10
```

- replace(old, new): Returns a copy of the string with all occurrences of the substring 'old' replaced by the substring 'new'.
```py
my_string = "Python is fun to learn."

# Replace substring with another substring
print(my_string.replace("fun", "exciting"))  
# Output: "Python is exciting to learn."
```

### String Formatting Examples in Python

#### Using %-formatting:
- %s: Placeholder for a string.
- %d: Placeholder for an integer.
```python
name = "Alice"
age = 30

# Using %-formatting to insert variables into a string
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  
# Output: "My name is Alice and I am 30 years old."
```

- Placeholder for variables, which are inserted using the format() method.
```py
name = "Bob"
age = 25

# Using str.format() method for string formatting
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  
# Output: "My name is Bob and I am 25 years old."
```

- Placeholder for variables, which are directly inserted within the f-string.
```py
name = "Charlie"
age = 35

# Using f-strings for string formatting
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: "My name is Charlie and I am 35 years old."
```

## Integers
In Python, an integer is a data type used to represent whole numbers without any fractional or decimal part. Integers can be positive, negative, or zero, allowing for mathematical operations like addition, subtraction, multiplication, and division to be performed on them.   

### Integer Math Operators
- +: Addition operator.
- -: Subtraction operator.
- *: Multiplication operator.
- /: Division operator.
- //: Integer division operator (returns the integer part of the quotient).
- %: Modulus operator (returns the remainder of the division).
- **: Exponentiation operator.
```python
# Addition
result_addition = 10 + 5  # Result: 15

# Subtraction
result_subtraction = 10 - 5  # Result: 5

# Multiplication
result_multiplication = 10 * 5  # Result: 50

# Division (returns float)
result_division = 10 / 5  # Result: 2.0

# Integer Division (returns integer)
result_integer_division = 10 // 3  # Result: 3

# Modulus (remainder)
result_modulus = 10 % 3  # Result: 1

# Exponentiation
result_exponentiation = 2 ** 3  # Result: 8
```

- abs(number): Returns the absolute value of the number.
```py
# Get the absolute value of a number
absolute_value = abs(-10)  # Result: 10
```

- &gt;: Greater than.
- <: Less than.
- &gt;=: Greater than or equal to.
- <=: Less than or equal to.
- ==: Equal to.
- !=: Not equal to.
```py
# Greater than
result_gt = 10 > 5  # Result: True

# Less than
result_lt = 10 < 5  # Result: False

# Greater than or equal to
result_gte = 10 >= 10  # Result: True

# Less than or equal to
result_lte = 10 <= 5  # Result: False

# Equal to
result_eq = 10 == 10  # Result: True

# Not equal to
result_neq = 10 != 5  # Result: True
```

## Floats
Floats in Python represent real numbers with a decimal point.

```py
# Float declaration
float_num = 3.14
```

Convert integer to float:
```py
float_from_int = float(5)  # Result: 5.0
```

Rounding floats:
```py
# Round a float to a specified number of decimal places
rounded_float = round(3.14159, 2)  # Result: 3.14
```

## Math Operators on String
In Python, mathematical operators are primarily used for numerical operations and do not have direct application to strings in the same way they do for numbers. However, some operators and methods can be used for string manipulation. Here's an example illustrating the concatenation operator `+` and repetition operator `*` applied to strings:
```py
# Concatenation using the + operator
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: "John Doe"

# Repetition using the * operator
message = "Hello! "
repeated_message = message * 3
print(repeated_message)  # Output: "Hello! Hello! Hello! "
```
- The + operator concatenates two strings (first_name and last_name) along with a space to create the full_name.
- The * operator repeats the string message three times, creating repeated_message.   

