def f(string):
    if len(string) < 1:
        return string
    else:
        return f(string[1:]) + string[0]

print(f('the'))