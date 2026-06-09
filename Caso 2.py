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
        CREATE TABLE IF NOT EXISTS eventos (
            id            INT AUTO_INCREMENT PRIMARY KEY,
            dia           INT,
            mes           INT,
            anio          INT,
            nombre_evento VARCHAR(200),
            horario       VARCHAR(50),
            estado        VARCHAR(20),
            fecha         TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

init_tabla()

# ── Programa ──────────────────────────────────────────────────────────────

dia = int(input("Ingrese el dia: "))

while True:
    try:
        mes = int(input("Ingrese el mes: "))
        if mes < 1 or mes > 12:
            print("El mes debe estar entre 1 y 12.")
            continue
        break
    except ValueError:
        print("Ingrese solo numeros.")

anio = int(input("Ingrese el anio: "))

meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio",
         7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
nombreMes = meses[mes]

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    maxDias = 30
elif mes == 2:
    maxDias = 28
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    maxDias = 31
else:
    maxDias = 0

if dia >= 1 and dia <= maxDias and maxDias > 0:
    nombreEvento = input("Ingrese el nombre del evento: ")
    print("Nota: Si es en la tarde o noche use formato 24h")
    horaInicio = int(input("Ingrese hora de inicio (0-23): "))
    minutoInicio = int(input("Ingrese minutos de inicio: "))
    horaFin = int(input("Ingrese hora de fin (0-23): "))
    minutoFin = int(input("Ingrese minutos de fin: "))

    if horaInicio < 12:
        periodo = "AM"
    else:
        periodo = "PM"

    print("Fecha Correcta.")
    print(f"Fecha: {dia}/{nombreMes}/{anio}")
    print(f"Nombre: {nombreEvento}")
    print(f"Horario: {horaInicio}:{minutoInicio} / {horaFin}:{minutoFin} {periodo}")

    horario = f"{horaInicio}:{minutoInicio:02d} / {horaFin}:{minutoFin:02d} {periodo}"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO eventos (dia, mes, anio, nombre_evento, horario, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (dia, mes, anio, nombreEvento, horario, "Correcta"))
    conn.commit()
    cursor.close()
    conn.close()
    print("\n✅ Evento guardado en la base de datos.")

else:
    print("Fecha Incorrecta. Favor verificar e intentar de nuevo.")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO eventos (dia, mes, anio, estado) VALUES (%s, %s, %s, %s)",
        (dia, mes, anio, "Incorrecta")
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Registro guardado en la base de datos.")