# booking.py
"""
Booking class → represents a travel booking.

Attributes:
- booking_id (str)
- trip_name (str)
- price (float)
- status (str, e.g., "Confirmed", "Cancelled", "Pending")

💡 Hint:
- Use utils.generate_id("BOOK") for booking IDs.
"""

class Booking:
    def __init__(self, booking_id,customer_id, trip_name, price, status="Pending"):
         self.booking_id = booking_id
         self.customer_id=customer_id
         self.trip_name = trip_name
         self.price = price
         self.status = status
     

    def __str__(self):
         return f"Booking {self.booking_id}: {self.trip_name} - ₹{self.price} ({self.status})"
        
