#
#
# Author: Stephen Hilt
# Usage: Place this in a folder called scripts on hassio
#   Then we will update the configuration.yaml 
#
import requests 
import datetime
import json
import time 

#Follow the instructions here to get this: https://www.npmjs.com/package/homebridge-petkit-feeder-mini
cookie = 'YOUR COOKIE HERE'

#This is my headers, youc an change your host based on what your region shows as the above example for homebridge
headers = {'Host': 'api.petkt.com',
'X-Client': 'ios(14.7.1;iPhone11,2)', 
'X-Session': '%s' % cookie, 
'Accept': '*/*',
'X-Timezone': '-4.0',
'F-Session': '%s' % cookie,
'Accept-Language': 'en-US;q=1',
'X-Api-Version': '7.26.2',
'User-Agent': 'PETKIT/7.26.2 (iPhone; iOS 14.7.1; Scale/3.00)', 
'X-TimezoneId': 'America/New_York', # you might need to change this timezone to match yours
'X-Img-Version': '1',
'X-Locale': 'en_US' }

# change the host as needed
host = 'http://api.petkt.com/latest'
# needed to query to get the ID, but also you can't just do the second step with out this roster command
roster = '/discovery/device_roster'
# some of the things I will be adding and playing with but the code can grab them as needed 
device_detail = 'device_detail'
feed = 'feed'
devicestate = 'devicestate'
dailyfeeds = 'dailyfeeds'
resetDesiccant = 'desiccant_reset'
# create the first request 
res = requests.post('%s%s' % (host,roster) , headers=headers)
res_json = json.loads(res.text)
# this will be used as the ID for the next one, I have only one device so this was easy, if you have more we need to change this
device_id = res_json['result']['devices'][0]['data']['id']
device_name = res_json['result']['devices'][0]['data']['name']
device_type = res_json['result']['devices'][0]['type']
# This will get the rest of the information
#
url = '%s/%s/%s?id=%s' % (host,device_type.lower(),device_detail,device_id)
data='id=%s' % device_id
res = requests.post(url, data=data, headers=headers)
res_json = json.loads(res.text)
desiccantDaysLeft = res_json['result']['state']['desiccantLeftDays']
foodFill = res_json['result']['state']['food']
currentlyFeeding = res_json['result']['state']['feeding']

# Now put the json file on disk to ensure things worked, also incase we need it for something else
# Remove if you don't care about this part 
f = open("/config/scripts/petkit.json", "w+")
f.write(res.text)
f.close()
# print out the json
print(res.text) #res_json

