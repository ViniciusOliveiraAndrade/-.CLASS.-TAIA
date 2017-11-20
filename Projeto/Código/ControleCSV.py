import csv


def salvar_CSV ( dados, maximo_caracteres, minimo_caracteres = 16):

	max_caracteres = maximo_caracteres
	min_caracteres = minimo_caracteres

	qt_com = 0

	#Salvar os dados coletados no arquivo facebook_data.csv
	meu_arquivo = open('results/facebook_data.csv', mode='a', encoding='utf-8')
	writer = csv.writer(meu_arquivo)

	writer.writerow(["ID Comentario", "Nome do usuário","Mensagem","Ándre","Vinícius"])

	for dado in dados['comments']['data']:
	    
	    if "bolsonaro" in dado['message'].lower():
	    	if len(dado['message']) <= max_caracteres and len(dado['message']) > min_caracteres:
	            writer.writerow([dado['id'], dado['from']['name'],dado['message']])
	            qt_com += 1

	meu_arquivo.close()
	print("Quantidades de commentarios salvos: %i"%(qt_com))