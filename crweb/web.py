from bs4 import BeautifulSoup as take
import requests as ree
def takedata(url,wordd):
    l=[]
    for c in url:
        re = ree.get(c)
        so = take(re.text,"html.parser")
        lista = str(so.body).split()
        cont=0
		li= { }
        for word in lista:
		if wordd == word:
			cont+=1
		li["link"] = str(c)
		li[word] = cont
        		
          
takedata(['https://pt.wikipedia.org/wiki/Anan%C3%A1s'])
