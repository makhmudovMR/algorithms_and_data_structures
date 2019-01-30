a, b = list(map(int, input().split()))

res = abs(a - b)
mod_days = int(((a+b) - res) / 2)
if res>1:
    days = res//2
else:
    days=0
print("{} {}".format(mod_days, days))
