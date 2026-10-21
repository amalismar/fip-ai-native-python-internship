# Storing Students scrores in a dictionary 
student_scores = {
    "Janet": 98,
    "Jack": 85,
    "Obi": 56,
    "Aisha": 78
}

# Adding a new student and their score 
def add_student():
    name = input("Enter student name: ").strip()
    score = float(input("Enter student score: "))

    if not name:
        print("Student name cannot be empty.")
        return

    if name in student_scores:
        print(f"Student {name} already exists.")
        return

    student_scores[name] = score
    print(f"Student {name} added with score {score}.")

# Displaying students and their scores
def display_students():
    print("\n--- Student Scores ---")

    if not student_scores:
        print("No students found.")
        return

    # Convert dictionary keys to a list and sort them
    sorted_names = sorted(student_scores.keys())

    for name in sorted_names:
        print(f"Name: {name}, Score: {student_scores[name]}")


# Display students that passed
def display_passed_students():
    print("\n--- Students Who Passed ---")
    passed_students = [
        (name, score) for name, score in student_scores.items() if score >= 60
    ]
    if not passed_students:
        print("No students passed.")
        return

    for name, score in passed_students:
        print(f"Name: {name}, Score: {score}")


# Run this Program to add and display student scores
display_students()
choice = input("Do you want to add a new student? (yes/no): ").strip().lower()
choice2 = input("Check students that passed? (yes/no): ").strip().lower()

if choice == "yes":
    print("\n--- Add a New Student ---")
    add_student()
    display_students()

else:
    print("No new student added.")

if choice2 == "yes":
    display_passed_students()

else:
    print("No check for passed students.")