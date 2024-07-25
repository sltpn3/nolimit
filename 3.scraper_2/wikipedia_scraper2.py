from bs4 import BeautifulSoup
from datetime import datetime
import argparse
import requests
import json
import os


def scrape_wikipedia(url: str):
    # scrapped_url.append(url)
    print('scraping ' + url)
    pagename = url.split('?')[0].split('/')[-1]
    if os.path.isfile("{}/result-{}.json".format(os.path.abspath(os.getcwd()), pagename)):
        return
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features='html.parser')
    title = soup.find('h1', {'id': 'firstHeading'}).text

    for caption in soup.find_all("figcaption"):
        caption.decompose()

    content_soup = soup.find('div', {'id': 'bodyContent'})
    result = {'title': title,
              'content': content_soup.text}

    result['relateds'] = []
    relateds = soup.find('div', {'class': 'div-col'})
    if relateds:
        for r in relateds.ul.find_all('li'):
            result['relateds'].append({
                'title': r.a['title'],
                'url': 'https://en.wikipedia.org'+r.a['href']})
    with open("{}/result-{}.json".format(os.path.abspath(os.getcwd()), pagename), 'w') as f:
        f.write(json.dumps(result, indent=4))
    for r in result['relateds']:
        scrape_wikipedia(r['url'])


if __name__ == '__main__':
    scrape_wikipedia('https://en.wikipedia.org/wiki/Proxy_server')
