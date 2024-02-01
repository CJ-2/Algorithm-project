import Graph
import random
g = Graph.Graph(666)
for i in range(1,g.V+2):
    g.addNode('V{}'.format(i))
g.addEdge('V1','V2',random.randint(1,1000))
g.addEdge('V1','V3',random.randint(1,1000))
#--------------------
j = 2
for i in range(2,g.V,2):
    g.addEdge('V{}'.format(i),'V{}'.format(i+1),random.randint(1,1000))
    g.addEdge('V{}'.format(i),'V{}'.format(i+2),random.randint(1,1000))
    g.addEdge('V{}'.format(i+1),'V{}'.format(i+2),random.randint(1,1000))
    j+=3
#----------------------
g.addEdge('V{}'.format(g.V),'V{}'.format(g.V-2),random.randint(1,1000))
g.addEdge('V{}'.format(g.V),'V{}'.format(g.V-1),random.randint(1,1000))
