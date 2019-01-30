def main():
    matrix = [[j for j in range(5-i)] for i in range(5)]
    for m in matrix:
        print(m)
    i=0
    while i < len(matrix[0]):
        j=0
        while j < len(matrix)-i:
            print(matrix[j][i])
            j+=1
        i+=1
            
if __name__ == "__main__":
    main()
