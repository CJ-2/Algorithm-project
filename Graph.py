import disjointset as dis
import merge
import counting
import random
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []
    def addEdge(self,s,d,w):
        self.graph.append([w,d,s])
    def addNode(self,value):
        self.nodes.append(value)
    def display(self,s,d,w):
        for w,d,s in self.MST:
            print("s={},d={},w={}".format(s,d,w))
    def kruskal_counting(self):
        i,e = 0,0
        ds = dis.disjointset(self.nodes)
        self.graph = counting.counting_sort(self.graph)
        while e<self.V-1:
            w,d,s = self.graph[i]
            i+=1
            x = ds.find(s)
            y= ds.find(d)
            if x!= y:
                e += 1
                self.MST.append([w,d,s])
                ds.union(x,y)
        self.display(s,d,w)
    def kruskal_merge(self):
        i,e = 0,0
        ds = dis.disjointset(self.nodes)
        self.graph = merge.merge_sort(self.graph)
        while e<self.V-1:
            w,d,s = self.graph[i]
            i+=1
            x = ds.find(s)
            y= ds.find(d)
            if x!= y:
                e += 1
                self.MST.append([w,d,s])
                ds.union(x,y)
        self.display(s,d,w)
