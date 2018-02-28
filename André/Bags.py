from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
from sklearn.svm import LinearSVC
from sklearn import metrics


def bagofwords(base):
    #dados_treino, dados_val, pols_treino, pols_val = train_test_split(dataset, polarity, test_size=0.25)
    k_fold = KFold(n_splits=4, shuffle=True)
    acuracia = 0

    for train, test in k_fold.split(base):
        
        dados_treino = []
        pols_treino = []
        dados_val = []
        pols_val = []
        
        for x in train:
        
            dados_treino.append(base[x][0])
            pols_treino.append(base[x][1])
        
        for y in test:
        
            dados_val.append(base[y][0])
            pols_val.append(base[y][1])
       
        # Print do conjunto de treinamento e suas respectivas polaridades
        # print("Conjunto de Treinamento")
        # print(dados_treino)
        # # Print do conjunto de validaĂ§ĂŁo e suas respectivas polaridades
        # print("Polaridades do Conjunto de Treinamento")
        # print(pols_treino)

        # Print do conjunto de validaĂ§ĂŁo e suas respectivas polaridades
        # print("Conjunto de Validação")
        # print(dados_val)
        # print("Polaridades do Conjunto de Validação")
        # print(pols_val)

        






        """
            Escolha o tipo de bag, descomente-o e comente os outros
        """
        # Cria uma instânncia para a bag-of-words
        bag = CountVectorizer() # bag count vectorizer
        # bag = TfidfVectorizer()  # bag tf-idf
        # bag = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1) #bag bigram
        







        # Método fit_transform:
        # fit = cria e aprende a bag
        # transform = cria a matriz termo-documento
        bag_treino = bag.fit_transform(dados_treino)

        # Printa o vocabulário da bag-of-words
        # print("Vocabulário da bag-of-words")
        # print(sorted(bag.vocabulary_))
        # print("\n---------------------------------------------\n")

        # Printa a bag-of-words
        # print("Bag-of-words de treino")
        # print(bag_treino)
        # print("\n---------------------------------------------\n")

        # Cria a matriz termo-documento para o conjunto de validaĂ§ĂŁo com a bag jĂĄ treinada
        bag_val = bag.transform(dados_val)

        # Printa a matriz termo-documento criada para o conjunto de validaĂ§ĂŁo
        # print("Bag-of-words de validaĂ§ĂŁo")
        # print(bag_val)
        # print("\n---------------------------------------------\n")

        pols_pred_val = predict(bag_treino, pols_treino, bag_val)

        acr = metrics.accuracy_score(pols_val, pols_pred_val)
        print(metrics.confusion_matrix(pols_val, pols_pred_val, labels=[1, 2]))
        acuracia += acr
    acuracia = (acuracia / 4) * 100
    print("\n\n\nAcuracia média: %.2f" % acuracia, "%")



def predict(bag_treino, pols_treino, bag_val):
    """
    Escola um modelo de algoritmo e descomente-o e comente os outros
    :param bag_treino: bag de treino
    :param pols_treino: polaridades de treino
    :param bag_val: bag de validação
    :return: retorna as polaridades preditas
    """





    modelo = MultinomialNB()    # Cria uma instância para o algoritmo Multinomial Naive Bayes
    # modelo = LinearSVC()   # Cria uma instânncia para o algoritmo SVM
    # modelo = LogisticRegression()   # Cria uma instânncia para o algoritmo Logistic Regression

    



    # O método fit treina o modelo utilizando o algoritmo Multinomial Naive Bayes
    # O argumento da bag deve ser passado no formato array
    modelo.fit(bag_treino.toarray(), pols_treino)

    # Realiza as prediĂ§Ăľes para o conjunto de treinamento
    pols_pred_treino = modelo.predict(bag_treino.toarray())
    # Realiza as prediĂ§Ăľes para o conjunto de validação
    pols_pred_val = modelo.predict(bag_val.toarray())
    # Printa as prediĂ§Ăľes calculadas para ambos os conjuntos
    # print("Polaridades preditas para o conjunto de treinamento")
    # print(pols_pred_treino)
    # print("Polaridades preditas para o conjunto de validação")
    # print(pols_pred_val)

    return pols_pred_val
