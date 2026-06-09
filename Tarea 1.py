# Tarea 1
 
num_productores = int(input("Cantidad de productores: "))
 
datos = []  
 
for i in range(1, num_productores + 1):
    print(f"\nDatos productor {i}")
    print(f"{'Año':<6} {'Num_Hect':<12} {'Toneladas_Cosechas'}")
 
    hectareas = []
    toneladas = []
 
    for anio in range(1, 4):
        num_hect = float(input(f"Año {anio} - Hectáreas: "))
        ton = float(input(f"Año {anio} - Toneladas cosechadas: "))
        hectareas.append(num_hect)
        toneladas.append(ton)
 
    datos.append((hectareas, toneladas))
 
print()
 
mejor_productor = -1
mejor_promedio = -1
 
for i, (hectareas, toneladas) in enumerate(datos, 1):
    toneladas_ordenadas = sorted(toneladas, reverse=True)
 
    prom_ton = sum(toneladas) / len(toneladas)
    prom_hect = sum(hectareas) / len(hectareas)
 
    print(f"Productor {i}:")
    print("Lista Ordenada por Toneladas.", end=" ")
    print("  ".join(str(int(t)) for t in toneladas_ordenadas))
    print(f"Promedio Toneladas:{prom_ton:.1f}")
    print(f"Promedio de Hectáreas:{prom_hect:.1f}")
    
 
    
    if prom_ton > mejor_promedio:
        mejor_promedio = prom_ton
        mejor_productor = i
 
print(f"El productor del mejor promedio fue {mejor_productor}")