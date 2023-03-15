def print_formatted(number):
    # your code goes here
    for i in range(1, number + 1):
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        b = bin(i)[2:]
    print(d.rjust(l), o.rjust(l), h.rjust(l), b.rjust(l))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)