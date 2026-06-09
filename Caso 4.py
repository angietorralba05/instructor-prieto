# Caso 4 

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))


if c < a or c > b:
    resultado = True
else:
    resultado = False


print(str(resultado).lower())  