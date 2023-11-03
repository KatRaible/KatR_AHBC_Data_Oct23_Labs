class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print("Staring engine...")
        self.engine_on = True

    def make_noise(self):
        print("beep! beep!")

class Truck(Vehicle):
    def __init__(self, make, miles, price):
        super().__init__(make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True

class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print("vroom! vroom!")



truck_1 = Truck("Chevy", 234000, 5000)
truck_2 = Truck("Dodge", 45000, 33000)
truck_3 = Truck("Toyota", 69877, 14000)

moto_1 = Motorcycle("Harley Davidson", 146797, 19000, 198)
moto_2 = Motorcycle("Yamaha", 98765, 32123, 145)
moto_3 = Motorcycle("Honda", 123456, 23145, 176)

vehicle_comparison = []

def main():
    while True:
        print("Would you like to compare vehicles today? (y or n)")
        choice = input().lower()
        if choice == "y":
            display_vehicles()
            user_choice_comparison()
        elif choice == "n":
            compare_vehicles()
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def display_vehicles():
    print("Choose a category to view available vehicles:")
    print("1. Trucks")
    print("2. Motorcycles")
    category_choice = input()

    if category_choice == "1":
        print("Available trucks:")
        for truck in [truck_1, truck_2, truck_3]:
            print(f"{truck.make} - {truck.miles} miles - ${truck.price}")
    elif category_choice == "2":
        print("Available motorcycles:")
        for moto in [moto_1, moto_2, moto_3]:
            print(f"{moto.make} - {moto.miles} miles - ${moto.price}")

def user_choice_comparison():
    vehicle_choice = int(input("Enter the number of the vehicle you want to compare: "))
    if 1 <= vehicle_choice <= 3:
        vehicle_comparison.append(get_vehicle_by_index(vehicle_choice))
    else:
        print("Invalid selection. Please enter a valid number.")


def get_vehicle_by_index(index):
    all_vehicles = [truck_1, truck_2, truck_3, moto_1, moto_2, moto_3]
    return all_vehicles[index - 1]

          

def compare_vehicles():
    if vehicle_comparison:
        print("Vehicles selected for comparison: ")
        for vehicle in vehicle_comparison:
            print(f"{vehicle.make} - {vehicle.miles} miles - ${vehicle.price}")
            vehicle.start_engine()
            vehicle.make_noise()
    else:
        print("No vehicles selected for comparison.")



if __name__ == "__main__":
    main()