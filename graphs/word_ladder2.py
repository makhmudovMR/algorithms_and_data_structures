from pythonds.graphs import Graph
from pythonds.basic import Queue

def word_ladder():
    file_name = 'text.txt'
    buckets = {}
    graph = Graph()

    file = open(file_name, 'r')

    for line in file:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in buckets:
                buckets[bucket].append(word)
            else:
                buckets[bucket] = [word]
    for bucket in buckets:
        for word1 in buckets[bucket]:
            for word2 in buckets[bucket]:
                if word1 != word2:
                    graph.addEdge(word1, word2)
    print(graph)
    return graph

def bfs(graph):
    queue = Queue()
    visited = []
    start = graph.getVertex('FOOL')
    queue.enqueue(start)
    while queue.size() > 0:
        curr = queue.dequeue()
        print(curr.id)
        if curr not in visited:
            for nbr in curr.getConnections():
                queue.enqueue(nbr)
            visited.append(curr)

bfs(word_ladder())
