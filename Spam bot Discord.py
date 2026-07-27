import requests 
import time 
payload = {
       'content' : "Enter your message here"
}

header = {
     "authorization" : 'Enter your bot token here' 
}
for i in range (1000) : 
    time.sleep(30)
    r = requests.post('Enter your channel ID here', data=payload, headers=header)