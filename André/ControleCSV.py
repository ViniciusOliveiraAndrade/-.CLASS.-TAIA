import csv
from Limpeza import imprimeCorpus

#Função para salvar os dados do retorno do facebook recebe os dados, e o intervalo de caracteres que o comentarios deve ter para ser salvo
def salvar_CSV ( dados, maximo_caracteres, minimo_caracteres = 16):

	max_caracteres = maximo_caracteres #quantidade maxima de caracter
	min_caracteres = minimo_caracteres #quantidade minima de caracter

	qt_com = 0 #quantidade de comentarios salvos
	#Salvar os dados coletados no arquivo facebook_data.csv
	meu_arquivo = open('results/facebook_data.csv', mode='a', encoding='utf-8') #abre/cria o arquivo onde serao salvo os comentarios
	
	writer = csv.writer(meu_arquivo) #abre como csv

	writer.writerow(["ID Comentario", "Nome do usuário","Mensagem","Ándre","Vinícius"]) #escreve um titulo ao ariquivo

	for dado in dados['comments']['data']: #laço para salvar os comentarios
	    
	    if "bolsonaro" in dado['message'].lower(): #salva os comentarios apenas os que tiverem bolsonaro sitados
	    	if len(dado['message']) <= max_caracteres and len(dado['message']) > min_caracteres: # verifica o tamanho em caracteres do comentario para saber se esta entre o intervalo definido
	            writer.writerow([dado['id'], dado['from']['name'],dado['message']]) #salva o id, nome do ususario e comentario
	            qt_com += 1 #acrescenta um a quantidade salva

	meu_arquivo.close() #fecha o arquivo
	print("Quantidades de commentarios salvos: %i"%(qt_com)) #imprime a quantidade de comentarios
	
def pegarCorpus(diretorio):
	corpus = {"comentarios":[],"classificacoes":[]} 
	with open(diretorio) as arquivocsv: #abre o arquivo do diretorio
		ler = csv.DictReader(arquivocsv, delimiter=",") #ler como csv
		for linha in ler: #varre as linhas do arquivo
			corpus["comentarios"].append(linha['comentario'])#atribui o comentario a lista
			corpus["classificacoes"].append(linha["classificacao"])#atribui a polaridade a lista	
	return corpus
	
#imprimeCorpus(pegarCorpus())