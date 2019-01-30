import numpy as np

def main():
    matrix = np.array([[i for i in range(1,4)] for _ in range(5)])
    print(matrix)
    print('------')
    col = 0
    while col < len(matrix[col]):
        el = 0
        while el < len(matrix):
            print(matrix[el][col])
            el+=1
        col+=1

            
if __name__ == "__main__":
    main()
