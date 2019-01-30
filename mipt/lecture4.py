def is_simple_number(n):

    divizer = 2
    while divizer < n:
        if n%divizer==0:
            return False
        divizer+=1
    return True


print(is_simple_number(19))