
names = ["Dick Grayson", "Jason Todd", "Tim Drake", "Stephanie Brown", "Damian Wayne", "Cassandra Cain"]
hometowns = ["Bludhaven", "Gotham City", "Gotham City", "Gotham Heights", "Nanda Parbat", "Detroit"]
favorite_foods = ["Pineapple Pizza", "Chili Dogs", "Donuts", "Waffles", "Honeyed Dates", "Chocolate"]


num_students = len(names)

while True:
    print("\nOptions:")
    print("1. Enter a student number")
    print("2. See a list of all students")
    print("3. Search by student name")
    print("4. Exit")

    choice = input("Select an option (1/2/3/4): ")

    if choice == "1":

        while True:
            try:
                student_num = int(input("Enter a student number (1 to {}): ".format(num_students)))
                if 1 <= student_num <= num_students:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and {}.".format(num_students))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        student_num -= 1  

        
        print("Student's name: {}".format(names[student_num]))


        while True:
            category = input("Which category to display (Hometown or Favorite Food): ").strip().title()
            if category in ["Hometown", "Favorite Food"]:
                break
            else:
                print("Invalid category. Please enter 'Hometown' or 'Favorite Food'.")

        if category == "Hometown":
            print("Hometown: {}".format(hometowns[student_num]))
        elif category == "Favorite Food":
            print("Favorite Food: {}".format(favorite_foods[student_num]))

    elif choice == "2":
        for i in range(num_students):
            print("{}. {}".format(i + 1, names[i]))

    elif choice == "3":
        search_name = input("Enter a student name to search for: ").strip()
        matching_students = []
        for i in range(num_students):
            if search_name.lower() in names[i].lower():
                matching_students.append(i)
        if matching_students:
            print("Matching students:")
            for student_num in matching_students:
                print("Student {}: {}".format(student_num + 1, names[student_num]))
        else:
            print("No students found with that name.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")