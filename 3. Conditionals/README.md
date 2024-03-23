# Conditionals
Python conditionals are programming constructs used to make decisions based on certain conditions.

## Conditional Operators
 The primary conditional statements in Python are: 
 1. **if:** It is used to execute a block of code only if a specified condition is true.

2. **elif (else if):** It allows you to check multiple conditions and execute a block of code corresponding to the first true condition encountered.

3. **else:** It is used to execute a block of code if none of the preceding conditions are true.
4. 
Example: Checking if a number is positive, negative, or zero
```py
num = 10

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```
- The if statement checks if the value of num is greater than 0.
- If the condition is true, it executes the indented block of code, printing "The number is positive."
- If the condition is false, it moves to the elif (else if) statement, which checks if the number is less than 0.
- If the second condition is true, it executes the corresponding block of code, printing "The number is negative."
- If both conditions are false, it executes the else block, printing "The number is zero."

## Logical Operators
Logical operators can be used within conditional operators to make decisions.
```py
a = True
b = False
print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False
```   
Example: Checking if a number is between 10 and 20 (inclusive) or is negative

```py
num = 15

if (num >= 10 and num <= 20) or num < 0:
    print("The number satisfies the condition.")
else:
    print("The number does not satisfy the condition.")
```
- The if statement checks if the value of num satisfies the condition (num >= 10 and num <= 20) or num < 0.
- The condition uses logical operators (and, or) to combine multiple conditions.
- If the condition is true, it executes the indented block of code, printing "The number satisfies the condition."
- If the condition is false, it executes the else block, printing "The number does not satisfy the condition."
