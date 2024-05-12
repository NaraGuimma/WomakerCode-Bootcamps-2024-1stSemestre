from flask import Flask, render_template
import requests
from pprint import pprint
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/nara")
    estatistica = response.json()
    pprint(estatistica)
    # return 'Hello World'
    return render_template('nomes.html', dados=estatistica)


if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'test_debug'
    toolbar = DebugToolbarExtension(app)
    app.run(debug=True)
