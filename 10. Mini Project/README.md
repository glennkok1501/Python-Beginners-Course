# Mini Project Brief: **Student Height Management System**

## **Project Overview:**
This project aims to build a **Student Height Management System** using Python. The system will read a text file containing student names and heights, then calculate the average height, find the tallest and shortest students, and provide a Command-Line Interface (CLI) for users to interact with the data (add, edit, delete students). The project will focus on file handling, data types, conditionals, loops, error handling, and user input.

## **Key Features:**
1. **Read a Text File:**
   - The system will load a file containing student data. Each line will have a student’s name and height (e.g., `Alice 160`).
   - Handle missing or malformed data gracefully with appropriate error messages.

2. **Calculate Average Height:**
   - Compute the average height of all students and display the result.

3. **Find the Tallest and Shortest Student:**
   - Find the tallest and shortest student in the list and display their name and height.

4. **CLI Interface:**
   - The system will allow users to:
     - **Add a Student**: Add a new student with their name and height.
     - **Edit a Student**: Modify an existing student’s name or height.
     - **Delete a Student**: Remove a student from the list.

5. **Error Handling:**
   - Handle errors such as invalid input, missing file, or invalid data formats.
   - Use appropriate exception handling to ensure the system doesn’t crash due to incorrect user input or file issues.

## **Detailed Project Steps:**

### 1. **Reading the Text File:**
   - The text file `students.txt` will be formatted with each line containing a student's name and height separated by a space. For example:
     ```
     Alice 160
     Bob 175
     Charlie 165
     ```
   - The program should read this file and convert the data into a list of tuples or a dictionary.

### 2. **Calculating Average Height:**
   - After reading the file and storing the data, calculate the average height using:
     ```python
     average_height = sum(heights) / len(heights)
     ```

### 3. **Finding the Tallest and Shortest Students:**
   - Once the data is loaded into a suitable data structure (list of tuples or dictionary), find the tallest and shortest student using Python’s `max()` and `min()` functions.

### 4. **CLI Interface for User Interaction:**
   The user will be prompted with the following menu options:
   - **Add a student**: Enter a new student’s name and height.
   - **Edit a student**: Modify a student’s information (name/height).
   - **Delete a student**: Remove a student from the list.
   - **Show all students**: Display all students in the list.
   - **Exit**: Exit the program.