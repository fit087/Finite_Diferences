# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 18:56:18 2014

@author: Karyta Almeida
"""
import math 
import numpy as np

def main():
#Calculando o X a cada passo de tempo (0,05, 0,025, 0,0125)
    A=matrizIdent()
    B=matrizB()
    resultado=[]
    resultado.append(B)
    for i in range(1,41):
       B=resolve(A,B)
#       sum+=B-Sol_analitica
#       E=h*np.square
       resultado.append(B)
    return  resultado   
    
#def main ():
n= 41
#    A = forme_matriz(n,m)
kt=0.0005
d=0.05
L=2.0
u=1.0
h=L/(n)
print h
k = 1.0
#pi = 3.141592653
t = 0
d = 0.05
u = 1.0
a = 1.0
v= 4
vi=1

#def deltax():
#    print L/(n-vi)
#    return L/(n-vi)
    
#h= deltax()
#print h
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
    return math.exp(-v*(np.pi**2))*math.sin(2*np.pi*k*(2-u*t))
    
# Condição Inicial
def condInic(x):
    return math.sin(2.0*np.pi*k*(x*1.0))
    
# Matriz B
def matrizB():
    x = 0
    matriz = []
    while x<=2:
        if x != 0 and x != 2:
            matriz.append(condInic(x))
#        matriz.append(condCont(x))
        else:
            matriz.append(condCont(x))
        x=x+h
        
    return matriz
     
# X = A*B
def resolve(matrizA, matrizB):
    return np.linalg.solve(matrizA, matrizB)
    

       
X=main()
print X

#salvarresultado
np.savetxt("matrizAl.csv",X , delimiter=",")