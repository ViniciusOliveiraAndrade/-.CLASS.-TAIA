from nltk.tokenize import word_tokenize
import Limpeza as l

diretorio = "Test/facebook_data.csv"
lt = "__________________________________________________"

#pega a quantidade de comentarios antes e depos do pre processamento, recebe o diretorio do arquivo csv
def qt_antes_depois(diretorio):

	com,clas = l.pegar_comentarios_classificacao(diretorio)#pega os comentarios e as classificações
	corpus = l.limpar(diretorio) #pega os comentarios e as classificaões depois pre-processamento
	
	antes = []#lista antes pre-pro
	depois =[]#lista depois pre-pro
	antes_d = []#lista antes pre-pro diferente 
	depois_d =[]#lista depois pre-pro diferente

	#varra os comentarios antes pre-pro
	for comentario in com:
		antes.extend(word_tokenize(comentario))#tokeniza
	#varre os comentarios depois do pre-pro
	for comentarios in corpus["comentarios"]:
		depois.extend(comentarios)#adiciona a lista
	#varres os comentarios antes pre-pro e so pegas os diferentes
	for ca in antes:
		if ca not in antes_d:
			antes_d.append(ca)#adiciona a lita	
	#varre os comentarios depois pre-pro e so pegas os diferentes
	for cd in depois:
		if cd not in depois_d:
			depois_d.append(cd)#adiciona a lista

	qt_comentarios = len(com)#quantidade de comentarios
	qt_antes = len(antes)#quantidade de palavra antes pre-pro
	qt_depois = len(depois)#quantidade de palavra depois pre-pro
	qt_antes_d = len(antes_d)#quantidade de palavra antes pre-pro diferentes
	qt_depois_d = len(depois_d)#quantidade de palavra depois pre-pro diferentes

	#imprime os resultados
	print("\nQuantidade antes: "+str(qt_antes))
	print("Quantidade depois: "+str(qt_depois))
	
	print("\nQuantidade diferentes antes: "+str(qt_antes_d))
	print("Quantidade diferentes depois: "+str(qt_depois_d))
	
	print("\nQuantidade comentarios: "+str(qt_comentarios))
	
	print("\nQuantidade antes dividido por qt_Comentarios: "+str((qt_antes/qt_comentarios)))
	print("Quantidade depois dividido por qt_Comentarios: "+str((qt_depois/qt_comentarios)))

	print("\nQuantidade antes diferentes dividido pela quantidade de comentarios: "+str((qt_antes_d/qt_comentarios)))
	print("Quantidade depois diferentes dividido pela quantidade de comentarios: "+str((qt_depois_d/qt_comentarios)))

	print()
	#imprime os resultados em forma de tabela
	print(lt)
	print("Diferentes\t|Quantidade \t|Pré-Processamento ")
	print(lt)
	print("Não \t\t| {} \t\t| Antes".format(qt_antes))
	print("Não \t\t| {} \t\t| Depois".format(qt_depois))	
	print("Sim \t\t| {} \t\t| Antes".format(qt_antes_d))
	print("Sim \t\t| {} \t\t| Depois".format(qt_depois_d))
	print(lt)
	print("\nQuantidade comentarios: "+str(qt_comentarios))
	print(lt)
	print("\nQuantidade antes diferentes dividido pela quantidade de comentarios: "+str((qt_antes_d/qt_comentarios)))
	print("Quantidade depois diferentes dividido pela quantidade de comentarios: "+str((qt_depois_d/qt_comentarios)))	
	print(lt)
#chama a função
qt_antes_depois(diretorio)