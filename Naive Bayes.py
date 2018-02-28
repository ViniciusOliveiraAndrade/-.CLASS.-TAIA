#Conjunto de importações
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from ControleCSV import pegarCorpus

corpus = pegarCorpus()


dados_treino, dados_val, pols_treino, pols_val = train_test_split(corpus["comentarios"], corpus["classificacoes"], test_size=0.50)

#Cria uma instância para a bag-of-words   
bag = CountVectorizer()
  
bag_treino = bag.fit_transform(dados_treino)


# print(sorted(bag.vocabulary_)) 
 
# print(bag_treino)

#Cria a matriz termo-documento para o conjunto de validação com a bag já treinada
bag_val = bag.transform(dados_val)


nb_modelo = MultinomialNB()
nb_modelo.fit(bag_treino.toarray(), pols_treino)


#Realiza as predições para o conjunto de treinamento  
pols_pred_treino = nb_modelo.predict(bag_treino.toarray())
#Realiza as predições para o conjunto de validação
pols_pred_val = nb_modelo.predict(bag_val.toarray())
#Printa as predições calculadas para ambos os conjuntos
# print("Polaridades preditas para o conjunto de treinamento")
# print(pols_pred_treino)
# print("Polaridades preditas para o conjunto de validação")
# print(pols_pred_val)

print("\n---------------------------------------------\n")
print("\n---------------------------------------------\n")
print("\n---------------------------------------------\n")
print("\n---------------------------------------------\n")
print("\n---------------------------------------------\n")

b = dados_val
p = pols_val

pp = pols_pred_val
qt = 1
for i,a in enumerate(b):
	# print(""+str(a)+"\nPola: "+str(p[i])+"\t\tPred: "+str(pp[i]))
	print("N°:"+str(qt)+" Pola: "+str(p[i])+"\t\tPred: "+str(pp[i]))
	qt +=1


