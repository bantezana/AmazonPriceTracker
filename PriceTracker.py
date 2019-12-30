import requests
import smtplib
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/MSI-Gaming-RTX-2080-Super/dp/B07VDMGYGZ/ref=sr_1_1?keywords=gtx+2080&qid=1577723642&sr=8-1'

def priceCheck():
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    #Titel and price
    title = soup.find(id='productTitle')
    titleText = title.get_text()
    price = soup.find(id="priceblock_ourprice")
    priceText = price.get_text()

    #converter
    convertPrice = float(priceText[1:7])
    
    print(convertPrice)
    print(titleText)

    #email
    if(convertPrice < 749.99):
        sendEmail()
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #enter email and password
    server.login('lpistolero95@gmail.com', '************')

    subject= 'Price on Item Went Down!!'
    body = 'Check the Link if the price is right https://www.amazon.com/MSI-Gaming-RTX-2080-Super/dp/B07VDMGYGZ/ref=sr_1_1?keywords=gtx+2080&qid=1577723642&sr=8-1'

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'lpistolero95@gmail.com',
        'bantezana@my.uri.edu',
        message
    )
    print('HEY, Email has been sent!')

    server.quit()

priceCheck()