import requests
import json
import time

url = "https://freegeoip.app/json/"

headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

counter = 1

f = open('<YOUR_IP_LIST>', 'r')
listIP = f.readlines()
for i in listIP:
    realUrl = url+i.strip()
    
    try:
        response = requests.request("GET", realUrl, headers=headers)
        todos = json.loads(response.text)
        print(todos['ip']+" , " +todos['country_name'] + " , "+todos['city'])
        ipAddress = todos['ip']+" , "+todos['country_name'] + " , "+todos['city']
        ipList = open('ipList.txt', 'a')
        ipList.write(ipAddress+'\n')
    except:
        time.sleep(10)
        print("error")
        
    time.sleep(1)
