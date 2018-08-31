from bs4 import BeautifulSoup as take
import requests as ree
import json
#'''Importando todas as dependencias para o programa'''
class contapalavrasite:
    def __init__(self,url =[],palavra=''):
        self.cont = 0
        self. li = []
        self.url = url
        self.palavra = palavra
#'''Inicializando o construtor sendo a passagem da url e da palavra desejada, obrigatorio'''
    def converte_url(self):
        lii = [] #'''Lista para adiionar a pagina ja convertida'''
        for c in self.url: #'''Esse laço litera toda a lista de url e converte cada pagina html da  url em um lista'''
            re = ree.get(c)
            so = take(re.text,"html.parser")
            lista = str(so.body).split() #converte
            lii.append(lista)
            return lii
#'''A função acima pega uma url e converte o codigo Html em uma lista de caracteries'''
    def conta_palavra(self):
            dicionario = {}
            g = self.converte_url()
            for pagina in g:
                for word in pagina:
                    if self.palavra == word:
                        self.cont+=1
                dicionario = [self.palavra,self.cont]
                self.li.append(dicionario)
            with open("palavras.json","w") as lista:
                json.dump(self.li, lista)
            with open('palavras.json') as dados:
                data = json.load(dados)
            return data
