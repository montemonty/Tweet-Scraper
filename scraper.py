import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://twitter.com/kanyewest?lang=en'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def newestTweetFromKanye():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    newTweet = soup.find("div", class_="tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet").get_text()
    newTweetFinder = newTweet[40:45]
    if(id(newTweetFinder) == id('Jan 1')): #last tweet from Kanye West, used as a comparison
         send_mail()
    print(newTweetFinder.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('montanezj1997@gmail.com', REDACTED)
    subject = 'KANYE TWEETED'
    body = 'check twitter https://twitter.com/kanyewest?lang=en'
    msg =f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'montanezj1997@gmail.com',
        'montanezj1997@gmail.com',
        msg
    )

newestTweetFromKanye()
