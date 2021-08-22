To set up the bot execute this command in your shell ->

git clone https://github.com/anonymous-06-02/Polars-bot
pip3 install -r requirements.txt

Next create .env file in which directry you cloned it and place these keys as in same order as given below in the .env file ->

NOMICS_API=Your_Nomics_API_KEY
BSCSCAN_API=Your_BSCSCAN_API_KEY
ETHERSCAN_API=Your_ETHERSCAN_API_KEY
TELEGRAM_API=Your_TELEGRAM-BOT_API_TOKEN

Now your bot is ready to be used just execute the following command ->

python3 telegram-bot.py