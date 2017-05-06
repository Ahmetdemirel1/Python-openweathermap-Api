import datetime
import json
import urllib.request
import tkinter
import sys
import os


city = (input("city : "))
user_api = '' #your user api key
unit = 'metric'
api = 'http://api.openweathermap.org/data/2.5/weather?id='
#full_url = api + str(city) + '&mode=json&units=' + unit + '&APPID=' + user_api
full_url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (city, user_api)


url = urllib.request.urlopen(full_url)
output = url.read().decode('utf-8')
raw_api_dict=json.loads(output)
url.close()

def time_converter(time):
    convert_time= datetime.datetime.fromtimestamp(int(time)).strftime('%I:%M:%p')
    return convert_time

data = dict(
    city=raw_api_dict.get('name'),
    country = raw_api_dict.get('sys').get('country'),
    temp = raw_api_dict.get('main').get('temp'),
    temp_max=raw_api_dict.get('main').get('temp_max'),
    temp_min=raw_api_dict.get('main').get('temp_min'),
    sky=raw_api_dict['weather'][0]['main'],
    sunrise=time_converter(raw_api_dict.get('sys').get('sunrise')),
    sunset=time_converter(raw_api_dict.get('sys').get('sunset')),
    wind=raw_api_dict.get('wind').get('speed'),
    dt=time_converter(raw_api_dict.get('dt')),
)

print("________________________________")
print("Weather in: {}, {}:".format(data['city'],data['country']))
print("temp: {} \xb0K, sky:{}".format(data['temp'], data['sky']))
print('Max Temp: {}, Min Temp: {}'.format(data['temp_max'], data['temp_min']))
print('Sunrise at: {}'.format(data['sunrise']))
print('Sunset at: {}'.format(data['sunset']))
