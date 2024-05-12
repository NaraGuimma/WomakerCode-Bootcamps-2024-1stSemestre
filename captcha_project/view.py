from flask import Flask
from flask_recaptcha import ReCaptcha

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)

#or 

# recaptcha = Recaptcha()
# recaptcha.init_app(app)