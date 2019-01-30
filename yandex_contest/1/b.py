def main():
    f = open('input.txt', 'r')
    f2 = open('output.txt', 'w')
    str_ = f.read()
    a, b = map(int, str_.split())
    f2.write(str(a+b))
    f.close()
    f2.close()

main()
