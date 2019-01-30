def main():
    n, a, b = map(int, input().split())
    ways = list(input())
    # print(n, a, b)
    # print(ways)

    i = a-1
    j = a-1
    curr = a-1
    cost = 0
    # print(ways[i])
    # print(ways[j])
    # print(ways[b-1])
    
    while 0 < i < len(ways) or 0 < j < len(ways):
        if ways[i] == ways[b-1]:
            print(curr, i)
            cost = abs(curr - i)
        elif ways[j] == ways[b-1]:
            print(curr, j)
            cost = abs(curr - j)
        if 0 < i < len(ways):
            i+=1
        if 0 < j < len(ways):
            j-=1   
    # print(cost)


main()
