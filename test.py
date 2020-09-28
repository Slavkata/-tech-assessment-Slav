from datetime import datetime
import requests
import re

def request_page():
    url = 'https://www.weather-forecast.com/weather-stations/Eindhoven-Airport'

    response = requests.get(url).text
    label = re.findall('<td bgcolor=".+" class="cell">[\w&;"></=\s]+</td>', response)[:18]
    append = [re.search('<span class="tiny">(\w+)</span>', l).group(1) for l in label]
    label = [re.search('(\d+)&thinsp;', l).group(1) for l in label]
    for i in range(0, len(label)):
        label[i] += append[i]

    temp = re.findall('<span class="temp">(\d+)</span>', response)[:18]
    
    res = {label[i]: temp[i] for i in range(len(label))} 
    print(res)


if __name__ == '__main__':
    request_page()