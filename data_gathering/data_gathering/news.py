import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import sys

sys.path.append('../pynyt-master/pynyt')
from pynyt import NYTArticleAPIObject

class News:
    all_news = []
    topic = ""
    bs = ""
    sentiment = 0
    result = {}
    path = ""
    miner = NYTArticleAPIObject('6e3bd9111dfc4fa48eab5b8709222d05')
    
    def __init__(self, topic, path=None):
        self.topic = topic
        self.path = path
        #self.get_markup()
        self.extract_news()
        self.calc_sentiment()
        
    def get_markup(self):
        url = 'https://news.google.com/search?q={}'.format(self.topic)
        resp = requests.get(url, allow_redirects=True)
        src_code = resp.text.encode('ascii', 'replace')
        self.bs = BeautifulSoup(src_code, "html.parser")
        
    def extract_news(self):
	    
        results = self.miner.query(q = self.topic,
                            begin_date = 20180101,
                            end_date = 20180530,
                            facet_field = ['source', 
                                           'day_of_week'],
                            facet_filter = True,
                            page=1
                            )
        for item in results[0]['response']['docs']:
                news = {
                        "text": item['snippet'],
                        "sentiment": self.sentiment(item['snippet'])
				}
                if item is not None:
                    self.all_news.append(news.copy())
        print(self.all_news)
    @staticmethod
    def sentiment(str):
        blob = TextBlob(str)
        return blob.sentiment.polarity
    
    def calc_sentiment(self):
        result = 0
        cnt = 0
        for news in self.all_news:
            alpha = 0
            if news['sentiment'] > 0:
                cnt += 1
                alpha = 1
            elif news['sentiment'] <= 0:
                cnt+=1
            result += alpha
        self.sentiment = result
        self.sentiment = float(result)/cnt

    def get_sentiment(self):
        return round(self.sentiment*100, 2)
    
    def get_news(self):
        return self.all_news
    
    def get_result(self):
        return {
                'news':self.get_news(),
                'sentiment':self.get_sentiment()
                }
        
    def export_json(self):
        import json
        with open('{}/news.json'.format(self.path),'w') as outfile:
            json.dump(self.get_result(), outfile)