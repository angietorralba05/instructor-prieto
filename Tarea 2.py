# Tarea 2 
 
productos = {
    21: ("Papas limón",        2500),
    26: ("Plátanitos Maduros", 2600),
    32: ("Ponqué Gala",        1900),
    36: ("Maní Salado",        2100),
    38: ("CocaCola Lata",      4500),
    41: ("Seven Up Lata",      3900),
}
stock = {c: 5 for c in productos}
habilitada = True
 
denominaciones = {5000:"Billetes de Cincomil", 2000:"Billetes de Dosmil",
                  1000:"Billetes de Mil", 500:"Monedas de Quinientos",
                  200:"Monedas de Doscientos", 100:"Monedas de Cien"}
 
while True:
    print("\n1.Distribuidor  2.Cliente  3.Salir")
    op = input("Seleccione: ")
 
    if op == "1":
        while input("Contraseña: ") != "1001":
            print("Incorrecta, intente de nuevo.")
        while True:
            print("\n1.Habilitar/Deshabilitar  2.Agregar  3.Inventario  4.Salir")
            d = input("Opción: ")
            if d == "1":
                habilitada = not habilitada
                print("Máquina", "HABILITADA" if habilitada else "DESHABILITADA")
            elif d == "2":
                while True:
                    c = input("Código (0=salir): ")
                    if c == "0": break
                    c = int(c)
                    if c in productos:
                        stock[c] += int(input("Cantidad: "))
                        print(f"{productos[c][0]}: {stock[c]} unidades")
                    else:
                        print("Código inválido.")
            elif d == "3":
                for c,(n,p) in productos.items():
                    print(f"  {c} {n:<22} ${p}  Stock:{stock[c]}")
            elif d == "4": break
 
    elif op == "2":
        if not habilitada:
            print("Máquina deshabilitada.")
            continue
        for c,(n,p) in productos.items():
            print(f"  {c} {n:<22} ${p}")
        c = int(input("Código: "))
        if c not in productos:
            print("Código inválido."); continue
        n, p = productos[c]
        print(f"El precio de {n} es: ${p}")
        e = int(input("Efectivo: "))
        if e > 10000 or e < p:
            print("Dinero insuficiente o excedido.")
        else:
            cambio = e - p
            for d, nombre in denominaciones.items():
                cant = cambio // d
                if cant: print(f"{cant} {nombre}")
                cambio -= cant * d
            stock[c] -= 1
        print("Gracias por su Compra.")
 
    elif op == "3":
        print("¡Hasta luego!"); break