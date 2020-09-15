from django.shortcuts import render, HttpResponse

def flip(request):
    return render(request, "flipkart.html")

def deals(request):
    import random
    import requests as req
    from bs4 import BeautifulSoup as bs
    flip_name = request.POST['flip_name']
    flipkart_url = request.POST['flipkart_url']
    url = req.get(flipkart_url)
    # url = url.content
    url = url.content
    soup = bs(url, "lxml")
    a = soup.find_all("span", class_="_35KyD6")#This one is for product Title
    a = a[0]
    a = a.text
    b = soup.find("div", attrs = {'class': "_1vC4OE _3qQ9m1"}).text #This will print the product price
    b = b[1:]
    context = {
        "a": a,
        "b": b,
        "flip_name": flip_name,
        "flipkart_url": flipkart_url,
    }
    return render(request, "flipkart-deals.html",context)