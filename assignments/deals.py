import requests
import json

# Shuffle the deck - get the deck id
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)

print(json.dumps(response.json(), indent=2))

# 'deck_id': 'ebn1y89scli4'
deck_id = response.json()['deck_id']
#cards = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
#deal_1 = requests.get(cards)
#data = deal_1.json()
#print(json.dumps(data, indent=2))