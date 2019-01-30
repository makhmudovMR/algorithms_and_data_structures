import random

def count_sort(n):
    F = [0] * 10
    while n != 0:
        F[n%10]+=1
        n = n // 10

    print(F)

count_sort(123534514513534590)