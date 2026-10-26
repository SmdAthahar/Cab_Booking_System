from vehicles import Car, Bike
from fare import calculate_fare



car1 = Car("AP01AB1234", "Toyota", "Rahul", 20)
car2 = Car("AP01CD5678", "Hyundai", "Arjun", 25)



bike1 = Bike("AP01EF1111", "Honda", "Ravi", 10)
bike2 = Bike("AP01GH2222", "Yamaha", "Suresh", 12)



vehicles = [car1, car2, bike1, bike2]



print("================================")
print("        CAB BOOKING SYSTEM")
print("================================")

print("Available Vehicles:")

for i in range(len(vehicles)):

    vehicle = vehicles[i]

    if isinstance(vehicle, Car):
        vehicle_type = "Car"
    else:
        vehicle_type = "Bike"

    print(
        i + 1,
        "-",
        vehicle_type,
        "|",
        vehicle.brand,
        "| Driver:",
        vehicle.driver_name,
        "| Rate: Rs.",
        vehicle.price_per_km,
        "/KM"
    )


while True:

    print()

    choice = input(
        "Select a vehicle (1-4) or enter 0 to exit: "
    )

    if choice == "0":
        print("Thank you for using the Cab Booking System.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid vehicle selection. Please try again.")
        continue

    try:

        distance = float(
            input("Enter travel distance in KM: ")
        )

        if distance <= 0:
            print("Distance must be greater than zero.")
            continue

        selected_vehicle = vehicles[int(choice) - 1]

        total_fare = calculate_fare(
            selected_vehicle,
            distance
        )

        if isinstance(selected_vehicle, Car):
            vehicle_type = "Car"
        else:
            vehicle_type = "Bike"

        print()
        print("================================")
        print("           TRIP DETAILS")
        print("================================")

        print("Driver:", selected_vehicle.driver_name)
        print("Vehicle:", vehicle_type)
        print("Brand:", selected_vehicle.brand)
        print("Vehicle Number:", selected_vehicle.vehicle_number)
        print("Distance:", distance, "KM")
        print("Rate: Rs.", selected_vehicle.price_per_km, "/KM")
        print("Total Fare: Rs.", total_fare)

        print("================================")

    except ValueError:
        print("Invalid distance. Please enter a number.")