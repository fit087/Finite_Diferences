# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 17:35:14 2014

@author: Karyta Almeida
"""

#aplicando as condições iniciais - matriz B


#n=21
i = 0
k = 1
pi = 3.141592653
t = 0
d = 0.05
u = 1

matriz = []

while i<=2:
    linha = []                
    b=2*pi*i*k*(i-u*t)
    a = math.exp(-d*k*t)*math.sin(b)
    c = [[(a) for y in range(1)] for x in range(1)]
    i = i+0.1
    ele = float(a)
    linha.append(a)
    matriz.append(linha)
    print a
#aplicando as condições de contorno
    
    #array([1, 2, 3])