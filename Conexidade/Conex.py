#!/usr/bin/env python3

import random
from random import choice
import numpy as np


class Conex():
    def __init__(self):
        self.initvariables() # inicializacao de variaveis


    def initvariables(self):
        self.V_temp = ['a','b','c','d','e','f','g','h','i','j']
        self.V = set(['a','b','c','d','e','f','g','h','i','j'])
        self.R = {}
        #    G =  a  b  c  d  e  f  g  h  i  j
        self.G =[[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
                ]
        
        for i in self.V:
            self.R[i] = set()
        self.conexComponet = []

    """
    " Return the conex components of a graph
    """
    def calcConex(self):

        #chooses a vertice of V
        v = choice(list(self.V))

        #add vertice v to dict R, with key 'v'
        self.R[v].add(v)

        #initialize Y as a set
        Y = set()

        #while there's a neighboor vertice
        while(len(self.neighboors(self.R[v]) - self.R[v])!=0):
            
            #Calculate the neighboors of R(v) - R(v)
            Y = self.neighboors(self.R[v]) - self.R[v]

            #R(v) = R(v) U Y
            self.R[v] = self.R[v] | Y

            #add R(V) to array conexComponent
            self.conexComponet.append(list(self.R[v]))

        #set as R(v)
        Y = self.R[v]

        #set V as the difference between the sets V and Y
        self.V = self.V - Y        
        
        #if there's vertices left in V
        if (len(self.V)!=0):
            self.calcConex()
        
        return self.conexComponet
        

    """
    " V = set of Vertices
    " Returns = set of Neighboors of v
    """
    def neighboors(self,V):
        neighboors_vertices = set() # initializes vertices' array
        for i in V:            
            pos = self.V_temp.index(i) # position of vertice in array        
            vertices = self.G[pos] # adjacency of vertice v            
            for i in range(0,len(vertices)): 
                if(vertices[i]==1):
                    neighboors_vertices.add(self.V_temp[i])
        return neighboors_vertices
    
if __name__ == '__main__':
    Conex = Conex()
    print("Componentes Conexas")
    print(Conex.calcConex())