import requests
import sys
from flask import Flask
app = Flask(__name__)

def change_all_domains(text, domain):
    return text.replace(domain, 'href="http://127.0.0.1:5000/')

WEBSITE='https://www.serialeonline.pl/'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(path)
    print(WEBSITE)
    #r = requests.get(WEBSITE + path, verify=False)
    r = requests.get(WEBSITE + path)
    return change_all_domains(r.text, 'href="' + WEBSITE)

if __name__=='__main__':
    app.run(host='127.0.0.1', port=5000)
