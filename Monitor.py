from lxml import html
import requests
import time
import smtplib

url = 'https://www.pccasegear.com/category/193_1901/graphics-cards/radeon-rx-vega-56'






while True:
    response = requests.get(url)
    site = html.fromstring(response.content)
    price = site.xpath('//h3[@class]/text()')
    print(price)
    """UNCOMMENT AND INPUT EMAIL AND STUFF"""
    #msg = 'Subject: Your Bot here. It looks like the price of the vega 56 on PCCG dropped below $620 aud'
    #fromaddr = ''
    #toaddrs = ''
    #Uncomment and replace things
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.starttls()
    #server.login("YOUR_EMAIL_ADDRESS", "YOUR_PASSWORD")
    for n in price:
        n = int(n.replace("$", ""))
        if n < 620:
            #server.sendmail(fromaddr, toaddrs, msg)
            print("Price goal has been met")
            break
        else:
            print("Wel Nothing to report Yet")
            time.sleep(60)
            continue
