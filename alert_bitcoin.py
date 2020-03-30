#bitcoin scheduler text code
import time
import requests
import schedule
import json
import os
from twilio.rest import Client

#run daily between 6am-midnight
#further modification can specify certain days of the week if you would like

def perfect_timing():
	schedule.every().day.at("06:00").do(txt_code)
	schedule.every().day.at("07:00").do(txt_code)
	schedule.every().day.at("08:00").do(txt_code)
	schedule.every().day.at("09:00").do(txt_code)
	schedule.every().day.at("10:00").do(txt_code)
	schedule.every().day.at("11:00").do(txt_code)
	schedule.every().day.at("12:00").do(txt_code)
	schedule.every().day.at("13:00").do(txt_code)
	schedule.every().day.at("14:00").do(txt_code)
	schedule.every().day.at("15:00").do(txt_code)
	schedule.every().day.at("16:00").do(txt_code)
	schedule.every().day.at("17:00").do(txt_code)
	schedule.every().day.at("18:00").do(txt_code)
	schedule.every().day.at("19:00").do(txt_code)
	schedule.every().day.at("20:00").do(txt_code)
	schedule.every().day.at("21:00").do(txt_code)
	schedule.every().day.at("22:00").do(txt_code)
	schedule.every().day.at("23:00").do(txt_code)
	schedule.every().day.at("00:00").do(txt_code)


def txt_code():
	response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
	data = response.json()
	currency = data["data"]["base"]
	price = data["data"]["amount"]
	output4 = (f"{currency} is at {price}")

	message_to_send = (output4)
	receiving_phone_number = os.environ.get("my_phone_number")
	local_time = time.strftime("%A %B %d, %Y and its %X",time.localtime())
	account_sid = os.environ.get("twilio_acct_sid")
	auth_token = os.environ.get("twilio_auth_token")
	client = Client(account_sid, auth_token)

	message = client.messages \
					.create(
						 body= message_to_send,
						 from_= os.environ.get("twilio_phone_number"),
						 to= receiving_phone_number
					 )
	
#old lines of code i dont just yet want to delete, so here they are, commented out
#	print(message.sid)
#	print(f"\nI sent '{message_to_send}' to {receiving_phone_number} on {local_time}")
	
#schedule.every().hour.at("00:00").do(txt_code)
#schedule.every().day.at("15:44", "15:45").do(txt_code)
perfect_timing()

while True:
	schedule.run_pending()
	time.sleep(1)
