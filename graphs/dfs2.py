def dfs_recursive(graph, vertex, visited=[]):
    print(vertex)
    for n in graph[vertex]:
        if n not in visited:
            visited.append(n)
            dfs_recursive(graph, n, visited)


def dfs_iterable(graph, vetrex):
    visited = []
    stack = [vetrex]
    while stack:
        vetrex = stack.pop()
        print(vetrex)
        if vetrex in visited:
            continue
        visited.append(vetrex)
        
        # reverse
        alist = graph[vetrex]
        if alist is not []:
            alist.reverse()


        for n in alist:
            stack.append(n)
    

def main():
    graph = {
        'a': ['b','c','d'],
        'b': ['e', 'f'],
        'e': ['k'],
        'k': [],
        'f': [],
        'c': ['h'],
        'h': ['g'],
        'g': [],
        'd': ['i', 'j'],
        'i': [],
        'j': ['l'],
        'l': []
    }

    dfs_recursive(graph, 'a')
    print('------')
    dfs_iterable(graph, 'a')


main()