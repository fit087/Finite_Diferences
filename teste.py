# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 00:48:24 2014

@author: Karyta Almeida
"""

import math
#n=21
k = 1
pi = 3.141592653
t = 0
u = 1
x = 0
matriz = []

while x<=2:
    linha = []                
#    a =2*pi*(k**2)*(x-u*t)
#    b = math.exp(-4*(pi**2))*math.sin(a)
    b=math.exp(-d*(k**2)*t)*math.sin(2*pi*k*(x-u*t))
    c = [[(b) for y in range(1)] for z in range(1)]
    x = x+0.1
    ele = float(b)
    linha.append(b)
    matriz.append(linha)
    print c

import numpy as np
#def main ():
n=21
#   A = forme_matriz(n,n)
#   kt=0.05
#   D=0.05
#   h=0.10
#   u=1
A1=-4.95
A2=-5.05
A3=30
A=A2*np.eye(n, k=0)+(A1)*np.eye(n, k=-1)+(A3)*np.eye(n, k=1)
print A

B=np.linalg.solve(A, c)
print B