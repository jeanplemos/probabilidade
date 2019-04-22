import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
while True:
    os.system('clear')
    print()
    print('\033[33m-=\033[m' * 31)
    print('        \033[31m<< C A L C U L A D O R A  B I N O M I A L >>\033[m')
    print('\033[33m-=\033[m' * 31)
    print()
    print ("\033[36mPara calcular uma probabilidade binomial é preciso especificar:")
    print()
    n = int(input("Número de observações [n]: \033[31m"))
    factn = 1
    for i in range(1,n+1):
        factn = factn * i
    print()
    x = int(input("\033[36mNúmero de sucessos [x]: \033[31m"))
    factx = 1
    for j in range(1,x+1):
        factx = factx * j
    factnx = 1
    for k in range(1,(n-x)+1):
        factnx = factnx * k
    c = factn/(factx*factnx)
    print()
    p = float(input("\033[36mProbabilidade de sucesso em cada observação [p em valor absoluto]: \033[31m"))
    px = float (c*(p**x)*(1-p)**(n-x))
    print('''
\033[33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m
                 \033[31m<< R E S U L T A D O S >>\033[m
\033[33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m
''')
    print (f"\033[36mProbabilidade de {x} é de: \033[31m{(px*100):.2f}%")
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
    print()
    print(f'\033[36mProbabilidade de no máximo {x} é de: \033[31m{(pxa2*100):.2f}%')
    print()
    print(f'\033[36mProbabilidade de no mínimo {x} é de: \033[31m{((px+(1-pxa2))*100):.2f}%')
    print()
    media = n * p
    print(f'\033[36mMédia: \033[31m{media:.2f}')
    variancia = float(n*p*(1-p))
    desvio_padrao = variancia**0.5
    print()
    print(f"\033[36mDesvio padrão: \033[31m{desvio_padrao:.2f}")
    plt.axis([0,i,0,1])
    plt.show()
    while True:
       print()
       continua = input('\033[36mDeseja continuar? [S/n] \033[31m')
       if continua in 'NnsS':
           break
       else:
           print()
           print('\033[36mERRO!! Digite apenas "S" ou "N"!')
    if continua == 'N' or continua == 'n':
        break
