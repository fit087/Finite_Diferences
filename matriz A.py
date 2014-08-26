# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 20:32:17 2014

@author: Karyta Almeida
"""


#def main ():
n=4
#    A = forme_matriz(n,n)
#    kt=0.05
#    D=0.05
#    h=0.10
#    u=1
c=-4.95
a=-5.05
b=30
A=b*np.eye(n, k=0)+(a)*np.eye(n, k=-1)+(c)*np.eye(n, k=1)

print A
    

#def forme_matriz(lin,col):
#    kt=0.05
#    D=0.05
#    h=0.10
#    u=1
#    c=-4.95
#    a=-5.05
#    b=30
#
#
#
#    matriz = []
#    for i in range(lin):
#        linha = []
#        for j in range (col):
#            ele = float(input("Digite o elemento a%d%d da matriz: "%(i+1,j+1)))
#            linha.append(ele)
#        matriz.append(linha)
#    return matriz
#main ()




#30*np.eye(3, k=0)+(-5.05)*np.eye(3, k=-1)+(-4.95)*np.eye(3, k=1)


    





