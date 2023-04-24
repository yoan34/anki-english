import requests
import json

from utils.deck import create_deck, get_decks_names
from utils.card import create_card

from data.verbe import all_verbe_deck
from data.nom import all_deck_nom
from data.temps import all_deck_temps
from data.adjectif import all_deck_mixte_adj_adverb
from data.adverbe import all_adverbes
from data.preposition import all_preposision_deck



from data.lessons.condition import all_condition_decks
from data.lessons.phrase_verbal import all_phrase_verbal_decks
from data.lessons.B2.lessons_b2 import all_B2_lessons



from data.friends.saison1 import all_deck_friends_saison1




packs = all_verbe_deck + all_deck_nom + all_deck_temps + all_deck_mixte_adj_adverb \
      + all_adverbes + all_preposision_deck

lessons_packs = all_condition_decks + all_phrase_verbal_decks
lessons_levels_packs = all_B2_lessons

friends_packs = all_deck_friends_saison1

decknames = get_decks_names()
    
for pack in packs + lessons_packs + friends_packs + lessons_levels_packs:
    if pack['deck'] in decknames:
        print(f"deckname: {pack['deck']} already exist.")
    else:
        create_deck(pack['deck'])
        for card in pack['reversed_cards']:
            create_card(pack['deck'], 'Basic (and reversed card)', card[0], card[1])
        for card in pack['basic_cards']:
            create_card(pack['deck'], 'Basic', card[0], card[1])


            

