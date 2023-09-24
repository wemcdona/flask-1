from flask import Flask, request, render_template, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension
import requests


def create_app():
    app = Flask(__name__)
    # @app.route('/')
    # def hello_world():
    #     return 'Hello, World!'
    return app
app = create_app()
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES_KEY = "responses"

# Define the API url for currency conversion
API_URL = 'https://api.exchangerate.host/convert?'

# List of valid currency codes
VALID_CURRENCY_CODES = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        amount = request.form.get('amount')


        #Validate currency codes
        if not (from_currency in VALID_CURRENCY_CODES) or not (to_currency in VALID_CURRENCY_CODES):
            return render_template('index.html', error_message='Invalid currency code!')
        
        # Make the API request for currency conversion
        conversion_result = convert_currency(from_currency, to_currency, amount)

        if conversion_result is not None:
            return render_template('index.html', conversion_result=conversion_result)
        else:
            return render_template('index.html', error_message='Currency conversion failed.')
    
    return render_template('index.html')

def is_valid_currency(currency_code):
    return bool(currency_code)


def convert_currency(from_currency, to_currency, amount):
    """Create the API request URL"""
    api_request_url = f'{API_URL}from={from_currency}&to={to_currency}&amount={amount}'

    try:
        # Make the API request
        response = requests.get(api_request_url)
        data = response.json()

        if 'result' in data:
            return data['result']
        
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")

    return None

if __name__ == '__main__':
    app.run(debug=True)