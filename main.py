import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

df_hotels = pd.read_csv(f'{SCRIPT_DIR}/hotels.csv', dtype={'id': str, 'name': str, 'available': str})
df_cards = pd.read_csv(f'{SCRIPT_DIR}/cards.csv', dtype=str).to_dict(orient='records')
df_card_security = pd.read_csv(f'{SCRIPT_DIR}/card_security.csv', dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_data = df_hotels.loc[df_hotels['id'] == hotel_id].squeeze() if not df_hotels.loc[df_hotels['id'] == hotel_id].empty else None

    def available(self):
        """Check if the hotel is available."""

        availability = self.hotel_data['available'] if self.hotel_data is not None else "no"
        if availability.lower() == 'yes':
            return True
        else:
            return False
        
    def book_room(self):
        """Book a room in the hotel."""

        df_hotels.loc[df_hotels['id'] == self.hotel_id, 'available'] = 'no'
        df_hotels.to_csv(f'{SCRIPT_DIR}/hotels.csv', index=False)
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
    

class CreaditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self, expiration, cvv, holder):
        """Validate the credit card details. Mock validation against a CSV file."""
        
        card_data = {
            'number': self.card_number,
            'expiration': expiration,
            'cvc': cvv,
            'holder': holder
        }

        if card_data in df_cards:
            return True

class SecureCreditCard(CreaditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security['number'] == self.card_number, 'password'].squeeze()
        
        if password == given_password:
            return True
            

    
print(df_hotels)
id = input("Enter the hotel ID you want to book: ")
hotel = Hotel(id)

if hotel.available():
    credit_card = SecureCreditCard(card_number="12383912389123")  

    if credit_card.validate(expiration="12/26", cvv="123", holder="JOHN SMITH"):
        user_card_password = input("Card password: ")
        if(credit_card.authenticate(given_password=user_card_password)):
            name = input("Enter your name: ")
            hotel.book_room()
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed!")
    else:
        print("There was a problem with your payment") 

else:
    print("Sorry, the hotel is not available for booking at the moment.")