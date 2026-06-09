import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tu_password",  # Cambia esto
        database="ejercicios_sena"
    )

def init_tabla():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS figuras (
            id      INT AUTO_INCREMENT PRIMARY KEY,
            altura  INT,
            fecha   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_tabla()

# ── Programa ──────────────────────────────────────────────────────────────

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

# ── Guardar en BD ─────────────────────────────────────────────────────────
conn = get_connection()
cursor = conn.cursor()
cursor.execute("INSERT INTO figuras (altura) VALUES (%s)", (altura,))
conn.commit()
cursor.close()
conn.close()
print("\nRegistro guardado en la base de datos.")