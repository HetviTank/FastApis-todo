from urllib.request import urlopen

# import json
import json

# store the URL in url as
# parameter for urlopen
url = "https://nywwa6iqfmh2jxl3c7zlhm7qya0rrmka.lambda-url.ap-south-1.on.aws/"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data = json.loads(response.read())

# print the json response
# print(data['d']['results'][1]['Material'])
# json_data = []
material_data = []
rate_data = []
checknow = []
lets = 0
andy = ''
gg=[]
for i in data['d']['results']:
    # i["DivisionDesc"] = i["DivisionDesc"].row.low
    material_data.append(i["DivisionDesc"].lower())
    rate_data.append(i["NetValueINR"])
#     for io in checknow:
#         if io==i['DivisionDesc']:
#             lets=1
#     if lets!=1 :
#         gg.append(i['DivisionDesc'].lower())
#     lets=0
# random = set(gg)
# print(random)
print(max(rate_data))
# print(data[i]['material'])
# print(i)


# fruit_price['name'] = fruit_price['name'].str.lower()


# message = 'PYTHON IS FUN'
# print(message.lower())

# for item in json_data:
#     for data_item in item['data']:
#         print data['material'], data_item['value']
