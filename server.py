from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")
update_id = None

def auth():
	bot.send_message("Enter ID", from_)
	# username=()
	# bot.send_message("Enter Password", from_)
	# password=()
	
	# get_attendance(username, password)

def make_reply(msg, first_name, last_name):
	if msg == "Hi":
		reply = "Hello "+first_name+ " "+ last_name
		return reply

	elif msg == "Get":
		return auth()
	
	else:
		return "Try something else!"
	

while True:
	print("...")
	updates = bot.get_updates(offset=update_id)
	updates = updates["result"]
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try:
				message = item["message"]["text"]
			except:
				message = None
			from_ = item["message"]["from"]["id"]
			first_name = item['message']["from"]["first_name"]
			last_name = item['message']["from"]["last_name"]
			reply = make_reply(message, first_name, last_name)
			bot.send_message(reply, from_)
