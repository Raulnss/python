n1 = int(input("incira um numero: "))
op = input("coloque o sinal da operação: ")
n2 = int(input("incira outro numero: "))
if op == "+":
    print("a soma é: ",n1+n2)
elif op == "-":
     print("a subtração é: ",n1-n2)
elif op == "*":
     print("a multiplicação é: ",n1*n2)
elif op == "/":
     print("a divisão é: ",n1/n2)
elif op == "%":
     print("o resto de divisão é: ",n1%n2)
else:
     print("caractere incorreto")                     