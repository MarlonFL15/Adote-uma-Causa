#Caso queira baixar e utilizar o projeto, acesse o site da globalgiving API e insira sua chave privada nessa variável
import requests

API_KEY = 'a6137dc5-159c-4355-8a8f-c53bdbe4e9ac'

headers = {
    'accept': 'application/json',
    'content-Type': 'application/json'
}

def make_request(url):
    response = requests.get(url+'?api_key='+API_KEY, headers=headers)
    print(url+'?api_key='+API_KEY)
    return response.json()

