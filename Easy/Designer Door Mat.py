# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
a= '.|.'
for i in range(n):
    if(i%2 !=0):
     print((a*i).center(m,'-'))
print('WELCOME'.center(m,'-'))

for i in range(n):
    t=range(n)[-i-1]
    if(i%2 !=0):
     print((t*a).center(m,'-'))