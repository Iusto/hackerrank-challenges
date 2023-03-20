# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s,n = input().split()
p = sorted(list(permutations(s,int(n))))
for i in p :
    print("".join(i))