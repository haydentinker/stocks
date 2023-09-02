import requests
from bs4 import BeautifulSoup

def get5YearGrowthRate(ticker):
    URL=f"https://finance.yahoo.com/quote/{ticker}/analysis?p={ticker}"
    page=requests.get(URL,headers={'User-Agent':'Hayden Tinker','From':'haydentinker613@gmail.com'})
    soup=BeautifulSoup(page.content,"html.parser")
    trList=soup.find_all('tr',class_='BdT Bdc($seperatorColor)')
    for tr in trList:
        header=tr.find('td',class_='Ta(start) Py(10px)')
        if(header):
            if(header.get_text()=="Next 5 Years (per annum)"):
                growthRate=tr.find('td',class_='Ta(end) Py(10px)').get_text()
                return(float(growthRate.replace("%","")))
