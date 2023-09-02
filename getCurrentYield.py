import requests
from bs4 import BeautifulSoup

def getCurrentYield():
    page=requests.get('https://fred.stlouisfed.org/series/AAA')
    soup=BeautifulSoup(page.content,"html.parser")
    observationValue=soup.find('span',class_='series-meta-observation-value')
    return(float(observationValue.get_text()))
