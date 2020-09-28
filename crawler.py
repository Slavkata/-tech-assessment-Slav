from datetime import datetime
import requests
import re
from time import sleep

def request_page(url):
    response = requests.get(url).text

    label = re.findall('<td bgcolor=".+" class="cell">[\w&;"></=\s]+</td>', response)[:18]
    append = [re.search('<span class="tiny">(\w+)</span>', l).group(1) for l in label]

    label = [re.search('(\d+)&thinsp;', l).group(1) for l in label]
    for i in range(0, len(label)):
        label[i] += append[i]

    temp = re.findall('<span class="temp">(\d+)</span>', response)[:18]
    
    res = [{'time': label[i], 'temp': temp[i]} for i in range(len(label))]
    for item in res:
        requests.post(url='http://localhost:5000/weather/', data=item)

    return res


