from bs4 import BeautifulSoup as take
import requests as ree
def takedata(url):
    l=[]
    for c in url:
        re = ree.get(c)
        so = take(re.text,"html.parser")
        lista = str(so.body).split()
        cont=0
        for word in lista:
            if word == 'abacaxi':
                cont+=1
        print(cont)
takedata(['https://pt.wikipedia.org/wiki/Anan%C3%A1s'])
