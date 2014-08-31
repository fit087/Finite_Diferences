# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 18:56:18 2014

@author: Raisa Cardoso
"""
import math 
import numpy as np

def main():
#Calculando o X a cada passo de tempo (0,05, 0,025, 0,0125)
#    E=0
    soma=0
    A=matrizIdent()
    B=matrizB()
    resultado=[]
    resultado.append(B)
    #mudando o tempo de acordo com o deltat - para que chegue até t=1
    for i in range(1,2000):
       B=resolve(A,B)
       resultado.append(B)
#       if i==300:
       plot(B)
#        b2=B
    an=calculo()
    i=0
    for i in range(0,n):
        diferenca=B[i]-an[i]
        soma+=diferenca
    E=h*np.square(soma)
        
#       sum+=(B-calculo())
#       E=h*np.square(sum)
    return  resultado,E,soma#,#b2
    

    
    
    
#def main ():
n= 21
#    A = forme_matriz(n,m)
kt=0.0005

d=0.025
L=2.0
u=1.0
#h=L/(n)
h=L/(n-1)
print h
k = 1.0
#pi = 3.141592653
t = 0
tf=1
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
    return -((u*kt)/(2*h)-(d*kt)/(h**2))
    
# Coeficiente B
def coefB():
    return (kt/kt)+(2*d*kt)/(h**2)
    
# Coeficiente C
def coefC():
    return -((u*kt)/(2*h)+(d*kt)/(h**2))
        
# Matriz Identidade
def matrizIdent():
    return coefB()*np.eye(n, k=0)+(coefA())*np.eye(n, k=-1)+(coefC())*np.eye(n, k=1)
    
# Condição de Contorno
def condCont(x):

    return math.exp(-v*(np.pi**2)*d*(k**2)*t)*math.sin(2*np.pi*k*(x-u*t))
#    return math.exp(1)*math.sin(2*np.pi*k*(x-u*t))
    
# Condição Inicial
def condInic(x):
    return math.sin(2.0*np.pi*k*(x*1.0))
    
##Solução analítica
def gerarAnalitica(x):
#    x=0
    return math.exp(-v*(np.pi**2)*d*(k**2)*t)*math.sin(2*np.pi*k*(x-u*tf))
    
def calculo():  
    x= 0
    matriz1 = [] 
#    while x<=2:
    for i in range(0,n):
        x=i*h
        matriz1.append(gerarAnalitica(x)) 
        x=x+h
        
    return matriz1
        

    
# Matriz B
def matrizB():
#    x = 0
    matriz = []
#    while x<=2:
    for i in range(0,n):
        x=i*h
#        if x != 0 and x != 2:
#        matriz.append(condInic(x))
        matriz.append(condCont(x))
#    else:
#            matriz.append(condCont(x))
        x=x+h
        
    return matriz
    
     
# X = A*B
def resolve(matrizA, matrizB):
    return np.linalg.solve(matrizA, matrizB)
    

       
#X,E,soma,B2=main()
X,E,soma=main()
print X

#salvarresultado
np.savetxt("matrizAl.csv",X , delimiter=",")
