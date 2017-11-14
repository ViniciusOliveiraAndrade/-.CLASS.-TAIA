from sklearn.metrics import cohen_kappa_score

resultado = cohen_kappa_score([1,2,2,1,2],[1,2,1,2,2])

print(resultado)