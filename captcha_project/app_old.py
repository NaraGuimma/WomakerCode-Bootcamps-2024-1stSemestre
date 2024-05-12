from flask import Flask, render_template, request, session
from flask_wtf.csrf import CSRFProtect
import random
from PIL import Image, ImageDraw, ImageFont
import io
import string
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c505b79147024cb65e1a1420b7473a56'
csrf = CSRFProtect(app)

# Generate random CAPTCHA text
def generate_captcha_text(length=6):
    captcha_chars = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(captcha_chars) for _ in range(length))
    return captcha_text

# Generate CAPTCHA image
def generate_captcha_image(captcha_text):
    image = Image.new('RGB', (200, 100), color = (255, 255, 255))
    d = ImageDraw.Draw(image)
    # font = ImageFont.truetype("arial.ttf", 36)
    font = ImageFont.load_default()
    d.text((10,10), captcha_text, font=font, fill=(0,0,0))
    return image

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['captcha']
        if user_input == session['captcha']:
            return "CAPTCHA validation successful!"
        else:
            return "CAPTCHA validation failed. Please try again."

    captcha_text = generate_captcha_text()
    captcha_image = generate_captcha_image(captcha_text)

    # Store the CAPTCHA text in the session
    session['captcha'] = captcha_text

    # Convert image to byte array
    img_byte_arr = io.BytesIO()
    captcha_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    img_data = base64.b64encode(img_byte_arr).decode('utf-8')

    return render_template('form.html', captcha_image=img_data)


if __name__ == '__main__':
    app.run(debug=True)
