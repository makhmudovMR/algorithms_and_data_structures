class Vertex:
    
    def __init__(self, key):
        '''
            Конструктор инициализирует ключ(номер) вершины
            и словарь с объектами которые имеют отношение с текущей вершиной
        '''
        self.id = key
        self.connectTo = {}


    def __str__(self):
        return self.id + ' connectTo:' + str([x.id for x in self.connectTo])

    def addNeighbor(self, nbr, weight=0):
        '''
            Добавляет вершину(соседа) с корым мы имеем отношение
        '''
        self.connectTo[nbr] = weight

    def getConnections(self):
        '''
            Возвращает список всех вершин с которыми мы имеем отношение
        '''
        return self.connectTo.keys()

    def getId(self):
        '''
            Возвращает ID (ключ) вершины
        '''
        return self.id

    def getWeight(self, nbr):
        '''
            Возврщает вес ребра который соединяет текущюю вершину с nbr 
        '''
        return self.connectTo[nbr]


class Graph:

    def __init__(self):
        '''
            Конструктор инициализирует словарь со всеми вершинами графа
            и колличество вершин графа
        '''
        self.vertList = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self, n):
        return n in self.vertList

    def addVertex(self, key):
        '''
            Добавляет вершину в граф 
            инициализируя её под колючом
        '''
        self.numVertices+=1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        '''
            Возращает вершину если она имеется 
        '''
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        '''
            Добавляет ребро между двумя вершинами графа f(from), t(to)
            Если этих вершин изначально не существует то мы их добавляем в граф
        '''
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        '''
            Возвращет все ключи вершин графа
        '''
        return self.vertList.keys()


    

def main():
    g = Graph()
    for i in range(5):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print('({}, {})'.format(v.getId(), w.getId()))


if __name__ == '__main__':
    main()


    