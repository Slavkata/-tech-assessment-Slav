from datetime import datetime
import requests
import re
from time import sleep

def request_page(url):
    response = requests.get(url).text

    label = re.findall(r'<td bgcolor=".+" class="cell">[\w&;"></=\s]+</td>', response)[:18]
    append = [re.search(r'<span class="tiny">(\w+)</span>', l).group(1) for l in label]

    label = [re.search(r'(\d+)&thinsp;', l).group(1) for l in label]

    label = [label[0] + append[0] for i in range(0, len(label))]

    for i in range(0, len(label)):
        label[i] += append[i]

    temp = re.findall(r'<span class="temp">(\d+)</span>', response)[:18]
    
    res = [{'time': label[i], 'temp': temp[i]} for i in range(len(label))]

    for item in res:
        print(item)
        requests.post(url='http://localhost:5000/weather/', data=item)

    return res


