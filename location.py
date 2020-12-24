import requests

res = requests.get('https://ipinfo.io/')
# the above function takes information of your isp and grabs its information
data=res.json()

city = data['city']
location  = data['loc'].split(',')
latitude = location[0]
longitude = location[1]

print('latitude : ',latitude)
print('longitude : ',longitude)
print('city : ',city)
