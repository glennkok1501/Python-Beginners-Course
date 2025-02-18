
## Chapter 8: Dictionaries and Sets

### Dictionaries in Python

Dictionaries store key-value pairs and are unordered.

#### Creating a Dictionary

```python
student = {"name": "Alice", "age": 20, "grade": "A"}
print(student)
```

#### Accessing Values

```python
print(student["name"])  # Output: Alice
```

#### Modifying a Dictionary

```python
student["age"] = 21
print(student)
```

#### Looping Through a Dictionary

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

### Sets in Python

Sets are unordered collections of unique elements.

#### Creating a Set

```python
numbers = {1, 2, 3, 4, 5}
print(numbers)
```

#### Adding Elements

```python
numbers.add(6)
print(numbers)
```

#### Removing Elements

```python
numbers.remove(3)
print(numbers)
```

### Practical Exercises

#### Exercise 1: Dictionary Operations
**Input:**
```python
data = {"name": "John", "age": 25, "city": "New York"}
data["country"] = "USA"
data["age"] = 26
print(data)
```
**Output:**
```python
{'name': 'John', 'age': 26, 'city': 'New York', 'country': 'USA'}
```

#### Exercise 2: Set Operations
**Task:**
1. Create a set with five unique numbers.
2. Add a new number.
3. Remove one number.
4. Print the final set.

#### Exercise 3: Dictionary Key Sorting
**Task:**
1. Create a dictionary with five key-value pairs.
2. Print the dictionary keys in sorted order.

#### Exercise 4: Finding Common Elements in Sets
**Task:**
1. Create two sets with some common numbers.
2. Find and print the common elements.

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common = set1.intersection(set2)
print(common)  # Output: {4, 5}
```
