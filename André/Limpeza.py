from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

import unicodedata 
import csv
import re

#Função para remover emotions, recebe o comentario e retorna ela sem emotion
def removeemoji(word):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', word)  # no emoji

def remover_acentos(txt):
	# Unicode normalize transforma um caracter em seu equivalente em latin.
	nfkd = unicodedata.normalize('NFKD', txt)
	palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
 
	# Usa expressão regular para retornar a palavra apenas com números, letras e espaço
	return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)


#Faz o tokenizer Pelo do Tweeter, recebe o texto e se vai ou não remover os emotions, recebe o texto e se remove ou não os acentos e emotions
def tokenizer(texto):
	
	tt = TweetTokenizer() #cria o tokenizer do tweet
	textoLower = texto.lower() #passa o texto para caixa baixa
	textoSemAcento = remover_acentos(textoLower)#Remove os acentos
	textoSemEmoji = removeemoji(textoSemAcento)#Remove os Emoji
	text = tt.tokenize(textoSemEmoji)#tokeniza	
	return text #retorna o texto a pois o tokenizer e sem emoji 
 

#Funçao para remover URL hastags mentions e o nome do candidato, recebe uma lista de palavras e o nome a ser removido 
def remover_URL_hastags_mentions (lista,nomeCandidato):
	
	novaLista = [] #cria um novo arquivo
	for item in lista: #varre a lista
		if "#" not in item and "@" not in item and "http" not in item and nomeCandidato not in item: #se não tiver nada que deve ser removido
			novaLista.append(item) #adiciona a nova lista
	return novaLista #retorna o comentario limpo


#remove as stopwords, recebe uma lista de palavras
def remover_stopwords (lista):
	
	stopword = set(stopwords.words('portuguese'))#cria o stop word para portugues
	novaLista = [word for word in lista if not word in stopword] #cria uma nova lista sem as stopwords
	return novaLista#retorna a nova lista limpa
	 

#função para pegar os comentarios e sua polarização, recebe o diretorio do arquivo
def pegar_comentarios_classificacao(diretorio):
	comentario = [] #cria a lista de comentario
	classificacao = [] #cria lista de classificação/ polaridade
	with open(diretorio) as arquivocsv: #abre o arquivo do diretorio
		ler = csv.DictReader(arquivocsv, delimiter=",") #ler como csv
		for linha in ler: #varre as linhas do arquivo
			comentario.append(linha['Mensagem'])#atribui o comentario a lista
			classificacao.append(linha["Classificação"])#atribui a polaridade a lista
				
	return comentario,classificacao #retorna os comentarios e as polaridade


#faz a lipensa utilizando todas as funções acima, recebe o diretorio do arquivo e se deve limpar ou não
def limpar(diretorio):
	corpus = {"comentarios":[],"classificacoes":[]}#cria um dicionario para ser o corpu
	comentario,Classificacao = pegar_comentarios_classificacao(diretorio)#pega os comentarios
	for i, c in enumerate(comentario):# varre os comentarios
		corpus["comentarios"].append(remover_stopwords(remover_URL_hastags_mentions(tokenizer(c),"bolsonaro"))) #limpa e tokeniza os comentarios e atribui ao corpus
		corpus["classificacoes"].append(Classificacao[i])#atribui a classificação de cada comentario
	return corpus #retorna o corpus
 

def uni_string(lista):
	frase = ""
	for p in lista:
		frase+= " "+str(p)
	return frase


def corpus(diretorio):
	corpus = limpar(diretorio)
	comentarios = []
	for lista in corpus["comentarios"]:
		comentarios.append(uni_string(lista))
	corpus["comentarios"] = comentarios
	return corpus

def tranformkfold(corpus):
	base = []
	for i,cla in enumerate(corpus["comentarios"]):
		temp1 = cla
		temp2 = int(corpus["classificacoes"][i])
		base.append(tuple([temp1, temp2]))
	return base