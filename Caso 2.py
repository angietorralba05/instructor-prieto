# Caso 2

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
else:
    print("Fecha Incorrecta. Favor verificar e intentar de nuevo.")