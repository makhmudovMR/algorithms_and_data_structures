polygons = {'Tetrahedron': 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}

n = int(input())
summ = 0
for _ in range(n):
    summ += polygons[input()]
print(summ)
