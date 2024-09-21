import requests
from bs4 import BeautifulSoup
import pprint

# where we will be getting our data
response = requests.get('https://news.ycombinator.com/news')
# convert the text we get into html , by parsing it to html because it also parses into xml
# from the response we can get the body, body.content for the contents inside the body
content = BeautifulSoup(response.text, 'html.parser')

links = content.select('.titleline')
subtext = content.select('.subtext')


def create_custom_news(links, subtext):
    news = []
    # get the text contents in the title
    for index, item in enumerate(links):
        anchor_tag = item.find('a')
        title = links[index].getText()
        votes = subtext[index].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            href = anchor_tag.get('href')
            news.append({'title': title, 'href': href, 'votes': points})
    return news


pprint.pprint(create_custom_news(links, subtext))
