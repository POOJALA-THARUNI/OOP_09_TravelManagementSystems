# main.py
"""
Main program for Travel Booking System.

Steps:
1. Import TravelAgency from travel_agency.py
2. Create TravelAgency instance.
3. Display menu:
   - Add Customer
   - Make Booking
   - View Customer Bookings
   - Generate Report
   - Exit

Hint:
- Use input() for interaction.
- Wrap operations in try/except for clean error handling.
"""

from travel_agency import TravelAgency

def main():
     agency = TravelAgency()
    
     while True:
        print("\n--- Travel Booking Menu ---")
        print("1. Add Customer")
        print("2. Make Booking")
        print("3. View Customer Bookings")
        print("4. Generate Report")
        print("5. Exit")
    
        choice = input("Enter your choice: ")

        if choice == "1":
            name=input("Enter Customer Name:")
            email=input("email:")
            phone=int(input("phone:"))
            agency.add_customer(name,email,phone)
             
        elif choice == "2":
            customer_id=input("Customer_ID:")
            trip_name=input("Trip Name:")
            price=float(input("Price:"))
            agency.make_booking(customer_id,trip_name,price)
             
        elif choice == "3":
            customer_id=input("Enter Customer_ID to View Bookings:")
            agency.view_customer_bookings(customer_id)
            
        elif choice == "4":
            agency.generate_reports()

        elif choice == "5":
            print("Have a Great Journey!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
