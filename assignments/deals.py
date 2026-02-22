import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
## 'deck_id': 'ebn1y89scli4'
cards = "https://deckofcardsapi.com/api/deck/ebn1y89scli4/draw/?count=2"
deal_1 = requests.get(cards)
data = deal_1.json()
print(json.dumps(data, indent=2))