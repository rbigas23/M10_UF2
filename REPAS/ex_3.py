n1 = int(input("Introduiex un valor: "))
n2 = int(input("Introduiex un segon valor: "))
nt = n1 if n1 > n2 else n2 if n2 > n1 else n1
print(f"El valor més gran és: {nt}")
