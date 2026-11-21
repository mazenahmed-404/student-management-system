# Student Management System

A beginner-friendly command-line Student Management System built using Python.

This project allows users to manage student records and calculate academic statistics through an interactive terminal menu.

## Features

- **Add Students:** Add new students with automatically generated IDs.
- **View Students:** Display all registered students.
- **Search Students:** Search for students by name or ID.
- **Update Grades:** Modify an existing student's grade.
- **Delete Students:** Remove student records using their IDs.
- **Statistics:** Calculate average, highest, and lowest grades, and count passing and failing students.
- **Input Validation:** Handle invalid grades and IDs.

## Technologies Used

- Python 3
- Built-in Python functions and data structures

## Concepts Practiced

- Functions
- Lists and dictionaries
- `while` and `for` loops
- Conditional statements
- Input validation
- Exception handling (`try` / `except`)
- List comprehensions
- Lambda functions
- Sorting and built-in functions (`sorted`, `max`, `sum`)
- Returning and updating data between functions

## How to Run

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd student-management-system
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Data Storage

Student records are currently stored in an in-memory Python list.

This means the records reset when the application is closed. Persistent storage has not been implemented yet.

## Future Improvements

- Save student records in a JSON file.
- Load previously saved records when the application starts.
- Support searching and updating students using IDs.
- Improve the user interface.
- Add more detailed student reports.

## Author

Created as a Python programming practice project.
