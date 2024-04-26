students = [
    {"name": "Dick Grayson", "hometown": "Bludhaven", "favorite_food": "Pineapple Pizza"},
    {"name": "Jason Todd", "hometown": "Gotham City", "favorite_food": "Chili Dogs"},
    {"name": "Tim Drake", "hometown": "Gotham City", "favorite_food": "Donuts"},
    {"name": "Stephanie Brown", "hometown": "Gotham Heights", "favorite_food": "Waffles"},
    {"name": "Damian Wayne", "hometown": "Nanda Parbat", "favorite_food": "Honeyed Dates"},
    {"name": "Cassandra Cain", "hometown": "Detroit", "favorite_food": "Chocolate"}
]

def list_names(students):
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']}")

def get_new_student():
    new_student = {}
    new_student["name"] = input("Please input a name for the new student:\n> ")
    new_student["hometown"] = input("Next, please input their hometown:\n> ")
    new_student["favorite_food"] = input("Last, please input their favorite food:\n> ")
    return new_student

def main():
    while True:
        print("Please select which action you'd like to do: add, view, or quit")
        choice = input("> ")

        if choice == "add":
            new_student = get_new_student()
            students.append(new_student)
            print("\nStudent added!\n")

        elif choice == "view":
            list_names(students)
            student_choice = int(input("Which student would you like to learn more about? Enter a number 1-{}:\n> ".format(len(students))))

            if 1 <= student_choice <= len(students):
                selected_student = students[student_choice - 1]
                print(f"Student {student_choice} is {selected_student['name']}. What would you like to know?")
                info_choice = input("Enter 'hometown' or 'favorite_food' to learn more:\n> ")
                
                if info_choice == "hometown":
                    print(f"{selected_student['name']}'s hometown is {selected_student['hometown']}")
                elif info_choice == "favorite_food":
                    print(f"{selected_student['name']}'s favorite food is {selected_student['favorite_food']}")
                else:
                    print("Invalid option. Please enter 'hometown' or 'favorite_food'.")
            else:
                print("Invalid student number. Please choose a number between 1 and {}.".format(len(students)))

        elif choice == "quit":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 'add', 'view', or 'quit'.")

if __name__ == "__main__":
    main()
