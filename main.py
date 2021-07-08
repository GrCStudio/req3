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
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {"order": "desc", "sort": "activity", "tagged": "python", "filter": "default", "site": "stackoverflow"}
    params.update(getdata())
    response = requests.get(url, params=params)
    print(response.url)
    data_json = response.json()
    my_list = []
    for i in range(len(data_json['items'])):
        my_list.append( data_json['items'][i]['title'])
    return(my_list)


pprint(get_python_news())

#https://api.stackexchange.com/docs/articles#
# fromdate=2021-07-05&todate=2021-07-07
# &order=desc&sort=activity&tagged=Python&filter=default&site=stackoverflow