import requests
import json

url = 'https://graph.facebook.com/v2.12/720663717966776?fields=photos.fields(source).limit(100)&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
json1_str = requests.get(url)
jdata = json.loads(json1_str.text)["photos"]
data = jdata["data"]
with open('images.json') as f:
        old_data = json.load(f)
old_id=old_data[0]["id"]
if data[0]["id"]>old_id:
	data=list(filter(lambda x: x["id"]>old_id, data))
	data.extend(old_data)
	f=open('images.json',"w")
	json.dump(data,f)
	f.close()