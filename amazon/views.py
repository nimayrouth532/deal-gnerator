from django.shortcuts import render, HttpResponse

def amazon(request):
    return render(request, "amazon.html")

def nimaydeals(request):
    import random
    import requests
    from bs4 import BeautifulSoup as bs
    amazon_url = request.POST['amazon_url']
    your_name = request.POST['your_name']
        #This is a bowser user-agent list user-agent's are listed here as string
    browser_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1', 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996', 'Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10', 'Opera/9.80 (J2ME/MIDP; Opera Mini/5.1.21214/28.2725; U; ru) Presto/2.8.119 Version/11.10', 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53', 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0', 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4', 'Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30', 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP', 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP', 'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0.3', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Microsoft; Lumia 950)', 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977', 'Mozilla/5.0 (BB10; Kbd) AppleWebKit/537.35+ (KHTML, like Gecko) Version/10.3.3.2205 Mobile Safari/537.35+', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:59.0) Gecko/20100101 Firefox/59.0']
    #This is a bowser referer stored in list
    ref = ['https://www.amazon.com.br/', 'https://en.wikipedia.org/wiki/Lady_Gaga', 'http://www.tutorsinindia.com/', 'https://bel-india.com/', 'https://brandservices.amazon.com/', 'https://moz.com/top500', 'https://amazon-presse.de/', 'https://insider.razer.com/index.php?threads/which-mouse-should-i-get.49833/', 'https://www.iamin.in/', 'https://www.audible.in/', 'https://play.google.com/store/apps/details?id=in.amazon.mShop.android.shopping&hl=en_US', 'https://www.aboutamazon.in/']
    a = random.choice(browser_agent) #random choice function to pick a random users agent every time the code runs
    b = random.choice(ref)
    headers = {
        'user-agent': a,
        'referer': b
    }
    a = requests.get(amazon_url, headers=headers, params={
                "api_key": "NPUVAPJM6F1X64JC1Q6WWBBPHLRM6PUK21SBHHGO5KY2M85M8YC3PAEJNKJ9N84P977IS3J98CKUE2YE", #This is proxy api from scrapingbee.com
                "url": amazon_url,
                "premium_proxy": "true", 
                "country_code":"in",
            },
            )
    offer = amazon_url+"&tag=mandibabu-21"
    a = a.content
    soup = bs(a, 'lxml')
    b = soup.find('h1') #This will print the Title  from amazon
    b = b.text
    b = b.strip("\n")
    c = soup.find('span', attrs={'class': 'buyingPrice'}).text
    # c = c.split(',')
    # c = ''.join(c)
    # c = c.text #This will print the price from amazon
    context = {
        'product_title': b,
        'product_price': c,
        'your_name': your_name,
        'random_word': random.choice(["Latest offer from Amazon", "New Loot offer from Amazon", "Bumper Offer from Amazon", "Loot Now Offer from Amazon"]),
        'offer': offer,
    }
    return render(request, "amazon-deals.html", context)