import requests

proxies = {
 "https": "http://132.255.23.157:3128",
}

token = '972242987:AAEBckYsY4kxn9C362DCCfdNUH8p4NNOsKM'

link = f'https://api.telegram.org/bot{token}'

message = {
    'chat_id': '981105764',
    'text': 'Саламуля'
} 

r = requests.get(f'{link}/sendMessage', proxies=proxies, data = message)

print(r.json())
