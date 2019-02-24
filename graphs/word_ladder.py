from pythonds.graphs import Graph
import pythonds

def buildGraph():
    d = {}
    g = Graph()

    # формируем корзины из слов
    wfile = open('forGraph.txt', 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    
    return g

print(buildGraph())