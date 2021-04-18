from flask import Flask

app = Flask(__name__)

@app.route('/')
def shipping():
    return '<h1>THIS IS SHIPPING SERVICE</h1>'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)