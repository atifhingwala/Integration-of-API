import json
import urllib.request

api_key= '43f82d17e10a4ebeb1633d979887293b'

url= 'http://newsapi.org/v2/everything?apiKey=43f82d17e10a4ebeb1633d979887293b'

def result_based(option):
    api_key= '43f82d17e10a4ebeb1633d979887293b'
    if(option=='1'):
        keyword= input("Enter any keyword: ")
        date_entry = input('Enter a date in YYYY-MM-DD format: ')
        final_url= 'http://newsapi.org/v2/everything?apiKey=' + api_key + '&q=' + keyword + '&from=' + date_entry
    else:
        source= input("Enter the Source: ")
        final_url= 'http://newsapi.org/v2/everything?apiKey=' + api_key + '&sources=' + source
        
    json_obj= urllib.request.urlopen(final_url)
    data= json.load(json_obj)

    for item in data['articles']:
        print(item)

option= input("Result on basis of: 1.Query \t 2.Source :")
result_based(option)
