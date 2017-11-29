from nltk.tokenize import TweetTokenizer
from nltk.stem	import RSLPStemmer
from nltk.corpus import stopwords
from unicodedata import normalize
import csv

test = "Exemplo de tokenização de um tweet.#DarBobeira é NÃO achar que o BB envia e-mail pedindo a atualização dos seus dados cadastrais ou com resultado de sorteio:http://t.co/muffie... SPOIEORIWERN #POSKOPKDK KMMKKPODSK HTTP://TUDO.PUTA Bolsanaro2018"
diretorio = "Test/facebook_data.csv"

#Função para remover acentos e emogis
def remover_acentos(txt):
     return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

#Faz o tokenizer Pedo do Tweeter
def tokenizer(texto,remover = False):
	
	tt = TweetTokenizer()
	textoLower = texto.lower()
	if remover:
		textoSemAcento = remover_acentos(textoLower)		
		text = tt.tokenize(textoSemAcento)
	else:
	
		text = tt.tokenize(textoLower)
	
	return text

#print(tokenizer(test))
#print(len(tokenizer(test)))

def remover_URL_hastags_mentions (lista,nomeCandidato):
	novaLista = []
	for item in lista:
		if "#" not in item and "@" not in item and "http" not in item and nomeCandidato not in item: 
			novaLista.append(item)
	return novaLista

#print(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro"))
#print(len(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro")))
 

def remover_stopwords (lista):
	stopword = set(stopwords.words('portuguese'))

	novaLista = [word for word in lista if not word in stopword]
	return novaLista

#print(remover_stopwords(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro")))
#print(len(remover_stopwords(remover_URL_hastags_mentions(tokenizer(test),"bolsonaro"))))

def pegar_comentarios_classificacao(diretorio):
	comentario = []
	classificacao = []
	with open(diretorio) as arquivocsv:
		ler = csv.DictReader(arquivocsv, delimiter=",")
		for linha in ler:
			if linha["Classificação"] == "2" or linha["Classificação"] == "1": 
				comentario.append(linha['Mensagem'])
				classificacao.append(linha["Classificação"])
				
	return comentario,classificacao

#print(pegar_comentarios_classificacao(diretorio))

#faz a lipensa utilizando todas as funções acima
def limpar(diretorio,remover = False):
	corpus = {"comentarios":[],"classificacoes":[]}
	comentario,Classificacao = pegar_comentarios_classificacao(diretorio)
	for i, c in enumerate(comentario):
		corpus["comentarios"].append(remover_stopwords(remover_URL_hastags_mentions(tokenizer(c,remover),"bolsonaro")))
		corpus["classificacoes"].append(Classificacao[i])
	return corpus


#Imprime o corpus
def imprimeCorpus(corpus):
	for i , c in enumerate(corpus["comentarios"]):
		print("Comentario:"+str(c)+" | Classicação:"+str(corpus["classificacoes"][i]))

#imprimeCorpus(limpar(diretorio)) 