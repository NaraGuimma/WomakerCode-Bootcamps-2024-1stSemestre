from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Subsctituir com as chaves geradas 
RECAPTCHA_SITE_KEY = '6LcKPZMpAAAAAMoYZBMalwECOMKNyRcUrh_5qfpc'
RECAPTCHA_SECRET_KEY = '6LcKPZMpAAAAADEs-Pxm9ga4zf5scGLPWZwevpaY'

@app.route('/')
def index():
    return render_template('index.html', site_key=RECAPTCHA_SITE_KEY)

@app.route('/submit', methods=['POST'])
def submit():
    recaptcha_response = request.form.get('g-recaptcha-response')
    
    # Validando resposta do reCAPTCHA
    if recaptcha_response:
        payload = {
            'secret': RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
        result = response.json()
        
        if result['success']:
            # reCAPTCHA validado com sucesso
            message = "reCAPTCHA verificacao com sucesso. Formulário enviado com sucesso!"
            status = "success"
        else:
            # reCAPTCHA falhou
            message = "reCAPTCHA verificacao falhou. Por favor tente novamente."
            status = "error"
    else:
        # Se o reCAPTCHA token nao for fornecido
        message = "reCAPTCHA verificacao falhou. Por favor complete o reCAPTCHA."
        status = "error"

    return render_template('index.html', site_key=RECAPTCHA_SITE_KEY, message=message, status=status)

if __name__ == '__main__':
    app.run(debug=True)
