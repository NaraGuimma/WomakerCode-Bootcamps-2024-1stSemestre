from flask import Flask, render_template, request
import requests

app = Flask(__name__)

SITE_KEY = "6Lc9ppUpAAAAAF6VD3pZKF1tE2NWoQ5rnr-G2yQx"
SECRET_KEY = "6Lc9ppUpAAAAAAMn1-N2drONVSzi06kW_IpYqDMc"

@app.route('/')
def index():
    return render_template('index.html', site_key=SITE_KEY)

@app.route("/submit", methods=["POST"])
def submit():
    recaptcha_response = request.form.get("g-recaptcha-response")

    if recaptcha_response:
        payload = {
            'secret': SECRET_KEY,
            'response': recaptcha_response
        }
        response = requests.post(url = 'https://www.google.com/recaptcha/api/siteverify', data= payload)
        result = response.json()
        print(result)

        if result['success']:
            mensagem = 'Validado.'
            status = 'success'
        else:
            mensagem = 'Nao validado.'
            status = 'error'     
    else:
            mensagem = 'Falha na verificacao.'
            status = 'error'      

    print(mensagem, status)
    return render_template('index.html', site_key=SITE_KEY, mensagem=mensagem, status=status)          

if __name__ == '__main__':
    app.run(debug=True, port=8085)