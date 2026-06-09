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
        CREATE TABLE IF NOT EXISTS intervalos (
            id        INT AUTO_INCREMENT PRIMARY KEY,
            tipo      VARCHAR(30),
            a         FLOAT,
            b         FLOAT,
            c         FLOAT,
            resultado VARCHAR(10),
            fecha     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_tabla()

# ── Programa ──────────────────────────────────────────────────────────────

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

if c < a or c > b:
    resultado = True
else:
    resultado = False

print(str(resultado).lower())

# ── Guardar en BD ─────────────────────────────────────────────────────────
conn = get_connection()
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO intervalos (tipo, a, b, c, resultado) VALUES (%s, %s, %s, %s, %s)",
    ("punto fuera intervalo", a, b, c, str(resultado).lower())
)
conn.commit()
cursor.close()
conn.close()
print("✅ Resultado guardado en la base de datos.")