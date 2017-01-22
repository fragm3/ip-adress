from requests import get
from urllib2 import urlopen
import json

ip = get('https://api.ipify.org').text
print 'Public IP address is: {}'.format(ip)

url='http://ipinfo.io/' + ip + '/json'
response = urlopen(url)

data=json.load(response)
city = data['city']
region = data['region']
country = data['country']
location = data['loc']
org = data['org']

print "City : " + city
print "Region : " + region
print "Country : " + country
print "Location : " + location
