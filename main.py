import requests
response_jokes = requests.get('https://api.chucknorris.io/jokes/random')
print(response_jokes.json()['value'])