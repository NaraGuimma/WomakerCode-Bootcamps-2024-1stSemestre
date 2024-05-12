from flask import Flask

app = Flask(__name__)

@app.route('/api/exemplo', methods=['GET'])
def exemplo():
    return {'mensagem': 'Esta é uma resposta da API'}

if __name__ == '__main__':
    app.run(debug=True, port=5555)