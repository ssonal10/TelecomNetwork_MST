## Data Structures and Algorithms Design
## Assignment 2  PS2 - [Telecom Network with a MST]
## Group Number# 258


''' The Below Class define a vertex of a graph'''
class Vertex:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return  self.name

''' The Below Class define a edge of a graph'''
class Edge:
    def __init__(self, start: Vertex, end: Vertex, weight: int):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return "(% s,% s)" % (self.start,self.end)

'''Class to represent a graph
   Stores the vertices count and all the edges
   Defined Utility functions to run the Kruskal's MST algorithm
   Defined Kruskal's MST algorithm to find the MST edges
   This Class is for respresenting graph. It contains set of vertices and list of edges
'''
class Graph:
    def __init__(self, v, e):
        self.vertices = v
        self.edges = e

    '''This method returns the vertex object by name'''
    def vertex_from_name(self, name: str) -> Vertex:
        """ Return vertex by name """
        return next((v for v in self.vertices if v.name == name), None)

    '''This method add the edges to list of edges and vertices to the set of vertices''' 
    def add_edge(self, start, end, weight):
        """ Adding the edge to the graph and vertices to the unique set"""
        if isinstance(start, str):
            startVertex = self.vertex_from_name(start)
            if(startVertex == None):
                startVertex=Vertex(start)
                self.vertices.add(startVertex)

        if isinstance(end, str):
            endVertex = self.vertex_from_name(end)
            if(endVertex==None):
                endVertex = Vertex(end)
                self.vertices.add(endVertex)
       
        self.edges.append(Edge(startVertex, endVertex, weight))
    
    ''' This Method takes disjoint set of vertices 
        Joins the two sets if v1 and v2 belong to different sets
        If v1 and v2 belong to same set returns false
    '''
    def union(self, lst, v1, v2):
        """ Given a list of disjoint sets of vertices, merges v1 root set with v2 root set and returns merged sets."""
        a, b = [], []
        # Find roots of both elements
        for i in lst:
            if v1 in i:
                a = i
            if v2 in i:
                b = i
        # Same root, cannot merge
        if a == b:
            return False
        a.update(b)
        lst.remove(b)
        return lst

    '''This method contains the algorithm to find the minimum spanning tree for the Graph'''  
    def MST(self):
        """ Returns the MST """
        self.tree = Graph([], [])
        self.sets = [{v} for v in self.vertices]
        numVertices = len(self.sets)
       
        self.tree.vertices = self.vertices
        self.sorted_edges = sorted(self.edges, key=lambda x: x.weight)
        for edge in self.sorted_edges:            
            self.tree.edges.append(edge)
            _temp = self.union(self.sets, edge.start, edge.end)
            """if vertices already connected remove the edge else keep it added"""
            if _temp == False:
                 self.tree.edges.remove(edge)
            else:                 
                self.sets = _temp

            edgeCount =  len(self.tree.edges)
            """if all the vertices are covered for a MST"""
            if(edgeCount == (numVertices-1)):
                break            
        
        return self.tree

import os
import sys
'''This is the main method contains the logic to populate the graph and find its Minimum spanning tree'''
if __name__ == "__main__":

    g = Graph(set(), [])
    filename = os.getcwd()+"/"+"inputPS2.txt"
    inputFile = open(filename,'r')
    for line in inputFile.readlines():
        arr = line.split("/")
        g.add_edge(arr[0].strip(),arr[1].strip(),int(arr[2]))

    inputFile.close
    
    edgeList = g.MST().edges
    edge_string = ''
    minSum = 0
    for i in range(len(edgeList)-1):
        edge_string +=str(edgeList[i])+", "
        minSum += edgeList[i].weight
    
    edge_string +=str(edgeList[-1])
    minSum += edgeList[-1].weight
    
    orig_stdout = sys.stdout
    filename = os.getcwd()+"/"+"outputPS2.txt"
    f = open(filename, 'w')
    sys.stdout = f
    print("The offices can be connected as")
    print (edge_string)
    print("The minimum cost of connecting the offices is " + str(minSum))

    sys.stdout = orig_stdout
    f.close()
   