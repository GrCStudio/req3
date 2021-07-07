from datetime import datetime, timedelta
from pprint import pprint
import requests


def getdata():
    datenow = datetime.now()
    before_yesterday = datetime.now() - timedelta(2)
    end_date = datenow.strftime("%Y-%m-%d")
    begin_date = before_yesterday.strftime("%Y-%m-%d")
    return({'fromdate': begin_date, 'todate': end_date})


def get_python_news():
    url = 'http://api.stackexchange.com/docs/articles'
    params = {"order": "desc", "sort": "activity", "tagged": "Python", "filter": "default", "site": "stackoverflow"}
    params.update(getdata())
    response = requests.get(url, params=params)
    print(response.url)
    pprint(response.text)
    pprint(response.json())


get_python_news()

#https://api.stackexchange.com/docs/articles#
# fromdate=2021-07-05&todate=2021-07-07
# &order=desc&sort=activity&tagged=Python&filter=default&site=stackoverflow