
# Flight Reservation System
# Using Searching and Sorting

flights = [
    {"id": 101, "name": "Air India", "source": "Pune",
     "destination": "Delhi", "price": 4500, "seats": 5},
    {"id": 102, "name": "IndiGo", "source": "Pune",
     "destination": "Mumbai", "price": 2500, "seats": 4},
    {"id": 103, "name": "Akasa Air", "source": "Pune",
     "destination": "Bengaluru", "price": 3500, "seats": 6},
    {"id": 104, "name": "SpiceJet", "source": "Pune",
     "destination": "Delhi", "price": 4000, "seats": 3},
    {"id": 105, "name": "IndiGo", "source": "Pune",
     "destination": "Goa", "price": 2000, "seats": 5}
]


# Display all flights
def display_flights(data):
    print("\nID   Airline       Source   Destination   Price   Seats")
    print("-" * 60)

    for f in data:
        print(f"{f['id']:<5} {f['name']:<13} "
              f"{f['source']:<8} {f['destination']:<13} "
              f"Rs.{f['price']:<6} {f['seats']}")


# Linear Search by destination
def linear_search():
    destination = input("Enter destination: ").strip().lower()
    found = []

    for f in flights:
        if f["destination"].lower() == destination:
            found.append(f)

    if found:
        print("\nFlights found:")
        display_flights(found)
    else:
        print("No flights found for this destination.")


# Binary Search by flight ID
def binary_search():
    flight_id = input("Enter flight ID: ").strip()

    if not flight_id.isdigit():
        print("Please enter a valid numeric flight ID.")
        return

    flight_id = int(flight_id)

    # Binary Search requires sorted data
    sorted_flights = sorted(flights, key=lambda f: f["id"])

    low = 0
    high = len(sorted_flights) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_flights[mid]["id"] == flight_id:
            print("\nFlight found:")
            display_flights([sorted_flights[mid]])
            return
        elif sorted_flights[mid]["id"] < flight_id:
            low = mid + 1
        else:
            high = mid - 1

    print("Flight ID not found.")


# Bubble Sort by ticket price
def sort_by_price():
    sorted_flights = flights.copy()
    n = len(sorted_flights)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if sorted_flights[j]["price"] > sorted_flights[j + 1]["price"]:
                sorted_flights[j], sorted_flights[j + 1] = (
                    sorted_flights[j + 1], sorted_flights[j]
                )

    print("\nFlights sorted by price (low to high):")
    display_flights(sorted_flights)


# Book a flight
def book_flight():
    flight_id = input("Enter flight ID to book: ").strip()

    if not flight_id.isdigit():
        print("Please enter a valid numeric flight ID.")
        return

    flight_id = int(flight_id)

    for f in flights:
        if f["id"] == flight_id:
            if f["seats"] <= 0:
                print("Sorry, no seats are available.")
                return

            passenger = input("Enter passenger name: ").strip()

            if not passenger:
                print("Passenger name cannot be empty.")
                return

            f["seats"] -= 1

            print("\nBooking Successful!")
            print("Passenger:", passenger)
            print("Airline:", f["name"])
            print("Destination:", f["destination"])
            print("Ticket Price: Rs.", f["price"])
            print("Remaining Seats:", f["seats"])
            return

    print("Flight ID not found.")


# Main Menu
while True:
    print("\n===== FLIGHT RESERVATION SYSTEM =====")
    print("1. Display All Flights")
    print("2. Search by Destination (Linear Search)")
    print("3. Search by Flight ID (Binary Search)")
    print("4. Sort Flights by Price (Bubble Sort)")
    print("5. Book a Flight")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        display_flights(flights)
    elif choice == "2":
        linear_search()
    elif choice == "3":
        binary_search()
    elif choice == "4":
        sort_by_price()
    elif choice == "5":
        book_flight()
    elif choice == "6":
        print("Thank you for using Flight Reservation System!")
        break
    else:
        print("Invalid choice. Please try again.")
