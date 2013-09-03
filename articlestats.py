#! /usr/bin/python

""" An article class for handling web based articles and reporting statistics
    about their textual content. """

__appname__ = "Article Class"
__author__ = "Scott G. Allen"
__version__ = "0.0pre0"

import nltk
import requests

class Article(object):
    def __init__(self, url):
        self.url = url
        self.raw_data = ""

    def fetch_article(self, url=None):
        if url is None:
            url = self.url
        response = requests.get(url)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError, err:
            print "Unable to fetch article: {}".format(err)
        self._save_to_file(response)

    def _save_to_file(self, response):
        pass

def main():
    url = "http://www.usatoday.com/story/sports/nfl/broncos/2013/09/02/cornerback-champ-bailey-wants-redemption-against-baltimore-ravens-sprained-foot/2755655/?utm_source=dlvr.it&utm_medium=twitter"
    article = Article(url)
    article.fetch_article()

if __name__ == '__main__':
    main()
