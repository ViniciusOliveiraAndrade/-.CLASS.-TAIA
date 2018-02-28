from unicodedata import normalize
from sklearn.metrics import cohen_kappa_score
import csv

lt = "_________________________________________________________________________________________________"
d = "Test/facebook_data.csv"

#Função para calcular o Kappa, recebe o diretorio
def calcular_kappa(diretorio):
    
    #listas de nossas classificação
    andre = []
    vinicius = []
    
    #abre o arquivo e pega nossas classificações e salva
    with open(diretorio) as arquivocsv:
        ler = csv.DictReader(arquivocsv, delimiter=",")
        for linha in ler:
            andre.append(linha['Ándre'])
            vinicius.append(linha["Vinícius"])
    #calcula nosso kappa
    pre = float(cohen_kappa_score(andre,vinicius))
    resultado = pre *100
    print("\n"+lt)
    print("\n|A porcetangem do kappa é: %.2f"%(resultado))
    print(lt+"\n")


#Função para ver a quantidade de numeros positivos, negativos, ambos, neutros, irrelevantes e ironicos 
def quantidadePN(diretorio):
    #Vinícius quantidade de numeros positivos, negativos, ambos, neutros, irrelevantes e ironicos
    vp = 0
    vn = 0
    va = 0
    vne = 0
    vi = 0
    vir = 0
   
    #André quantidade de numeros positivos, negativos, ambos, neutros, irrelevantes e ironicos
    ap = 0
    an = 0
    aa = 0
    ane = 0
    ai = 0
    air = 0
	
    #abre o arquivo e conta
    with open(diretorio) as arquivocsv:
        ler = csv.DictReader(arquivocsv, delimiter=",")
        for linha in ler:
            #Vinícius 
            if str(linha["Vinícius"]) == "1":
            	vp +=1
            if str(linha["Vinícius"]) == "2":
            	vn +=1
            if str(linha["Vinícius"]) == "3":
            	va +=1
            if str(linha["Vinícius"]) == "4":
            	vne +=1
            if str(linha["Vinícius"]) == "5":
            	vi +=1
            if str(linha["Vinícius"]) == "6":
            	vir +=1
            #André
            if str(linha["Ándre"]) == "1":
            	ap +=1
            if str(linha["Ándre"]) == "2":
            	an +=1
            if str(linha["Ándre"]) == "3":
            	aa +=1
            if str(linha["Ándre"]) == "4":
            	ane +=1
            if str(linha["Ándre"]) == "5":
            	ai +=1
            if str(linha["Ándre"]) == "6":
            	air +=1
    #imprime o resultado
    print(lt)
    print("\n|Nome\t\t| Positivos\t| Negativos\t| Ambas\t| Neutras\t| Irrelevantes\t| Ironias")
    print("|Ándre\t\t| %i\t\t| %i\t\t| %i\t| %i\t\t| %i\t\t| %i"%(ap,an,aa,ane,ai,air))
    print("|Vinícius\t| %i\t\t| %i\t\t| %i\t| %i\t\t| %i\t\t| %i"%(vp,vn,va,vne,vi,vir))
    print(lt+"\n")

#função de quantidade classificações finais
def quantidadePNT(diretorio):
    #Quantidade de numeros positivos, negativos, ambos, neutros, irrelevantes e ironicos
    p = 0
    n = 0
    a = 0
    ne = 0
    i = 0
    ir = 0
    #Abre o arquivo e conta  
    with open(diretorio) as arquivocsv:
        ler = csv.DictReader(arquivocsv, delimiter=",")
        for linha in ler:
             
            if str(linha["Classificação"]) == "1":
            	p +=1
            if str(linha["Classificação"]) == "2":
            	n +=1
            if str(linha["Classificação"]) == "3":
            	a +=1
            if str(linha["Classificação"]) == "4":
            	ne +=1
            if str(linha["Classificação"]) == "5":
            	i +=1
            if str(linha["Classificação"]) == "6":
            	ir +=1
    #imprime
    print(lt)
    print("\n|Nome\t\t| Positivos\t| Negativos\t| Ambas\t| Neutras\t| Irrelevantes\t| Ironias")
    print("|Total\t\t| %i\t\t| %i\t\t| %i\t| %i\t\t| %i\t\t| %i"%(p,n,a,ne,i,ir))
    print(lt+"\n")

#Função para remover acentos e emogis
def remover_acentos(txt):
     return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')


#Apenas ignore a parte de baixo
"""
#Menu Simples
def menu():

	print( "\n0 - Sair\n1 - Calcular o Kappa\n2 - Calcular A Quantida De Poitivos E Negativos" )
	op = int(input(">"))

	if op == 0:
		exit()
	elif op == 1:
		calcular_kappa(d)
		menu()
	elif op == 2:
		quantidadePN(d)
		menu()

#menu()
"""
#calcular_kappa(d)
#quantidadePN(d)
quantidadePNT(d)