from bs4 import BeautifulSoup
import requests
import time
import smtplib

url = 'https://www.pccasegear.com/category/193_1901/graphics-cards/radeon-rx-vega-56'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

soup = soup.prettify()
print(soup)

price = soup.find_all('h3', class_ = 'product-price no-margin' )

while True:
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    soup = soup.prettify()
    price = soup.find_all('h3', class_ = 'product-price no-margin' )
    msg = 'Subject: Your Bot here. It looks like the price of the vega 56 on PCCG dropped below $620 aud'
    fromaddr = ''
    toaddrs = ''

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")
    for n in price:
        if n < 620:
            server.sendmail(fromaddr, toaddrs, msg)
            print("Price goal has been met")
            break
