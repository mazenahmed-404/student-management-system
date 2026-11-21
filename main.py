
def main():
    # Initial student data
    students = [
        {"id": 1, "name": "ahmed", "grade": 85},
        {"id": 2, "name": "omar", "grade": 92}
    ]

    while True:
        print("\n========== STUDENT MANAGER ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Grade")
        print("5. Delete Student")
        print("6. Display Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            students = add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            students = update_student(students)
        elif choice == "5":
            students = delete_student(students)
        elif choice == "6":
            statistics(students)
        elif choice == "7":
            print("Thank you for using Student Manager!")
            break
        else:
            print("Please enter a valid option!")


# Add a student
def add_student(data):
    if not data:
        new_id = 1
    else:
        new_id = max(record["id"] for record in data) + 1

    new_name = input("Enter the student's name: ").strip().lower()

    while True:
        try:
            new_grade = int(input("Enter the student's grade (0-100): "))
            if 0 <= new_grade <= 100:
                break
            print("Grade must be between 0 and 100!")
        except ValueError:
            print("Please enter a valid whole number!")

    updated = data + [
        {"id": new_id, "name": new_name, "grade": new_grade}
    ]

    print(f"Student {new_name} added successfully!")
    return updated


# View all students
def view_students(data):
    if not data:
        print("There are no students to display.")
        return

    print("\n========== STUDENT LIST ==========")

    for record in data:
        print(
            f"ID: {record['id']} | "
            f"Name: {record['name']} | "
            f"Grade: {record['grade']}/100"
        )


# Search for a student
def search_student(data):
    if not data:
        print("The student list is empty!")
        return

    while True:
        print("\n1. Search by name")
        print("2. Search by ID")
        print("X. Go back")

        kind = input("Choose a search method: ").strip().lower()

        if kind == "x":
            return

        elif kind == "1":
            name_search = input("Enter the student's name: ").strip().lower()

            found = False
            for record in data:
                if record["name"] == name_search:
                    print(
                        f"ID: {record['id']} | "
                        f"Name: {record['name']} | "
                        f"Grade: {record['grade']}/100"
                    )
                    found = True

            if not found:
                print("No student with that name was found!")

        elif kind == "2":
            id_search = input("Enter the student's ID: ").strip()

            found = False
            for record in data:
                if str(record["id"]) == id_search:
                    print(
                        f"ID: {record['id']} | "
                        f"Name: {record['name']} | "
                        f"Grade: {record['grade']}/100"
                    )
                    found = True
                    break

            if not found:
                print("No student with that ID was found!")

        else:
            print("Please enter a valid option!")


# Update a student's grade
def update_student(data):
    if not data:
        print("The student list is empty!")
        return data

    while True:
        name_search = input(
            "Enter the student's name (or X to go back): "
        ).strip().lower()

        if name_search == "x":
            return data

        student = None

        for record in data:
            if record["name"] == name_search:
                student = record
                break

        if student is None:
            print("No student with that name was found!")
            continue

        while True:
            try:
                new_grade = int(input("Enter the new grade (0-100): "))

                if 0 <= new_grade <= 100:
                    student["grade"] = new_grade
                    print("Student grade updated successfully!")
                    return data

                print("Grade must be between 0 and 100!")

            except ValueError:
                print("Please enter a valid whole number!")


# Delete a student
def delete_student(data):
    if not data:
        print("The student list is empty!")
        return data

    while True:
        id_search = input(
            "Enter the student's ID (or X to go back): "
        ).strip().lower()

        if id_search == "x":
            return data

        try:
            id_search = int(id_search)
        except ValueError:
            print("Please enter a valid ID!")
            continue

        student = None

        for record in data:
            if record["id"] == id_search:
                student = record
                break

        if student is None:
            print("No student with that ID was found!")
            continue

        updated = [
            record for record in data
            if record["id"] != id_search
        ]

        print(f"Student {student['name']} deleted successfully!")
        return updated


# Display statistics
def statistics(data):
    count = len(data)

    print("\n========== STUDENT STATISTICS ==========")
    print(f"Total number of students: {count}")

    if not data:
        print("No statistics are available because the list is empty.")
        return

    total_grades = sum(record["grade"] for record in data)
    average = total_grades / count

    ordered = sorted(data, key=lambda record: record["grade"])

    print(f"Average grade: {average:.2f}")
    print(f"Highest grade: {ordered[-1]['grade']}")
    print(f"Lowest grade: {ordered[0]['grade']}")

    passed = 0
    failed = 0

    for record in data:
        if record["grade"] >= 50:
            passed += 1
        else:
            failed += 1

    print(f"Students who passed: {passed}")
    print(f"Students who failed: {failed}")

    print("\nStudents sorted by grade:")

    for record in ordered:
        print(
            f"ID: {record['id']} | "
            f"Name: {record['name']} | "
            f"Grade: {record['grade']}/100"
        )

main()
