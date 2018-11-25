from pythonds.basic.stack import Stack


def bc(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    
    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    
    return newString

print(bc(256 , 16))