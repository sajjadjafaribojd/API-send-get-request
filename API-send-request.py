# importing the requests library 
import requests 
import json

URL ="http://5.9.6.3./api/v1/suspend"
Aheaders = {'token': '586524652kst',"Content-Type":"application/json"}
PARAMS = {'domainName':'prdevops.ir','suspend':'0'} 

r = requests.get(url = URL, params = PARAMS,headers=Aheaders) 
#data = r.json() 
print(r.text)