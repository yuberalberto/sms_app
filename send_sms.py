import json
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

# Add you auth information here:
# Your Account SID from twilio.com/console
TWILIO_ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
TWILIO_AUTH_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Phone Number from twilio.com/console
TWILIO_PHONE_NUMBER = "XXXXXXXXXXX"

def main():
  
  with open("./phones.json", "r") as file:
    try:
      phone_list = json.load(file)['numbers']
          
    except json.decoder.JSONDecodeError:
      print("There was a problem accessing the data.")


  try:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for number in range(len(phone_list)):
      message = client.messages.create(
        to=phone_list[number], 
        from_=TWILIO_PHONE_NUMBER,
        body="Hello from Python!")

      print(message.sid)

  except TwilioRestException as e:
    print(e)


if __name__ == "__main__":
    main()  