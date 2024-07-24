from bs4 import BeautifulSoup
from datetime import datetime
import argparse
import requests
import json
import os


def scrape_wikipedia(q: str, save_path: str = os.path.abspath(os.getcwd()), proxy: str = None):
    results = []
    url = "https://en.wikipedia.org/w/index.php?limit=20&offset=0&profile=default&search={}&title=Special:Search&ns0=1"
    resp = requests.get(url.format(q.replace(' ', '+')))
    soup = BeautifulSoup(resp.content, features='html.parser')
    search_results = soup.find_all("li", {"class": "mw-search-result"})
    for result in search_results:
        created_at_text = result.find(
            'div', {"class": "mw-search-result-data"}).text.split('-')[1].strip()
        s = {'title': result.a['title'],
             'link': "https://en.wikipedia.org"+result.a['href'],
             'content': result.find('div', {"class": "searchresult"}).text,
             'createdAt': datetime.strptime(created_at_text, '%H:%M, %d %B %Y').strftime('%Y-%m-%dT%H:%M:%SZ'),
             'category': None}
        results.append(s)
    i = 1
    while os.path.exists("{}/result-{}.json".format(save_path, i)):
        i += 1

    with open("{}/result-{}.json".format(save_path, i), 'w') as f:
        f.write(json.dumps(results, indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wikipedia Scrapers',
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-q', '--query', metavar='', type=str,
                        help='Search Query')
    args = parser.parse_args()
    scrape_wikipedia(args.query)
