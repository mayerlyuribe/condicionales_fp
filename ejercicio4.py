
diccionario_tareas = {}

for i in range(1, 3):
    tarea = input("ingrese el nombre de la tarea " + str(i) + ": ")
    ponderacion = float(input("ingrese la ponderación de la tarea " + tarea + " (%): "))
    nota = float(input("ingrese la nota obtenida en la tarea " + tarea + "(0.0 - 5.0): "))
    diccionario_tareas[tarea] = ponderacion, nota
    print("-------------------------")

nota_final = 0
ponderacion_total = 0

for clave in diccionario_tareas:
    ponderacion, nota = diccionario_tareas[clave]
    print("tarea:", clave)
    print("ponderación:", ponderacion, "%")
    print("nota obtenida:", nota,"\n")
    nota_final += (ponderacion * nota) / 100
    ponderacion_total += ponderacion

if nota_final >= 4.5 and nota_final <= 5.0:
    desempeño = "excelente"
elif nota_final >= 3.0 and nota_final < 4.5:
    desempeño = "bueno"
elif nota_final >= 2.5 and nota_final < 3.0:
    desempeño = "regular"
else:
    desempeño = "deficiente"

print("nota final del curso:", nota_final)
print("ponderación total evaluada:", ponderacion_total, "%")
print("desempeño final:", desempeño)
