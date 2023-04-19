import requests
import json

basicModel = 'Basic'
reversedModel = 'Basic (and reversed card)'

url = 'http://127.0.0.1:8765'
headers = {'Content-Type': 'application/json'}


def create_card(deckname, model, front, back):
    note = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deckname,
                "modelName": model,
                "fields": {
                    "Front": front,
                    "Back": back,
                },
            }
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(note))
    r = response.json()
    if r['error']:
        print(f"front: {front} --> {r['error']}")
    else:
        pass
        # print(f"Card Create. {front}")
    

if __name__ == "__main__":
    cards = [
        {"deck": "english::nom::animaux", "model": basicModel,}
    ]
    create_card("english::nom::animaux", reversedModel, "une maison bleu", "a blue house")