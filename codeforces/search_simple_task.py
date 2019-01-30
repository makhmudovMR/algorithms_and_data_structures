n = int(input())
lst_people = list(map(int, input().split()))


if sum(lst_people) != 0:
    print("HARD")
else:
    print("EASY")