from Limpeza import corpus as c #carrega a funcção de pegar o corpus que retorna o corpus que é um dicionario com comentarios e classificacoes
from Limpeza import tranformkfold
from Bags import bagofwords

# corpus = c("Corpus_Desbalanceado.csv")#carrga o corpos desbalanceado com 6 classificações 
corpus = c("Corpus_Balanceado.csv")#carrga o corpos balanceado com 2 classificações
corpus = tranformkfold(corpus)
print("Carregamento e limpeza do corpus concluido")
# print(corpus)

bagofwords(corpus)