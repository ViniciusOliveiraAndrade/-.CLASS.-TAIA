from nltk.tokenize import TweetTokenizer
from nltk.stem	import RSLPStemmer
from nltk.corpus import stopwords

import unicodedata 
import csv
import re

test = "Exemplo de tokenização de um tweet.#DarBobeira é NÃO achar que o BB envia e-mail pedindo a atualização dos seus dados cadastrais ou com resultado de sorteio:http://t.co/muffie... SPOIEORIWERN #POSKOPKDK KMMKKPODSK HTTP://TUDO.PUTA Bolsanaro2018"
diretorio = "Test/facebook_data.csv"

#Função para remover acentos, recebe o texto e se vai ou não remover os ascentos
def remover_acentos(txt):
	# Unicode normalize transforma um caracter em seu equivalente em latin.
	nfkd = unicodedata.normalize('NFKD', txt)
	palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
 
	# Usa expressão regular para retornar a palavra apenas com números, letras e espaço
	return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)
#Função para remover emotions, recebe o comentario e retorna ela sem emotion
def removeemoji(word):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', word)  # no emoji

def stemizacao(palavra):
    stemmerPT = RSLPStemmer()
    p = stemmerPT.stem(palavra)
    return p


#Faz o tokenizer Pelo do Tweeter, recebe o texto e se vai ou não remover os emotions, recebe o texto e se remove ou não os acentos e emotions
def tokenizer(texto,remover = False):
	
	tt = TweetTokenizer() #cria o tokenizer do tweet
	textoLower = texto.lower() #passa o texto para caixa baixa
	
	if remover: # se for para remover acentos e emotions
		textoSemAcento = remover_acentos(textoLower)
		textoSemEmoji = removeemoji(textoSemAcento)		
		text = tt.tokenize(textoSemEmoji)
	else:#se não for para remover nada so tokenizer
		text = tt.tokenize(textoLower)
		
	return text #retorna o texto a pois o tokenizer e sem acentos e emoji se for o caso

#print(tokenizer(test))
#print(len(tokenizer(test)))

#Funçao para remover URL hastags mentions e o nome do candidato, recebe uma lista de palavras e o nome a ser removido 
def remover_URL_hastags_mentions (lista,nomeCandidato):
	novaLista = [] #cria um novo arquivo
	for item in lista: #varre a lista
		if "#" not in item and "@" not in item and "http" not in item and nomeCandidato not in item: #se não tiver nada que deve ser removido
			novaLista.append(item) #adiciona a nova lista
	return novaLista #retorna o comentario limpo

#print(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro"))
#print(len(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro")))
 
#remove as stopwords, recebe uma lista de palavras
def remover_stopwords (lista):
	stopword = set(stopwords.words('portuguese'))#cria o stop word para portugues

	novaLista = [word for word in lista if not word in stopword] #cria uma nova lista sem as stopwords
	novaListaSteemer = []
	# for palavra in novaLista:
	# 	novaListaSteemer.append(stemizacao(palavra))
	# return novaListaSteemer #retorna a nova lista limpa
	return novaLista
 
#print(remover_stopwords(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro")))
#print(len(remover_stopwords(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro"))))

#função para pegar os comentarios e sua polarização, recebe o diretorio do arquivo
def pegar_comentarios_classificacao(diretorio):
	comentario = [] #cria a lista de comentario
	classificacao = [] #cria lista de classificação/ polaridade
	with open(diretorio) as arquivocsv: #abre o arquivo do diretorio
		ler = csv.DictReader(arquivocsv, delimiter=",") #ler como csv
		for linha in ler: #varre as linhas do arquivo
			if linha["Classificação"] == "2" or linha["Classificação"] == "1": #pega apenas as linhas com classificações positivas = 1 e negativas = 2 
				comentario.append(linha['Mensagem'])#atribui o comentario a lista
				classificacao.append(linha["Classificação"])#atribui a polaridade a lista
				
	return comentario,classificacao #retorna os comentarios e as polaridade

#print(pegar_comentarios_classificacao(diretorio))

#faz a lipensa utilizando todas as funções acima, recebe o diretorio do arquivo e se deve limpar ou não
def limpar(diretorio,remover = False):
	corpus = {"comentarios":[],"classificacoes":[]}#cria um dicionario para ser o corpu
	comentario,Classificacao = pegar_comentarios_classificacao(diretorio)#pega os comentarios
	for i, c in enumerate(comentario):# varre os comentarios
		corpus["comentarios"].append(remover_stopwords(remover_URL_hastags_mentions(tokenizer(c,remover),"bolsonaro"))) #limpa e tokeniza os comentarios e atribui ao corpus
		corpus["classificacoes"].append(Classificacao[i])#atribui a classificação de cada comentario
	return corpus #retorna o corpus


#Imprime o corpus
def imprimeCorpus(corpus):
	for i , c in enumerate(corpus["comentarios"]):
		print(str(i)+" Comentario:"+str(c)+" | Classicação:"+str(corpus["classificacoes"][i]))

#imprimeCorpus(limpar(diretorio,True)) 

def uni_string(lista):
	frase = ""
	for p in lista:
		frase+= " "+str(p)
	return frase


def corpus(diretorio, remover = False, imprimir = False):
	corpus = limpar(diretorio,remover)
	comentarios = []
	for lista in corpus["comentarios"]:
		comentarios.append(uni_string(lista))
	corpus["comentarios"] = comentarios
	if imprimir:
		imprimeCorpus(corpus)
	return corpus

#corpus(diretorio,True,True)

def salvarCorpus(corpus):
	meu_arquivo = open('Test/corpus.csv', mode='a', encoding='utf-8') #abre/cria o arquivo onde serao salvo os comentarios
	writer = csv.writer(meu_arquivo) #abre como csv
	writer.writerow(["comentario","classificacao"]) #escreve um titulo ao ariquivo
	for i , c in enumerate(corpus["comentarios"]):
		writer.writerow([str(c),str(corpus["classificacoes"][i])]) #salva o id, nome do ususario e comentario
	meu_arquivo.close() #fecha o arquivo


#salvarCorpus(corpus(diretorio,True,True)) 