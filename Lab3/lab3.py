def mul_by_num(num):
    num1 = lambda num:num*num
    return num1(num)

x = mul_by_num(5)
y = mul_by_num(2)
print(x)
print(y)
x = lambda x:x*x
print(x(3))

#Q2

from functools import reduce
n=10
fibs = reduce(lambda x, _:x+[x[-1]+x[-2]], [0]*(n-2), [0, 1])
print (fibs)

#Q3.py
from pprint import pprint
import requests

def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+
                  '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
    return res.json();

def print_weather(result,city):
    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))

def main():
    city=input('Enter the city:')
    print()
    try:
      query='q='+city;
      w_data=weather_data(query);
      print_weather(w_data, city)
      print()
    except:
      print('City name not found...' + e)
if __name__=='__main__':
    main()

# %%
# Question 4
import xml.etree.ElementTree as ET
import csv

xmlFile = "/Users/omkartawade/Omkar/DAP/Database-and-Analytics-Programming/Lab3/people.xml"
tree = ET.parse(xmlFile)
root = tree.getroot()

# open a file for writing

csvFile = "/Users/omkartawade/Omkar/DAP/Database-and-Analytics-Programming/Lab3/residentData.csv"

Resident_data = open(csvFile, 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []

count = 0
for member in root.findall('Resident'):
    resident = []
    address_list = []
    if count == 0:
        name = member.find('Name').tag
        resident_head.append(name)
        PhoneNumber = member.find('PhoneNumber').tag
        resident_head.append(PhoneNumber)
        EmailAddress = member.find('EmailAddress').tag
        resident_head.append(EmailAddress)
        Address = member[3].tag
        resident_head.append(Address)
        csvwriter.writerow(resident_head)
        count = count + 1

    name = member.find('Name').text
    resident.append(name)
    PhoneNumber = member.find('PhoneNumber').text
    resident.append(PhoneNumber)
    EmailAddress = member.find('EmailAddress').text
    resident.append(EmailAddress)
    Address = member[3][0].text
    address_list.append(Address)
    City = member[3][1].text
    address_list.append(City)
    StateCode = member[3][2].text
    address_list.append(StateCode)
    PostalCode = member[3][3].text
    address_list.append(PostalCode)
    resident.append(address_list)
    csvwriter.writerow(resident)

Resident_data.close()


