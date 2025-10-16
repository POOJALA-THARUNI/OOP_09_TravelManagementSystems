# report.py
"""
Reporting functions for Travel Booking System.

Functions:
- customer_report(customer)
- agency_summary(agency)
"""

def customer_report(customer,customer_id):
    # Print all bookings of a customer
    if customer_id not in customer.customers:
        print(f"No Customer found with ID:{customer_id}")
        return
    c = customer.customers[customer_id]
    print(f"Bookings for {customer.name}(ID:{customer_id}):")
    customer_bookings=[b for b in customer.bookings if b.customer_id==customer_id]
    if not customer_bookings:
        print("No Bookings Found")
    else:
        for b in customer_bookings:
            print(f"{b.booking_id}-{b.trip_name}-{b.price}")
            
    
def agency_summary(agency):
    total_bookings=len(agency.bookings)
    total_revenue=0
    for book in agency.bookings:
        total_revenue+=book.price
    print("Travel Agency Report")
    print(f"Total Bookings:{total_bookings}")
    print(f"Total Revenue:{total_revenue}")
          
   
   