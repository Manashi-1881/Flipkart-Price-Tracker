import requests
from bs4 import BeautifulSoup
import smtplib

url = "https://www.flipkart.com/apple-iphone-11-black-128-gb/p/itm06bac28995200?pid=MOBFKCTSYAPWYFJ5&lid=LSTMOBFKCTSYAPWYFJ580EM6T&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=f19221f1-9cc5-47bd-b6a9-d4fde4232afa.MOBFKCTSYAPWYFJ5.SEARCH&ppt=sp&ppn=sp&ssid=q0r9jggj8w0000001581859703916&qH=f6cdfdaa9f3c23f3"

browser = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def send_mail_to_me(mytitle):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('simmily.manashi@gmail.com','imiagyljsbhcjrxj')

    subject = 'Price Fail Down for '+mytitle
    content = 'Check Out the Link Here https://www.flipkart.com/apple-iphone-11-black-128-gb/p/itm06bac28995200?pid=MOBFKCTSYAPWYFJ5&lid=LSTMOBFKCTSYAPWYFJ580EM6T&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=f19221f1-9cc5-47bd-b6a9-d4fde4232afa.MOBFKCTSYAPWYFJ5.SEARCH&ppt=sp&ppn=sp&ssid=q0r9jggj8w0000001581859703916&qH=f6cdfdaa9f3c23f3'

    msg = f"Subject: {subject}\n\n{content}"

    server.sendmail('simmily.manashi@gmail.com','newrainbowad@gmail.com',msg)

    print('HEY EMAIL HAS BEEN SENT !!')

    server.quit()

def checkPrice():

    budget = 50000
    page = requests.get(url, headers=browser)
    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find_all('span', {'class' : '_35KyD6'})
    price = soup.find_all('div', {'class' : '_1vC4OE _3qQ9m1'})


    mytitle = title[0].text
    myprice = price[0].text

    myprice=myprice[1:]
    li = [x for x in myprice.split(',')]
    myprice = li[0]+li[1]
    convert_price = int(myprice)

    if convert_price <= budget:
        send_mail_to_me(mytitle)




checkPrice()