# Caso 3 

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

# PROCESO: c esta dentro si es >= a Y <= b
if c >= a and c <= b:
    resultado = True
else:
    resultado = False


print(str(resultado).lower())