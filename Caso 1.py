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
        CREATE TABLE IF NOT EXISTS empleados (
            id                 INT AUTO_INCREMENT PRIMARY KEY,
            nombre             VARCHAR(100),
            categoria          VARCHAR(20),
            antiguedad         INT,
            sueldo_basico      INT,
            monto_antiguedad   INT,
            sueldo_total       INT,
            porcentaje_aumento INT,
            fecha              TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_tabla()

# ── Programa ──────────────────────────────────────────────────────────────

apellidoNombre = input("Ingrese apellido y nombre: ")
categoria = input("Ingrese categoria (Junior / Semi Senior / Senior): ")
antiguedad = int(input("Ingrese antiguedad en anios: "))


if categoria == "Junior":
    basico = 1500
elif categoria == "Semi Senior":
    basico = 2000
elif categoria == "Senior":
    basico = 2500
else:
    basico = 0


if antiguedad >= 1 and antiguedad <= 5:
    porcentaje = 0.02
elif antiguedad >= 6 and antiguedad <= 10:
    porcentaje = 0.05
elif antiguedad >= 11 and antiguedad <= 20:
    porcentaje = 0.08
elif antiguedad > 20:
    porcentaje = 0.10
else:
    porcentaje = 0


montoAntiguedad = int(basico * porcentaje * antiguedad)
sueldoTotal = basico + montoAntiguedad
porcentajeAumento = int((montoAntiguedad / basico) * 100)


if montoAntiguedad > basico:
    comparacion = "EL EMPLEADO GANA MÁS POR ANTIGÜEDAD QUE POR SU SUELDO BÁSICO."
else:
    comparacion = "EL EMPLEADO GANA MÁS POR SALARIO BÁSICO QUE POR SU ANTIGÜEDAD."


print()
print(f"APELLIDO Y NOMBRE: {apellidoNombre.upper()}")
print(f"CATEGORÍA: {categoria.upper()}")
print(f"SUELDO BÁSICO: $ {basico}")
print(f"ANTIGÜEDAD: {antiguedad} AÑOS")
print(f"MONTO ANTIGÜEDAD: $ {montoAntiguedad}")
print(f"SUELDO TOTAL: $ {sueldoTotal}")
print("OBSERVACIONES:")
print(f"EL EMPLEADO GANA: {basico} SUELDO BÁSICO Y ${montoAntiguedad} DE ANTIGÜEDAD, {comparacion}")
print(f"EL PORCENTAJE DE AUMENTO ES: {porcentajeAumento}%")

# ── Guardar en BD ─────────────────────────────────────────────────────────
conn = get_connection()
cursor = conn.cursor()
cursor.execute("""
    INSERT INTO empleados
        (nombre, categoria, antiguedad, sueldo_basico, monto_antiguedad, sueldo_total, porcentaje_aumento)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""", (apellidoNombre, categoria, antiguedad, basico, montoAntiguedad, sueldoTotal, porcentajeAumento))
conn.commit()
cursor.close()
conn.close()
print("\n✅ Datos guardados en la base de datos.")