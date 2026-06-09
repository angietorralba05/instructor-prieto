import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",  # Cambia esto
        database="ejercicios_sena"
    )

def init_tablas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maquina_productos (
            id     INT AUTO_INCREMENT PRIMARY KEY,
            codigo INT UNIQUE,
            nombre VARCHAR(100),
            precio INT,
            stock  INT DEFAULT 5
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS maquina_ventas (
            id              INT AUTO_INCREMENT PRIMARY KEY,
            codigo_producto INT,
            nombre_producto VARCHAR(100),
            precio          INT,
            efectivo        INT,
            cambio          INT,
            fecha           TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def cargar_productos_default():
    conn = get_connection()
    cursor = conn.cursor()
    productos_default = [
        (21, "Papas limón",        2500, 5),
        (26, "Plátanitos Maduros", 2600, 5),
        (32, "Ponqué Gala",        1900, 5),
        (36, "Maní Salado",        2100, 5),
        (38, "CocaCola Lata",      4500, 5),
        (41, "Seven Up Lata",      3900, 5),
    ]
    for cod, nom, precio, stk in productos_default:
        cursor.execute(
            "INSERT IGNORE INTO maquina_productos (codigo, nombre, precio, stock) VALUES (%s, %s, %s, %s)",
            (cod, nom, precio, stk)
        )
    conn.commit()
    cursor.close()
    conn.close()

init_tablas()
cargar_productos_default()

# ── Cargar productos y stock desde BD ────────────────────────────────────
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT codigo, nombre, precio, stock FROM maquina_productos")
filas = cursor.fetchall()
cursor.close()
conn.close()

productos = {fila[0]: (fila[1], fila[2]) for fila in filas}
stock     = {fila[0]: fila[3]            for fila in filas}

# ── Variables ─────────────────────────────────────────────────────────────
habilitada = True

denominaciones = {5000: "Billetes de Cincomil", 2000: "Billetes de Dosmil",
                  1000: "Billetes de Mil",       500:  "Monedas de Quinientos",
                  200:  "Monedas de Doscientos", 100:  "Monedas de Cien"}

# ── Programa ──────────────────────────────────────────────────────────────

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
                        cantidad = int(input("Cantidad: "))
                        stock[c] += cantidad
                        conn = get_connection()
                        cursor = conn.cursor()
                        cursor.execute(
                            "UPDATE maquina_productos SET stock = stock + %s WHERE codigo = %s",
                            (cantidad, c)
                        )
                        conn.commit()
                        cursor.close()
                        conn.close()
                        print(f"{productos[c][0]}: {stock[c]} unidades")
                    else:
                        print("Código inválido.")
            elif d == "3":
                for c, (n, p) in productos.items():
                    print(f"  {c} {n:<22} ${p}  Stock:{stock[c]}")
            elif d == "4": break

    elif op == "2":
        if not habilitada:
            print("Máquina deshabilitada.")
            continue
        for c, (n, p) in productos.items():
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
            cambio_original = cambio
            for d, nombre in denominaciones.items():
                cant = cambio // d
                if cant: print(f"{cant} {nombre}")
                cambio -= cant * d
            stock[c] -= 1
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE maquina_productos SET stock = stock - 1 WHERE codigo = %s", (c,)
            )
            cursor.execute("""
                INSERT INTO maquina_ventas (codigo_producto, nombre_producto, precio, efectivo, cambio)
                VALUES (%s, %s, %s, %s, %s)
            """, (c, n, p, e, cambio_original))
            conn.commit()
            cursor.close()
            conn.close()
        print("Gracias por su Compra.")

    elif op == "3":
        print("¡Hasta luego!"); break