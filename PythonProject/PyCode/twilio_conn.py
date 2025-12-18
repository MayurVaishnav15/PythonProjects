from twilio.rest import Client
from config import account_sid, auth_token , phone_number
def set_twilio_connection(account_sid, auth_token):
      
      """Set up Twilio client connection for WhatsApp messaging.
      """
      client = Client(account_sid, auth_token)
      return client

def send_whatsapp_message(client, quote):
      
      """Send a WhatsApp message containing the quote using Twilio.
      """
      message = client.messages.create(
          from_='whatsapp:+14155238886',  # Twilio sandbox WhatsApp number
          body=quote,
          to=f'whatsapp:{phone_number}'
          )
      return message.sid

client = set_twilio_connection(account_sid, auth_token)


      
  
 

