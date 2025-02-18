# Loops and Iteration

### Introduction to Loops

Loops allow us to execute a block of code multiple times, making our programs more efficient and readable.

### Types of Loops in Python

1. **For Loop** - Used for iterating over a sequence (list, tuple, dictionary, string, etc.).
2. **While Loop** - Executes as long as a given condition is `True`.
3. **Nested Loops** - Loops inside other loops.

### The `for` Loop

The `for` loop iterates over a sequence:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### The `while` Loop

The `while` loop executes while a condition is `True`:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### The `range()` Function

The `range()` function generates a sequence of numbers:

```python
for i in range(5):
    print(i)
```

### Loop Control Statements

- `break` - Exits the loop early.
- `continue` - Skips the current iteration and moves to the next.
- `pass` - Placeholder for future code.

Example:

```python
for num in range(10):
    if num == 5:
        break  # Stop the loop when num is 5
    print(num)
```

### Nested Loops

Loops can be nested inside one another:

```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

### Difference Between `continue`, `pass`, and `break`

1. `` - Exits the loop entirely and moves to the next statement after the loop.

   ```python
   for i in range(5):
       if i == 3:
           break  # Exits the loop when i is 3
       print(i)
   ```

   **Output:**

   ```
   0
   1
   2
   ```

2. `` - Skips the rest of the current iteration and moves to the next iteration of the loop.

   ```python
   for i in range(5):
       if i == 3:
           continue  # Skips printing 3 and moves to the next iteration
       print(i)
   ```

   **Output:**

   ```
   0
   1
   2
   4
   ```

3. `` - Acts as a placeholder when a statement is syntactically required but doesn’t execute any operation.

   ```python
   for i in range(5):
       if i == 3:
           pass  # Does nothing and continues normally
       print(i)
   ```

   **Output:**

   ```
   0
   1
   2
   3
   4
   ```

### Practical Exercises

#### Exercise 1: FizzBuzz

Write a program that prints numbers from 1 to 20, but for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".

```python
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

#### Exercise 2: Using `range()` with Step

Print all even numbers between 0 and 20 using `range()` with a step value.

```python
for num in range(0, 21, 2):
    print(num)
```

#### Exercise 3: Iterate Over Alternate Items in a List

Given a list of names, print every alternate name.

```python
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
for i in range(0, len(names), 2):
    print(names[i])
```

#### Exercise 4: Nested Loops for Pattern Printing

Write a program that prints the following pattern:

```
*
**
***
****
*****
```

```python
for i in range(1, 6):
    print("*" * i)
```

#### Exercise 5: Reverse Iteration

Print numbers from 10 to 1 in descending order using a loop.

```python
for num in range(10, 0, -1):
    print(num)
```

#### Exercise 6: Print a Christmas Tree

Write a program that prints a Christmas tree pattern using a loop.
```
    *
   ***
  *****
 *******
*********
    |
```

```python
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
print(" " * (n - 1) + "|")
```
