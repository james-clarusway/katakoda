from flask import Flask

app = Flask(__name__)

@app.route('/')
def storefront():
    return '<h1>WELCOME TO CLARUSSHOP!<h1>'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)