import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com/Sony-Mirrorless-Digitial-3-0-Inch-16-50mm/dp/B00I8BICB2'

headers = {"User-Agent": 'https://www.youtube.com/watch?v=Bg9r_yLk7VY'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourpice").get_text()

    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_email()



    print(converted_price)
    print(title.strip())


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ed.magician@gmail.com','nddssecksosss')
    subject = 'price fell down!'
    body = 'check the amazon link https://www.amazon.com/Sony-Mirrorless-Digitial-3-0-Inch-16-50mm/dp/B00I8BICB2'
    
