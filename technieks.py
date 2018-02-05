from flask import Flask, g, render_template, request, redirect
import requests
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/events')
def events_all():
    url = 'https://graph.facebook.com/v2.8/' + 'techNIEks/events' \
    + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
    + '&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    print url
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["data"]
    j1 = json1_data[:len(json1_data)]
    return render_template('events.html',events1=j1, title="All Events")

# Here goes the code for the rest of the pages


@app.errorhandler(404)
def page_not_found(e):
    return "error"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
