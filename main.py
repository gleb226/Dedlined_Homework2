from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
import time

client = MongoClient('mongodb+srv://<Медвєдев Глєб>:<07072010Hm!>@<https://cloud.mongodb.com/v2/648da4b663cf1605b667b710#/clusters>/test?retryWrites=true&w=majority')
db = client['weatherdb']
collection = db['weather']

while True:
    response = requests.get('https://ua.sinoptik.ua/погода-ужгород')
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature = soup.find('span', class_='p1').text

    current_datetime = time.strftime('%Y-%m-%d %H:%M:%S')

    document = {'datetime': current_datetime, 'temperature': temperature}
    collection.insert_one(document)

    time.sleep(30 * 60)
