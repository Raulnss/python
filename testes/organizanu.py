n1 = int(input("incira um numero: "))
n2 = int(input("incira outro numero: "))
n3 = int(input("incira outro numero: "))
if n1 >= n2 and n1 >= n3 and n2 >= n3:
    print(str(n1)+" "+str(n2)+" "+str(n3))
elif n2 >= n1 and n2 >= n3 and n1 >= n3:
    print(str(n2)+" "+str(n1)+" "+str(n3)) 
elif n3 >= n2 and n3 >= n1 and n1 >= n2:
    print(str(n3)+" "+str(n1)+" "+str(n2)) 
elif n1 >= n2 and n1 >= n3 and n3 >= n2:
    print(str(n1)+" "+str(n3)+" "+str(n2))  
elif n2 >= n1 and n2 >= n3 and n3 >= n1:
    print(str(n2)+" "+str(n3)+" "+str(n1))
elif n3 >= n2 and n3 >= n1 and n2 >= n1:
    print(str(n3)+" "+str(n2)+" "+str(n1)) 
else:
    print("deu errado")                 