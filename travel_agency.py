# travel_agency.py
"""
TravelAgency class → manages customers and bookings.

Responsibilities:
- Add new customers
- Make bookings
- Link bookings to customers
- View bookings by customer
- Generate reports

💡 Hint:
- Use dictionaries {id: Customer} for customers.
- Maintain a list of all bookings.
"""

from customer import Customer
from booking import Booking
from exceptions import CustomerNotFoundError
import utils

class TravelAgency:
    def __init__(self):
        self.customers = {}
        self.bookings = []
        

    def add_customer(self,name, email, phone):
        customer_id=utils.generate_id("CUST")
        new_customer=Customer(customer_id,name,email,phone)
        self.customers[customer_id]=new_customer
        print(f"Customer ID:{customer_id} created for Customer Name:{name}")
        return customer_id
       
   
    
    def make_booking(self, customer_id, trip_name, price):
        if customer_id not in self.customers:         
            raise CustomerNotFoundError(f"Customer not found with ID:{customer_id}")
        booking_id=utils.generate_id("BOOK")
        new_booking=Booking(booking_id,customer_id,trip_name,price)
        self.bookings.append(new_booking)
        self.customers[customer_id].add_booking(new_booking)
        print(f'Booking ID:{booking_id} Created for {new_booking}')
        return booking_id
   
    
   
    
    def view_customer_bookings(self, customer_id):
        if customer_id not in self.customers:
            raise CustomerNotFoundError(f"Customer not found with ID:{customer_id}")
        customer=self.customers[customer_id]
        customer_bookings=[b for b in self.bookings if b.customer_id==customer_id]
        print(f"Bookings for {customer.name}(ID:{customer_id}):")
        if not customer_bookings:
            print("No Bookings Found")
        else:
            for b in customer_bookings:
                print(f"{b.booking_id}-{b.trip_name}-{b.price}")
        
   
    
    def generate_reports(self):
        total_customers=len(self.customers)
        total_bookings=len(self.bookings)
        total_revenue=0
        for book in self.bookings:
            total_revenue+= book.price
            
        print("Travel Agency Report")
        print(f"Total Customers:{total_customers}")
        print(f"Total Bookings:{total_bookings}")
        print(f"Total Revenue:{total_revenue}")
              
       