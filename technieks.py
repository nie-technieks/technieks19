from flask import Flask, g, render_template, request, redirect
import requests
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/')
@app.route('/index.html/')
def index():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('technieks18.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key('10pB43SvGbIWX0LEGaRfkYe1XYa_bw-OvlvdUgj-66gQ').sheet1
    sdata = wks.get_all_values()
    return render_template('index.html',data=sdata[1:])


@app.route('/events')
def events_all():
    url = 'https://graph.facebook.com/v2.8/' + 'techNIEks/events' \
    + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
    + '&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    print url
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["data"]
    j1 = json1_data[:len(json1_data)]
    return render_template('events2.html',events1=j1, title="All Events")

@app.route('/events1')
def test_events():
    url = 'https://graph.facebook.com/v2.8/' + 'techNIEks/events' \
    + '?fields=id%2Cname%2Ccover%2Cstart_time%2Cdescription%2Cplace%2Cticket_uri' \
    + '&access_token=1327383467301154%7CYDfQ94wTelbffydG5XrnanHnqu0'
    print url
    json1_str = requests.get(url)
    json1_data = json.loads(json1_str.text)["data"]
    j1 = json1_data[:len(json1_data)]
    return render_template('events1.html',events1=j1, title="All Events")




@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hackathon/')
def hackathon():
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSdy0PTBTJmAklzPThYgb78GlT9QzYI8oPsZ4DF8HjfyKnnTzg/viewform?usp=sf_link')

@app.route('/marathon/')
def marathon():
    return redirect('https://www.payumoney.com/events/#/buyTickets/technieksmarathon18')

@app.route('/youtube/')
def youtube():
    return redirect('https://www.youtube.com/channel/UC0Ky30GAIfdtGccczVNUIqA')


@app.route('/cyclothon/')
def cyclathon():
    return redirect('https://www.payumoney.com/events/#/buyTickets/cyclothon2018')

@app.errorhandler(404)
def page_not_found(e):
    return "error"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
