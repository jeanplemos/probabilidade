import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print ("Para calcular uma probabilidade binomial é preciso especificar:")
n = int(input("Número de observações: "))
factn = 1
for i in range(1,n+1):
    factn = factn * i
x = int(input("Número de sucessos: "))
factx = 1
for j in range(1,x+1):
    factx = factx * j
factnx = 1
for k in range(1,(n-x)+1):
    factnx = factnx * k
c = factn/(factx*factnx)
p = float(input("Probabilidade de sucesso em cada observação: "))
px = float (c*(p**x)*(1-p)**(n-x))
print ("Probabilidade individual é de:", px)
l = 0
pxa2 = 0
while l <= x:
    factl = 1
    for m in range(1,l+1):
        factl = factl * m
    factnl = 1
    for o in range (1, (n-l)+1):
        factnl = factnl * o
    d = factn/(factl*factnl)
    pxa = float(d*(p**l)*(1-p)**(n-l))
    plt.plot([l], [pxa], linestyle='--', color='g', marker='s',
         linewidth=3.0)
    l = l+1
    pxa2 = pxa2 + pxa
print("Probabilidade acumulada de < ou = ao número de sucessos é: ", pxa2)
print("Probabilidade acumulada de > ou = ao número de sucessos é: ", px+(1-pxa2))
media = float(n*p)
print("Média: ", media)
variancia = float(n*p*(1-p))
desvio_padrao = variancia**0.5
print("Desvio padrão: ", desvio_padrao)
plt.axis([0,i,0,1])
plt.show()
