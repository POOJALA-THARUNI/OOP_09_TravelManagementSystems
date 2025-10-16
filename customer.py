# customer.py
"""
Customer class → stores customer information.

Attributes:
- customer_id (str)
- name (str)
- email (str)
- phone (str)
- bookings (list of Booking objects)

Hint:
- Use utils.generate_id("CUST") to generate IDs.
- bookings should start as an empty list.
"""

class Customer:
    def __init__(self, customer_id,name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.bookings = []
        

    def add_booking(self,booking):
        self.bookings.append(booking)
        
       
    def __str__(self):
        return f"[{self.customer_id}] {self.name} ({self.email}, {self.phone})"
        
