from flask import Flask
import requests as r

app = Flask(__name__)

@app.route('/')
def get_joke():
    response = r.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        print(joke['setup'])
        print(joke['punchline'])
    else:
        print("Failed to fetch joke")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)