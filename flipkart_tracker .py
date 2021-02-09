import requests
from bs4 import BeautifulSoup
from email_alert import alert_system
from threading import Timer

URL = 'https://www.flipkart.com/boat-stone-190f-5-w-bluetooth-speaker/p/itm56d7dd8c16d6c?pid=ACCFZ59AK8NNGZA5&lid=LSTACCFZ59AK8NNGZA5QYVKUD&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=1367dbcf-b5ea-4372-a903-c6abd83f78dd.ACCFZ59AK8NNGZA5.SEARCH&ppt=sp&ppn=sp&ssid=6zhoavxk9s0000001610085926270&qH=d75f1e867076fd05'

headers = { 
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip', 
'DNT' : '1', # Do Not Track Request Header 
'Connection' : 'close'
}

set_price = 1000

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_='B_NuCI').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
    price = soup.find(class_='_30jeq3 _16Jk6d').get_text()
    # print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    if float(product_price) <= set_price:
        alert_system(product_title, URL)
        print('sent')
        return
    else:
        print('not sent')
    Timer(60, check_price).start()

check_price()