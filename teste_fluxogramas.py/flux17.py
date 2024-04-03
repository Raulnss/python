n1 = int(input("qual a sua velocidade: "))
if n1 == 80:
    print('tudo certo')
elif n1 > 80:
    print("você foi multado em mais: ",(n1-80)*5)
elif n1 <= 40:
    print('você foi multado')
else:
    print("você esta abaixo do permitido")      