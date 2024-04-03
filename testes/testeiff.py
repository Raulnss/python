n = int(input("incira numero: "))
n1 = int(input("incira numero: "))
if n > n1:
    n=n+1
    for i in range(n1, n):
        print(str(i))
else:    
    n1=n1+1
    for i in range(n, n1):
        print(str(i))