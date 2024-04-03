n1 = int(input("incira uma nota: "))
n2 = int(input("incira outra nota: "))
r=(n1+n2)/2
if r >= 7:
    print("você esta aprovado")
elif r <= 4:
    print("você esta reprovado")
else:
    print("regular então aprovado")        