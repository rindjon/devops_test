from flask import Flask
import requests as r

app = Flask(__name__)

@app.route('/')
def get_joke():
    res = r.get('https://api.chucknorris.io/jokes/random')
    json_res = res.json()
    return json_res['value']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)