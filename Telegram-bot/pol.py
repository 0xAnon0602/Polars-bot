import requests 
from millify import millify
from web3 import Web3
import json
import subprocess
import os 
from dotenv import load_dotenv

load_dotenv()

ETHERSCAN_API=os.getenv("ETHERSCAN_API")


bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(bsc))

dexguru="https://api.dex.guru/v1/tokens/0xc17fbe1d709ddf6c0b6665dd0591046815ac7554"
supply=f"https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0xc17fbe1d709ddf6c0b6665dd0591046815ac7554&apikey={ETHERSCAN_API}"
headers = {"User-Agent": "Chrome/79"}

print("<b><u>POL(Polars Governance Token)(BEP-20)</u></b>")


dexguru_data_temp=requests.get(url=dexguru,headers=headers)
dexguru_data = dexguru_data_temp.json()
print('Price: $'+'<b><u>'+str('%.4f'%(dexguru_data['priceUSD']))+'</u></b>')
print('Liquidity: $'+'<b><u>'+str(millify(dexguru_data['liquidityUSD'], precision=2))+'</u></b>')
print('Volume 24H: $'+'<b><u>'+str(millify(dexguru_data['volume24hUSD'], precision=2))+'</u></b>')


supply_temp=requests.get(url=supply,headers=headers)
supply=json.loads(supply_temp.text)
print('Max Total Supply: '+'<b><u>'+str(millify((web3.fromWei(int(supply['result']), 'ether')), precision=3))+'</u></b>')



bashCmd = ["sh","pol-holders.sh"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()
lines = output.decode('utf-8').splitlines()
print(lines[0])
