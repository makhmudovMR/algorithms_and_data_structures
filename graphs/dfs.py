from pythonds.basic.stack import Stack

class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {} # тут будут храниться ссылки на объекты с которым соеденена данная вершина
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
    
    def getConnections(self):
        return self.connectedTo.keys()

    def __str__(self):
        return '(' + str(self.id) +') connected with ' + str([x.id for x in self.connectedTo])


class Graph:

    def __init__(self):
        self.vertList = {}
        self.coutVert = 0
    
    def addVertex(self, key):
        self.coutVert += 1
        newVert = Vertex(key)
        self.vertList[key] = newVert
        return newVert

    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertecies(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())



def dfs():
    graph = Graph()
    tmp = [('a', 'b'), ('a', 'c'), ('a', 'd'), 
            ('b', 'e'), ('b', 'f'), 
            ('c', 'h'), 
            ('d', 'i'), ('d', 'j'), 
            ('e', 'k'), 
            ('h', 'g'),
            ('j', 'l')]

    for f, t in tmp:
        graph.addEdge(f, t)


    start = graph.getVertex('a')
    print(start)
    process(start)

#dfs realization
def process(curr, visited=[]):
    if curr not in visited:
        print(curr)
        visited.append(curr)
        for item in curr.getConnections():
            process(item, visited)
    

dfs()