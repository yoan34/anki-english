    # payload = {'action': 'createDeck', 'version': 6, 'params': {'deck': deck_name}}
    # response = requests.post(url, headers=headers, data=json.dumps(payload))
    # print(response.json())
    
import requests
import json

url = 'http://127.0.0.1:8765'
headers = {'Content-Type': 'application/json'}


def create_all_decks():
    verbes = ['verbe', 'verbe::action', 'verbe::etat', 'verbe::modal']
    temps = [
        'temps',
        'temps::forme_simple', 'temps::forme_simple::past', 'temps::forme_simple::present', 'temps::forme_simple::futur',
        'temps::forme_continue', 'temps::forme_continue::past', 'temps::forme_continue::present', 'temps::forme_continue::futur',
        'temps::forme_perfect', 'temps::forme_perfect::past', 'temps::forme_perfect::present', 'temps::forme_perfect::futur',
        'temps::exercice'
    ]
    noms = ['nom', 'nom::animaux', 'nom::plantes', 'nom::vehicules', 'nom::professions', 'nom::batiments',
            'nom::famille', 'nom::nourriture', 'nom::maison']
    # adjectifs = ['adjectif', 'adjectif::qualificatif', 'adjectif::demonstratif', 'adjectif::']
    adverbes = ['adverbe', 'adverbe::maniere', 'adverbe::frequence', 'adverbe::degre']
    
    all = ['english'] + verbes + temps + noms + adverbes
    for name in all:
        createDeck(f"{'english::' if name != 'english' else ''}{name}")
        
        
def create_deck(name):
    payload = {'action': 'createDeck', 'version': 6, 'params': {'deck': name}}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print(f"Le paquet de carte '{name}' à bien été crée.")
    else:
        print(f"[ERROR] Le paquet de carte '{name}' n'as pas été crée.")
        

def get_decks_names():
    payload = {"action": "deckNames", "version": 6}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['result']
    
    
    
if __name__ == "__main__":
    r = get_decks_names()
    for name in r:
        print(name)
    