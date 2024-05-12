from flask import Flask, render_template, request
import requests

app = Flask(__name__)

RECAPTCHA_SITE_KEY = 'RECAPTCHA_SITE_KEY'
RECAPTCHA_SECRET_KEY = 'RECAPTCHA_SECRET_KEY'

@app.route('/')
def index():
    return render_template('index.html', site_key=RECAPTCHA_SITE_KEY)

@app.route('/submit', methods=['POST'])
def submit():
    recaptcha_response = request.form.get('g-recaptcha-response')
    
    if recaptcha_response:
        payload = {
            'secret': RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        result = response.json()
        
        if result['success']:
            return "reCAPTCHA verification passed. Form submitted successfully!"
        else:
            return "reCAPTCHA verification failed. Please try again."
    else:
        return "reCAPTCHA verification failed. Please complete the reCAPTCHA."

if __name__ == '__main__':
    app.run(debug=True)
