import sys
import os

# Add the 'lib' directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

from lib.flask import Flask, request


app = Flask(__name__)

@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')
    return f"Authorization Code: {authorization_code}"

if __name__ == '__main__':
    app.run(port=8080)
