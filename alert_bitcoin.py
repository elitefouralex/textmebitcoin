#bitcoin scheduler text code
import time
import requests
import schedule
import json
import os
from twilio.rest import Client

def txt_code():
	response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
	data = response.json()
	currency = data["data"]["base"]
	price = data["data"]["amount"]
	output4 = (f"{currency} is currently at {price} per Coinbase.")

	message_to_send = (output4)
	receiving_phone_number = os.environ.get("my_phone_number")
	#local_time = time.strftime("%A %B %d, %Y and its %X",time.localtime())
	account_sid = os.environ.get("twilio_acct_sid")
	auth_token = os.environ.get("twilio_auth_token")
	client = Client(account_sid, auth_token)

	message = client.messages \
					.create(
						 body= message_to_send,
						 from_= os.environ.get("twilio_phone_number"),
						 to= receiving_phone_number
					 )

	print(message.sid)
	print(f"\nI sent '{message_to_send}' to {receiving_phone_number} on {local_time}")
	
schedule.every().hour.at("00:00").do(txt_code)

while True:
	schedule.run_pending()
	time.sleep(1)
