from flask import Flask

app = Flask(__name__)

@app.route('/')
def storefront():
    return 'Welcome to clarusshop!'

@app.route('/account')
def account():
    return 'This is your account.'

@app.route('/inventory')
def inventory():
    return 'This is inventory service'

@app.route('/shipping')
def shipping():
    return 'This is shipping service'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)