    # payload = {'action': 'createDeck', 'version': 6, 'params': {'deck': deck_name}}
    # response = requests.post(url, headers=headers, data=json.dumps(payload))
    # print(response.json())
    
import requests
import json

url = 'http://127.0.0.1:8765'
headers = {'Content-Type': 'application/json'}

def createDeck(name):
    payload = {'action': 'createDeck', 'version': 6, 'params': {'deck': name}}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print(f"Le paquet de carte '{name}' à bien été crée.")
    else:
        print(f"[ERROR] Le paquet de carte '{name}' n'as pas été crée.")
    