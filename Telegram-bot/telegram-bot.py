import telebot
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("TELEGRAM_API")
bot=telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["bpol"])
def bpol(message):
	bashCmd = ["python3","bpol.py"]
	process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
	output, error = process.communicate()


	bot.send_message(message.chat.id,output,parse_mode="html")


@bot.message_handler(commands=["pol"])
def pol(message):
	bashCmd = ["python3","pol.py"]
	process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
	output, error = process.communicate()


	bot.send_message(message.chat.id,output,parse_mode="html")


@bot.message_handler(commands=["pols"])
def pols(message):
	bashCmd = ["sh","pol-bpol.sh"]
	process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
	output, error = process.communicate()


	bot.send_message(message.chat.id,output,parse_mode="html")


@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id,"Send you token name as /token to get the statistics")

@bot.message_handler(commands=["help"])
def help(message):
	bot.send_message(message.chat.id,"Send you token name as /token to get the statistics")

bot.polling()
	
