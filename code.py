import datetime

class Car:
    def __init__(self, car_id, make, model, year):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.available = True

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class RentalSystem:
    def __init__(self):
        self.cars = []
        self.rented_cars = []

    def add_car(self, car):
        self.cars.append(car)

    def display_available_cars(self):
        available_cars = [car for car in self.cars if car.available]
        if available_cars:
            print("Available Cars:")
            for car in available_cars:
                print(f"{car.car_id}. {str(car)}")
        else:
            print("No cars available.")

    def rent_car(self, car_id, rental_type, rental_duration):
        for car in self.cars:
            if car.car_id == car_id and car.available:
                rental_cost = self.calculate_rental_cost(rental_type, rental_duration)
                rental_details = {
                    'car': car,
                    'rental_type': rental_type,
                    'rental_duration': rental_duration,
                    'rental_cost': rental_cost,
                    'rental_start_time': datetime.datetime.now()
                }
                self.rented_cars.append(rental_details)
                car.available = False
                print(f"You have rented: {str(car)} for {rental_duration} {rental_type}(s).")
                print(f"Total Rental Cost: ₹{rental_cost}")
                return
        print(f"Car with ID {car_id} not available for rent.")

    def return_car(self, car_id):
        for rental in self.rented_cars:
            if rental['car'].car_id == car_id:
                rental_end_time = datetime.datetime.now()
                rental_duration = (rental_end_time - rental['rental_start_time']).total_seconds() / 3600
                rental_cost = self.calculate_rental_cost(rental['rental_type'], rental_duration)
                rental['car'].available = True
                print(f"You have returned: {str(rental['car'])}.")
                print(f"Rental Duration: {round(rental_duration, 2)} hours.")
                print(f"Total Rental Cost: ₹{rental_cost}")
                self.rented_cars.remove(rental)
                return
        print(f"Car with ID {car_id} not found in the rented cars list.")

    def calculate_rental_cost(self, rental_type, rental_duration):
        if rental_type == 'hourly':
            return 2000 * rental_duration
        elif rental_type == 'daily':
            return 5000 * rental_duration
        elif rental_type == 'weekly':
            return 10000 * rental_duration
        else:
            raise ValueError("Invalid rental type. Choose 'hourly', 'daily', or 'weekly'.")

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

# Cars examples
car1 = Car(1, "Mahindra", "XUV 300", 2020)
car2 = Car(2, "TATA", "Harrier", 2024)
car3 = Car(3, "Toyota", "Innova", 2016)

rental_system = RentalSystem()
rental_system.add_car(car1)
rental_system.add_car(car2)
rental_system.add_car(car3)

rental_system.display_available_cars()

customer1 = Customer(101, "Shubhankar Jadhav")

rental_system.rent_car(1, 'hourly', 2)
rental_system.return_car(1)

rental_system.rent_car(2, 'daily', 3)
rental_system.return_car(2)
