# Lists in Python

Lists are ordered, mutable collections that can store multiple items.

#### Creating a List

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

#### Accessing Elements

```python
print(fruits[0])  # First element
print(fruits[-1]) # Last element
```

#### Modifying a List

```python
fruits.append("orange")  # Adds an item
fruits[1] = "mango"  # Modifies an item
print(fruits)
```

#### Looping Through a List

```python
for fruit in fruits:
    print(fruit)
```

#### List Slicing

```python
print(fruits[1:3])  # Get elements from index 1 to 2
```

# Tuples in Python

Tuples are similar to lists but are immutable (cannot be changed after creation).

#### Creating a Tuple

```python
colors = ("red", "green", "blue")
print(colors)
```

#### Accessing Elements

```python
print(colors[0])
```

#### Looping Through a Tuple

```python
for color in colors:
    print(color)
```

#### Tuple Unpacking

```python
r, g, b = colors
print(r, g, b)
```

### Mutable vs Immutable Objects

- **Mutable**: Objects that can be modified after creation (e.g., lists, dictionaries, sets).
- **Immutable**: Objects that cannot be changed after creation (e.g., tuples, strings, numbers).

#### Example: Mutable List
```python
nums = [1, 2, 3]
nums.append(4)  # Modifies the list
print(nums)  # Output: [1, 2, 3, 4]
```

#### Example: Immutable Tuple
```python
nums_tuple = (1, 2, 3)
nums_tuple[0] = 4  # This will cause an error
```

### Practical Exercises

#### Exercise 1: List Operations
**Input:**
```python
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers[1] = 25
print(numbers)
```
**Output:**
```python
[10, 25, 30, 40, 50, 60]
```

#### Exercise 2: List Slicing
**Task:**
1. Create a list of 10 numbers.
2. Print only the first 5 numbers.
3. Print every alternate number from the list.

#### Exercise 3: Tuple Basics
**Task:**
1. Create a tuple with 4 cities.
2. Print the second city.
3. Try to modify one of the cities (observe the error).
