import requests

response_data = requests.get(
    'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'
)

city_air = response_data.json()
qu_infos = city_air['RealtimeCityAir']['row']
# print(response_data)
# print(city_air)
for quinfo in qu_infos:
    if quinfo['PM10'] < 20:
        print(quinfo['MSRRGN_NM'],quinfo['PM10'])