
names = ["Dick Grayson", "Jason Todd", "Tim Drake", "Stephanie Brown", "Damian Wayne", "Cassandra Cain"]
hometowns = ["Bludhaven", "Gotham City", "Gotham City", "Gotham Heights", "Nanda Parbat", "Detroit"]
favorite_foods = ["Pineapple Pizza", "Chili Dogs", "Donuts", "Waffles", "Honeyed Dates", "Chocolate"]


num_students = len(names)

while True:
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

    
    another_student = input("Would you like to learn about another student? (yes/no): ").strip().lower()
    if another_student != "yes":
        break
