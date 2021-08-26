import discord
import subprocess
import os 
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()
@client.event

async def on_message(message):
	if message.author == client.user:
		return
	
	if message.content.startswith('!bpol'):
		bashCmd = ["python3","bpol.py"]
		process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
		output, error = process.communicate()
		lines = output.decode('utf-8').splitlines()
		await message.channel.send(lines[0])
		
		
	if message.content.startswith('!pol'):
		bashCmd = ["python3","pol.py"]
		process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
		output, error = process.communicate()
		lines = output.decode('utf-8').splitlines()
		await message.channel.send(lines[0])
		
		
DISCORD_API=os.getenv('DISCORD_API')
client.run(DISCORD_API)

