import requests

response = requests.get('http://localhost:5000/api/exemplo')
print(response.json())  # Saída: {'mensagem': 'Esta é uma resposta da API'}
