from ast import arg
import requests
import argparse
from datetime import datetime
import random

# -- RESGATANDO NEWS -- 
API_KEY = 'API KEY'

url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

response = requests.get(url)

data = response.json()

# -- Index da notícia aleatória entre as 10 últimas publicadas -- 
n = random.randint(2,9)

# -- DEFINDO ARGS -- 
parser = argparse.ArgumentParser()
parser.add_argument("-t1", "--PrimeiroTitulo", action="store_true", help="Imprime o título da primeira notícia")
parser.add_argument("-c1", "--PrimeiroCorpo", action="store_true", help="Imprime o corpo da primeira notícia")
parser.add_argument("-i1", "--PrimeiroInfo", action="store_true", help="Imprime informações da primeira notícia")
parser.add_argument("-t2", "--SegundoTitulo", action="store_true", help="Imprime o título da segunda notícia")
parser.add_argument("-c2", "--SegundoCorpo", action="store_true", help="Imprime o corpo da segunda notícia")
parser.add_argument("-i2", "--SegundoInfo", action="store_true", help="Imprime informações da segunda notícia")
parser.add_argument("-tr", "--RandomTitulo", action="store_true", help="Imprime o título de uma notícia aleatória")
parser.add_argument("-cr", "--RandomCorpo", action="store_true", help="Imprime o corpo de uma notícia aleatória")
parser.add_argument("-ir", "--RandomInfo", action="store_true", help="Imprime informações de uma notícia aleatória")
args = parser.parse_args()

if args.PrimeiroTitulo:
    #formatar título das notícias
    news_title = data['articles'][0]['title'].split('-')
    news_title.pop(-1) #remove o veículo de notícia
    news_title = '-'.join(news_title) #une os hifens do título

    print(news_title)
elif args.PrimeiroCorpo:
    news_description = data['articles'][0]['description']

    print(news_description)
elif args.PrimeiroInfo:
    news_vehicle = data['articles'][0]['source']['name']

    #formatando data
    news_date = data['articles'][0]['publishedAt']
    date = datetime.fromisoformat(news_date.replace('Z', '+00:00')).strftime("%d/%m/%Y")

    print(f'{date} - {news_vehicle}')
elif args.SegundoTitulo:
    news_title = data['articles'][1]['title'].split('-')
    news_title.pop(-1) 
    news_title = '-'.join(news_title) 

    print(news_title)
elif args.SegundoCorpo:
    news_description = data['articles'][1]['description']

    print(news_description)
elif args.SegundoInfo:
    news_vehicle = data['articles'][1]['source']['name']
    news_date = data['articles'][1]['publishedAt']
    date = datetime.fromisoformat(news_date.replace('Z', '+00:00')).strftime("%d/%m/%Y")

    print(f'{date} - {news_vehicle}')
elif args.RandomTitulo:
    news_title = data['articles'][n]['title'].split('-')
    news_title.pop(-1) 
    news_title = '-'.join(news_title) 

    print(news_title)
elif args.RandomCorpo:
    news_description = data['articles'][n]['description']

    print(news_description)
elif args.RandomInfo:
    news_vehicle = data['articles'][n]['source']['name']
    news_date = data['articles'][n]['publishedAt']
    date = datetime.fromisoformat(news_date.replace('Z', '+00:00')).strftime("%d/%m/%Y")

    print(f'{date} - {news_vehicle}')
else:
    print("Insira um parâmetro válido")

