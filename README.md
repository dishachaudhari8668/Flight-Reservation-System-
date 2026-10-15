# Flight-Reservation-System-
Flight Reservation System using Searching and Sorting in Python
# Implementation of Flight Reservation System Using Searching and Sorting

## 1. Project Description
The Flight Reservation System is a Python-based mini project developed for the Data Structures subject. It helps users view available flights, search for flights, sort flights according to ticket prices, and book tickets.

## 2. Objectives
- To implement Linear Search.
- To implement Binary Search.
- To implement Bubble Sort.
- To search and display available flights.
- To book flights and manage seat availability.

## 3. Technologies Used
- Programming Language: Python
- Data Structures: List and Dictionary
- Algorithms: Linear Search, Binary Search, Bubble Sort

## 4. Features
1. Display all available flights.
2. Search flights by destination.
3. Search flights by flight ID.
4. Sort flights by ticket price in ascending order.
5. Book a flight using its flight ID.
6. Display booking confirmation and remaining seats.

## 5. Algorithms Used

### Linear Search
Linear Search checks each flight one by one to find flights matching the given destination.

Time Complexity: O(n)

### Binary Search
Binary Search finds a flight using its ID by repeatedly dividing the sorted list into halves.

Time Complexity: O(log n) after sorting by flight ID.

### Bubble Sort
Bubble Sort compares adjacent flight prices and swaps them to arrange flights from lowest to highest price.

Time Complexity: O(n²) in the average and worst cases.

## 6. How to Run the Project
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python flight_reservation.py
```

## 7. Sample Output
The program displays available flights, searches flights by destination or ID, sorts flights by price, and confirms bookings.

## 8. Limitations
- Flight details are predefined.
- Booking information is stored temporarily.
- Data is reset when the program is restarted.

## 9. Conclusion
This project demonstrates the practical use of searching and sorting algorithms in a flight reservation system. It helps understand how data structures can be used to search, arrange, and manage flight information efficiently.

## 10. Author
Name: Your Name
