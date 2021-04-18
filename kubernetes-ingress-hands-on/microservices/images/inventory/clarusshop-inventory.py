from flask import Flask

app = Flask(__name__)

@app.route('/')
def inventory():
    return '<h1>THIS IS INVENTORY SERVICE</h1>'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)