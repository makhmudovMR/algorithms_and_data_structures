def toStr(n, base):
    # base основание системы счисления в которую мы хотим конвертиворвать n
    # n число которое мы хотим сконвертировать в 

    convert = '0123456789abcdef'
    if n < base:
        return convert[n] + convert[11]
    else:
        return toStr(n//base, base) + convert[n%base]

print(toStr(3,2))