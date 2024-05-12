from flask import Flask, render_template, request, session, Response
from captcha.image import ImageCaptcha
import random
import io

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Gerando randomicamente os caracteres da imagem CAPTCHA
def generate_captcha_text():
    captcha_text = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=4))
    return captcha_text

# Gerando e mostrando a imagem CAPTCHA
@app.route('/captcha')
def generate_captcha():
    captcha_text = generate_captcha_text()
    image = ImageCaptcha(width=500, height=250)
    data = image.generate(captcha_text)
    image_data = io.BytesIO(data.getvalue())
    session['captcha_text'] = captcha_text
    return Response(image_data, mimetype='image/png')

# Página com o desafio do CAPTCHA
@app.route('/')
def home():
    captcha_image_url = "/captcha"
    return render_template('home.html', captcha_image_url=captcha_image_url)

# Validando o que foi digitado
@app.route('/validate', methods=['POST'])
def validate_captcha():
    user_input = request.form.get('captcha_input')
    captcha_text = session.get('captcha_text')
    success_message = None
    error_message = None
    if user_input.lower() == captcha_text.lower():
        success_message = "Validacao realizada con sucesso "
    else:
        error_message = "Caracteres digitados sao INVALIDOS"

    return render_template('home.html', captcha_image_url="/captcha", success_message=success_message, error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True)
