# Empty dictionary for storing data
# Initialising dictionary

student_grades = { }

# Add a new student
def add_student(name, grade):
    student_grades[name] = grade
    
    print(f"Added {name} with a grede {grade} successfully")


# Update a student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade

        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")


# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]

        print(f"{name} has been deleted successfully")

    else:
        print(f"{name} is not found!")


# View all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():

            print(f"{name} : {grade}")

    else:
        print("No students found/added")



def main():
    while True:
        print("\n Student Grades Management System\n")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Delete Student")
        print("4. View all Students")
        print("5. Exit\n")

        choice = int(input("Enter Your Choice : "))

        if choice == 1 :
            name = input("Enter student name : ")
            grade = int(input("Enter student grade : "))
            add_student(name , grade)

        elif choice == 2 :
            name = input("Enter student name : ")
            grade = int(input("Enter student grade to be updated : "))
            update_student(name , grade)

        elif choice == 3 :
            name = input("Enter student name : ")
            delete_student(name)

        elif choice == 4 :
            display_all_students()

        elif choice == 5 :
            print("Thank you for using...Closing the program")
            break

        else :
            print("Invalid choice..Please enter the valid choice")

main()