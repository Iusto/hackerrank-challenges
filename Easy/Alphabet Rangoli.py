import string
def print_rangoli(size):
    alphabets = list(string.ascii_lowercase)
    nSquare = 2*size-1
    for i in range(nSquare):
        output = ''
        for j in range(nSquare):
            index = max(abs(i-j),abs(i-(nSquare-j-1)))
            if index <= nSquare // 2:
                output += alphabets[index]
            else:
                output += '-'
            if j != nSquare - 1:
                output += '-'
        print(output)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)