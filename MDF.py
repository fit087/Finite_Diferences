# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 18:56:18 2014

@author: Karyta Almeida
"""
import math 
import numpy as np

def main():
    A=matrizIdent()
    B=matrizB()
    resultado=[]
    resultado.append(B)
    for i in range(1,21):
       B=resolve(A,B)
       resultado.append(B)
    return  resultado   
    
#def main ():
n=21
#    A = forme_matriz(n,n)
kt=0.025
d=0.05
h=0.1
u=1.0
k = 1.0
pi = 3.141592653
t = 0
d = 0.05
u = 1.0
a = 1.0


#variaveis

# Coeficiente A
def coefA():
    return -((u*kt)/(2*h)+(d*kt)/(h**2))
    
# Coeficiente B
def coefB():
    return (kt/kt)+(2*d*kt)/(h**2)
    
# Coeficiente C
def coefC():
    return -((u*kt)/(2*h)-(d*kt)/(h**2))
        
# Matriz Identidade
def matrizIdent():
    return coefB()*np.eye(n, k=0)+(coefA())*np.eye(n, k=-1)+(coefC())*np.eye(n, k=1)
    
# Condição de Contorno
def condCont(x):

#    return math.exp(-4*(pi**2))*math.sin(2*pi*k*(x-u*t))
    return math.exp(-d*(k**2)*t)*math.sin(2*np.pi*k*(2-u*t))
    
# Condição Inicial
def condInic(x):
    return math.sin(2.0*np.pi*k*(x*1.0))
    
# Matriz B
def matrizB():
    x = 0
    matriz = []
    while x<2.1:
        if x != 0 and x != 2:
            matriz.append(condInic(x))
#        matriz.append(condCont(x))
        else:
            matriz.append(condCont(x))
        x=x+0.1
        
    return matriz
    
# X = A*B
def resolve(matrizA, matrizB):
    return np.linalg.solve(matrizA, matrizB)
       
X=main()
print X