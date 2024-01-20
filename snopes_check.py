from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import requests
import re

snopes_url = "https://www.snopes.com/search/"

def query_snopes(query):
    req = requests.get(snopes_url + query)
    soup = BeautifulSoup(req.text, 'lxml')
    selection = soup.select('.article_wrapper')

    articles = []

    for article in selection:
        
        title = article.select('.article_title')[0]
        
        #TODO: fix byline \n
        byline = article.select('.article_byline')[0]

        link_wrapper = article.select('.outer_article_link_wrapper')[0]
        link = re.match(r'log_search\(\'click\',\'(.+)\'', link_wrapper['onclick'])

        articles.append({'title': title.text, 'byline': byline.text, 'link': 'https://snopes.com/' + link.group(1)})
    
    return articles



if __name__ == '__main__':

    result = query_snopes("shoes")

    print(result)

