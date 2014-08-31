# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 21:59:59 2014

@author: Mauricio
"""

# Trbalho Diferencas Finitas

#Importacao de Pacotes

import numpy as np
import scipy as spy
import matplotlib as mpl

# Definicao de constantes e variaveis

A= 1
G= 1
u= 1
D= 0.05
L= 2

# 1.Dependencia do erro com dt variavel e dx fixo 

#Definicao dos delta t
dt= [0.05, 0.025, 0.0125]
MtxBanal= []
MtxB= []
## Definir pocisao para estabelecer delta t (paso transisao no tempo)
for dtj in array(range(len(dt))):
    k= dt[dtj]
    m= int(1/k)
    print "Com k= ", k, "então m= ", m
    if dtj== 0:
        j= array(range(m+1))
        print "Gera-se uma sequencia j=", j
        tj= j*k
        print "Portanto, os valores discretizados de tj= ", tj
        savetxt("Mtx_t1.txt",tj)
        
        # Com dx fixo
        dx= [21]
        n= dx[0]
        h= float(L/((n-1)))
        print"Com n=", n, "então h= ", h
        i = array(range(n))
        print "Gera-se uma sequencia i= ", i
        xi= i*h
        print "Portanto, os valores discretizados de xi= ", xi
        savetxt("Mtx_xi.txt",xi)
        
        for j in array(range(m+1)):
            k
            h
            # Solução Analitica
            tj[j]
            xi[i]
            Banali= (e**(-4*(pi**2)*D*(G**2)*(tj[j]))*(np.sin(2*pi*G*(xi[i]-(u*tj[j])))))
            #plot(Banali)
            MtxBanal= np.append(MtxBanal, Banali)
            print "Com k= ", k , " e h= ", h , "as Soluções Analiticas são: "
            MtxBanal
            #plot(Banali)
            savetxt("Mtx_Banal.txt", MtxBanal)
            
            #Sistemas Ax = B
            
            if tj[j] == 0: # C.I.
                print "Con tempo inicial ti= ", tj[j]
                
                B0= A*np.sin(2*pi*G*xi)
                print "B0= ", B0
                #plot(B0)
                savetxt("Mtx_B0.txt", B0)
                
                # Calculo Matriz A e seus Coefs. a, b e c
                print "calculo Matriz A:"
                a= (((u*k)/(2*h))-((D*k)/(h**2)))
                print "Coef. a= ", a
                b= (((2*D*k)/(h**2))+1)
                print "Coef. b= ", b
                c= (((u*k)/(2*h))+((D*k)/(h**2)))
                print "Coef. c= ", c
                MtxA= b*np.eye(n, k=0)+(c)*np.eye(n, k=-1)+(a)*np.eye(n, k=1)
                print "A= ", MtxA,
                print "Fica uma Magtriz A de Coefs. de tamanho: ", len(MtxA)
                savetxt("Mtx_A0.txt", MtxA)
                
                B1= np.linalg.solve(MtxA, B0)

                print "tj= ", tj[j]
                if xi[0]== 0 and xi[-1]== L: # C.C.
                    B1[0]= (e**(-4*(pi**2)*D*(G**2)*(tj[j]))*(np.sin(2*pi*G*(xi[0]-(u*tj[j])))))
                    B1[-1]= (e**(-4*(pi**2)*D*(G**2)*(tj[j]))*(np.sin(2*pi*G*(xi[-1]-(u*tj[j]))))) 
                           
                print "Sln t0 + k => B1= ", B1
                #plot(B1)
                
                MtxB= B0
                print "A Matriz MtxB é: ", MtxB
                MtxB= np.append(MtxB,B1)
                MtxB
                savetxt("Mtx_B.txt", MtxB)
                Bi= B1
                
            else: # Seguintes passos de tempo   
                tj[j]
                print "Para o seguinte passo de tempo ti= ", tj[j]  
                #Bi= B
                print "As C.I. são Bi= ", Bi
                #savetxt("Mtx_Bi.txt", Bi)
                
                a= (((u*k)/(2*h))-((D*k)/(h**2)))
                b= (((2*D*k)/(h**2))+1)
                c= (((u*k)/(2*h))+((D*k)/(h**2)))
                MtxA= b*np.eye(n, k=0)+(c)*np.eye(n, k=-1)+(a)*np.eye(n, k=1)
                len(MtxA)
                savetxt("Mtx_A0.txt", MtxA)
                
                B= np.linalg.solve(MtxA, Bi)
                print "A solução do seguinte passo de tempo é B= ", B
                #plot(B)
                Bi= B
                if xi[0]== 0 and xi[-1]== L: # C.C.
                   Bi[0]= (e**(-4*(pi**2)*D*(G**2)*(tj[j]))*(np.sin(2*pi*G*(xi[0]-(u*tj[j])))))
                   Bi[-1]= (e**(-4*(pi**2)*D*(G**2)*(tj[j]))*(np.sin(2*pi*G*(xi[-1]-(u*tj[j]))))) 
                print " Agora a novas C.I. são Bi= ", Bi
                #plot(Bi)
                MtxB
                MtxB= np.append(MtxB,Bi)
                savetxt("Mtx_B.txt", MtxB)

   
          
             
# 2. Dependencio do erro com dx variavel e dt fixo (Estudo de convergencia de Malha)

#Definicao delta X
dx2= [11, 21]#, 41, 61, 81, 101, 121, 161]

## Definir delta t

dt2= [0.05]

for dxi in array(range(len(dx2))):
    n= dx2[dxi]
    n
    h= float(L/((n-1)))  
    print"Com n=", n, "então h= ", h
    i = array(range(n))
    print "Gera-se uma sequencia i= ", i
    xi2= i*h
    print "Portanto, os valores discretizados de xi= ", xi2
    savetxt("Mtx_xi.txt",xi2)    
    
    # Com dt fixo
    k= dt2[0]
    m= int(1/k)
    print "Com k= ", k, "então m= ", m
    j= array(range(m+1))
    print "Gera-se uma sequencia j=", j
    tj2= j*k
    len(tj2)
    print "Portanto, os valores discretizados de tj= ", tj2
    savetxt("Mtx_t2.txt",tj2)
        
 
    for j in array(range(m)):
        # Solução Analítica 
        tj2[j]
        print "A sln ANAL é"
        Banal2= (e**(-4*(pi**2)*D*(G**2)*(tj[j]))*(np.sin(2*pi*G*(xi2-(u*tj[j])))))
        len(Banal2)
        plot(Banal2)
       
        #Calculo Matriz A
        a= (((u*k)/(2*h))-((D*k)/(h**2)))
        print "Coef. a= ", a
        b= (((2*D*k)/(h**2))+1)
        print "Coef. b= ", b
        c= (((u*k)/(2*h))+((D*k)/(h**2)))
        print "Coef. c= ", c
        MtxA= b*np.eye(n, k=0)+(c)*np.eye(n, k=-1)+(a)*np.eye(n, k=1)
        print "A= ", MtxA
        len(MtxA)
    
        #Calculo Matriz B
        
        B0= A*np.sin(2*pi*G*xi)
        
        
        B0= A*np.sin(2*pi*G*xi)
        print "B0= ", B0
        plot(B0)
        savetxt("Mtx_B0.txt", B0)
        
        # Solucao do Sistema A2x0 = B2    
        B= np.linalg.solve(MtxA, B0)






