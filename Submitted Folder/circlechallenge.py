import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_diameter(self):
        return 2 * self.radius

    def calculate_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def grow(self):
        self.radius *= 2

    def get_radius(self):
        return self.radius
    
radius = float(input("Enter a radius: "))

def main(self):
    if radius <= 0:
        print("Please enter a positive number. ")
    else:
        pass



circle = Circle(radius)


print("Circle Information:\n")
print(f"Diameter: {circle.calculate_diameter()}")
print(f"Circumference: {circle.calculate_circumference()}")
print(f"Area: {circle.calculate_area()}")

while True:
    choice = input("Would you like your circle to grow? (y/n)  ")
    if choice.lower() == "y":
        circle.grow()
        print("Stand by while your circle magically grows")
        print("Circle Information:")
        print(f"New radius: {circle.get_radius()}")
        print(f"Diameter: {circle.calculate_diameter()}")
        print(f"Circumference: {circle.calculate_circumference()}")
        print(f"Area: {circle.calculate_area()}")
    elif choice.lower() == "n":
        print("Goodbye")
        break
    else:
        print("That is not a recognized option. Would you like your circle to grow? (y/n)")

if __name__ == "__main__":
    main()
