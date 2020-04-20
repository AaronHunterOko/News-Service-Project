from newsapi import NewsApiClient
import requests
import random
api_key='de1b57db735e4ea7be566e68e953d86d'


newsapi = NewsApiClient(api_key='de1b57db735e4ea7be566e68e953d86d')



def addArticle(keyword):
    data = newsapi.get_everything(q=keyword,language='en', from_param='2020-04-17')
    results = []

    articles = data["articles"]
    
    for art in articles:
        results.append(art["url"])
        
    
    return random.choice(results)







