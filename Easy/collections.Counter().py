# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
i = int(input())
shoes = Counter(list(map(int, input().split())))
customer = int(input())
result = 0
for i in range(customer) :
    size, price = map(int, input().split())
    if size in shoes and shoes[size] > 0 :
        result += price
        shoes[size] -= 1
print(result)