#Caso queira baixar e utilizar o projeto, acesse o site da globalgiving API e insira sua chave privada nessa variável
import requests

API_KEY = 'your_key'

headers = {
    'accept': 'application/json',
    'content-Type': 'application/json'
}

def make_request(url):
    response = requests.get(url+'?api_key='+API_KEY, headers=headers)
    return response.json()

