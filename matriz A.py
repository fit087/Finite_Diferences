# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 20:32:17 2014

@author: Karyta Almeida
"""

import numpy as np
#def main ():
n=21
#    A = forme_matriz(n,n)
kt=0.05
d=0.05
h=0.1
u=1
   
A1= (u*kt)/(2*h)+(d*kt)/(h**2)
A2= (kt/kt)+(2*d*kt)/(h**2)
A3= (u*kt)/(2*h)-(d*kt)/(h**2)
A=A2*np.eye(n, k=0)+(A1)*np.eye(n, k=-1)+(A3)*np.eye(n, k=1)
print A


#aplicando as condições iniciais - matriz B

import math 
#n=21
k = 1
pi = 3.141592653
t = 0
d = 0.05
u = 1
x = 0
matriz = []

while x<=2:
    coluna = []                
    b=2*pi*(k**2)*(x-u*t)
    a = math.exp(-4*(pi**2))*math.sin(b)
#    c = [[(a) for y in range(1)] for z in range(1)]
    x = x+0.1
    ele = float(a)
    coluna.append(a)
    matriz.append(coluna)
    print c

# Ax=B - resolvendo
B=np.linalg.solve(A, c)
print B

    





