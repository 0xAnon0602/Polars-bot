import requests 
from millify import millify
from web3 import Web3
import json
import subprocess
import os 
from dotenv import load_dotenv

load_dotenv()

BSCSCAN_API=os.getenv("BSCSCAN_API")
NOMICS_API=os.getenv("NOMICS_API")

bsc = "https://data-seed-prebsc-1-s1.binance.org:8545/"
web3 = Web3(Web3.HTTPProvider(bsc))

# urls to be used 
nomics=f"https://api.nomics.com/v1/currencies/ticker?key={NOMICS_API}&ids=BPOL&interval=24h&convert=USD"
dexguru="https://api.dex.guru/v1/tokens/0x8a9c889e60ee674f0d55075fa0d60fb05e1a7aee-bsc"
supply=f"https://api.bscscan.com/api?module=stats&action=tokenCsupply&contractaddress=0x8a9c889e60ee674f0d55075fa0d60fb05e1a7aee&apikey={BSCSCAN_API}"
headers = {"User-Agent": "Chrome/79"}

print('```'+"bPOL(Polars Governance Token)(BEP-20)"+'```        ',end='')
 
#extractin data from nomics 
nomics_data_temp=requests.get(url=nomics,headers=headers)
nomics_data = nomics_data_temp.json()
print('```'+'Price: $'+str('%.4f'%(float(nomics_data[0]['price'])))+'```',end='                                                              ')
print('```'+'ATH: $'+ str('%.3f'%(float(nomics_data[0]['high'])))+'```',end='                                                         ')

#extracting data from dexguru
dexguru_data_temp=requests.get(url=dexguru,headers=headers)
dexguru_data = dexguru_data_temp.json()
print('```'+'Liquidity: $'+str(millify(dexguru_data['liquidityUSD'], precision=2))+'```',end='                                                   ')
print('```'+'Volume 24H: $'+str(millify(dexguru_data['volume24hUSD'], precision=2))+'```',end='                                                           ')


supply_temp=requests.get(url=supply,headers=headers)
supply=json.loads(supply_temp.text)
print('```'+'Max Total Supply: '+str(millify((web3.fromWei(int(supply['result']), 'ether')), precision=3))+'```',end='                                      ')



bashCmd = ["sh","bpol-holders.sh"]
process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
output, error = process.communicate()
lines = output.decode('utf-8').splitlines()
print(lines[0])
