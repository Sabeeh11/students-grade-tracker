def menu():
    # Display the menu options to the user 
    print("\nStudent Grades Tracker")
    print("1.Add Student")
    print("2.Upgrade Student Grades")
    print("3.View All Student Grades")
    print("4.Search For a Student")
    print("5.Exit")
    return input("Choose an Option: ")

grades_tracker = {}

def add_student(tracker):
    # Add a new student to the tracker
    name = input("enter Student's name: ")
    if name in tracker:
        print(f"Student {name} already exist")
    else:
        tracker[name] = []
        print(f"Student {name} added Successfully")
        
def update_grades(tracker):
    # Update grades for an existing student
    name = input("Enter the student's name: ")
    if name in tracker:
        while True:
            try:
                grades  = int(input(f"Enter a new grade For {name}: "))
                if grades < 0 or grades > 100:
                    print("Enter a grade between 0 and 100")
                else:
                    tracker[name].append(grades)
                    print(f"Updated new Grade for {name}: {tracker[name]}")
                    break
            except ValueError:
                print("Invalid input , Enter a valid Grade")
    else:
        print(f"{name} not found.")

def view_grades(tracker):
    # Display all students and their grades
    if tracker:
        for name , grades in tracker.items():
            print(f"{name} : {grades}")
    else:
        print("No student list available")                

def search_student(tracker):
    # Search for a student by name and display their grades
    name = input("Enter the student's name to search: ")

    if name in tracker:
        print(f"{name}'s grades : {tracker[name]}")
    else:
        print(f"Student {name} does not exist .")
def main(): 
    # Main program loop to keep the menu running until user exits
    while True:
        choice = menu()

        if choice == "1":
            add_student(grades_tracker)
        elif choice == "2":
            update_grades(grades_tracker)
        elif choice == "3":
            view_grades(grades_tracker)
        elif choice == "4":
            search_student(grades_tracker)
        elif choice == "5":
            print("Exiting menu...Menu exited")
            break
        else:
            print("Choose a valid option")                


if __name__ == "__main__":
    main()



