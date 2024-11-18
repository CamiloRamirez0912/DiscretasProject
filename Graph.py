class DirectedGraph:
    def __init__(self):
        self.graph_dic = {}
        
    def addNode(self, node):
        if node in self.graph_dic:
            return "node already added"
        self.graph_dic[node] = []
       
    def addEdge(self, edge):
        n1 = edge.getN1()
        n2 = edge.getN2()
        if n1 not in self.graph_dic:
            raise ValueError(f'Node {n1.getName()} not added to the graph')
        if n2 not in self.graph_dic:
            raise ValueError(f'Node {n2.getName()} not added to the graph')
        self.graph_dic[n1].append(n2)
        
    def isNodeIn(self, node):
        return node in self.graph_dic
    
    def getNode(self, nodeName):
        for node in self.graph_dic:
            if nodeName == node.getName():
                return node
        print(f"Node {nodeName} does not exist on the graph")
        
    def getNeighbours(self, node):
        return self.graph_dic[node]
    
    def __str__(self):
        allEdges = ""
        for n1 in self.graph_dic:
            for n2 in self.graph_dic[n1]:
                allEdges += n1.getName() + " -----> " + n2.getName() + "\n"
                
        return allEdges
    
class Edge:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    def getN1(self):
        return self.n1
    def getN2(self):
        return self.n2
    
    def __str__(self):
        return self.n1.getName() + "------>" + self.n2.getName()
    
    
class Node:
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
class UndirectedGraph(DirectedGraph):
    def __init__(self):
        super().__init__()
        
    def addEdge(self, edge):
        DirectedGraph.addEdge(self, edge)
        edgeBack = Edge(edge.getV2(), edge.getV1())
        DirectedGraph.addEdge(self, edgeBack)
        


def buildGrafh(graph):
    g = graph()
    for node in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'): 
        g.addNode(Node(node))
    g.addEdge(Edge(g.getNode('s'), g.getNode('a')))
    g.addEdge(Edge(g.getNode('s'), g.getNode('b')))
    g.addEdge(Edge(g.getNode('s'), g.getNode('c')))
    g.addEdge(Edge(g.getNode('s'), g.getNode('d')))
    
    return g
    


G1 = buildGrafh(DirectedGraph)
print(G1)