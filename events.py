#!/usr/bin/python3
import requests
import json
import pprint

#Script to automaically update events in present.json
# Change the access token and mention the number of events

access_token=input("Enter the access token\n")
n=int(input("Enter the number of events to fetch\n"))
url = 'https://graph.facebook.com/v2.8/' + 'techNIEks/events' \
+ '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
+ '&access_token='+access_token
json1_str = requests.get(url)
json1_data = json.loads(json1_str.text)["data"]
e1 = json1_data[0:n]
with open('present.json', 'w') as p:
    json.dump(e1, p)
pprint.pprint(e1)
