import requests
from bs4 import BeautifulSoup as bs
url = input("Enter Url: ")
url = requests.get(url)
url = url.content
soup = bs(url, "lxml")
a = soup.find("div", attrs = {"class": "_1vC4OE _3qQ9m1"}).text #This one is for price
b =soup.find("span", attrs = {"class": "_35KyD6"}).text #This one is for product name
a = a[1:]
print(a+b)