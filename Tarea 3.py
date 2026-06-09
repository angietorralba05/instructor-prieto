# Tarea 3
 
altura = int(input("Ingrese la altura: "))
 
print("\nOutput 1:")
for i in range(1, altura + 1):
    print("*" * i)
 
print("\nOutput 2:")
for i in range(1, altura + 1):
    print(" " * (altura - i) + "*" * i)
 
print("\nOutput 3:")
for i in range(altura, 0, -1):
    print("*" * i)
 
print("\nOutput 4:")
for i in range(altura, 0, -1):
    print(" " * (altura - i) + "*" * i)