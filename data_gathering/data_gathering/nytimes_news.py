import sys

sys.path.append('pynyt-master/pynyt')
from pynyt import NYTArticleAPIObject
miner = NYTArticleAPIObject('6e3bd9111dfc4fa48eab5b8709222d05')
                           
results = miner.query(q = 'Federal Reserve',
                            begin_date = 20170101,
                            end_date = 20180101,
                            facet_field = ['source', 
                                           'day_of_week'],
                            facet_filter = True,
                            page=1
                            )
for i in results[0]['response']['docs']:
    print(i['snippet'])