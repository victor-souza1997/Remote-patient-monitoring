import requests
import json


def load_array_points():
    cnt = get_temperature_db()
    array = []
    for e in cnt:
        print(e['sensor'])
        value = e['sensor'].values()
        array.append(float([i for i in value][0]))
        print(array)
    return array


def get_temperature_db():
    cnt = requests.get(
        'https://us-east-1.aws.webhooks.mongodb-realm.com/api/client/v2.0/app/temperature_analysis-gjbaa/service/get_temperature/incoming_webhook/get_temperature?db=iot&collection=readings')
    return json.loads(cnt.content)
