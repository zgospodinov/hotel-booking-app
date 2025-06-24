import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f'{SCRIPT_DIR}/hotels.csv', dtype={'id': str, 'name': str, 'available': str})



class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_data = df.loc[df['id'] == hotel_id].squeeze() if not df.loc[df['id'] == hotel_id].empty else None

    def available(self):
        """Check if the hotel is available."""

        availability = self.hotel_data['available'] if self.hotel_data is not None else "no"
        if availability.lower() == 'yes':
            return True
        else:
            return False
        
    def book_room(self):
        """Book a room in the hotel."""

        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv(f'{SCRIPT_DIR}/hotels.csv', index=False)
        print(f"Room booked successfully at {self.hotel_data['name']} hotel.")
    
class ReservationTicket: 
    def __init__(self, name, hotel):
        self.customer_name = name
        self.hotel = hotel

    def generate(self):
        """Generate a reservation ticket."""
        
        content = f"""
        Reservation Ticket
        ------------------
        Name: {self.customer_name}
        Hotel: {self.hotel.hotel_data['name']}
        Hotel ID: {self.hotel.hotel_id}
        """
        return content
    


print(df)
id = input("Enter the hotel ID you want to book: ")
hotel = Hotel(id)

if hotel.available():
    name = input("Enter your name: ")
    hotel.book_room()
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("Sorry, the hotel is not available for booking at the moment.")