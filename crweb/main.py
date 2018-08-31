from web import *
pega_palavra =contapalavrasite(["http://www8.receita.fazenda.gov.br/simplesnacional/"],'padrão')
print(pega_palavra.conta_palavra())
