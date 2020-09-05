import json
import urllib.request

api_key= 'i96cKLpErcFt1G98wiRBbggUNbheOnQK'
url= 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=indigo&api-key=i96cKLpErcFt1G98wiRBbggUNbheOnQK'

url_list=[]

data= json.load(urllib.request.urlopen(url))

for item in data['response']['docs']:
        print("URL is: \n",item['web_url'])
        url_list.append(item['web_url'])
