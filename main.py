import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f'{SCRIPT_DIR}/hotels.csv')



class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_data = df[df['id'] == hotel_id].iloc[0]

    def available(self):
        """Check if the hotel is available."""
        pass
        
    def book_room(self):
        """Book a room in the hotel."""
        pass
    
class ReservationTicket: 
    def __init__(self, name, hotel):
        pass

    def generate(self):
        """Generate a reservation ticket."""
        pass
    


print(df)
id = input("Enter the hotel ID you want to book: ")
hotel = Hotel(id)

if hotel.available():
    hotel.book_room()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("Sorry, the hotel is not available for booking at the moment.")