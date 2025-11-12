valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))

angulo1 = float(input("Ingrese el primer ángulo en grados: "))
angulo2 = float(input("Ingrese el segundo ángulo en grados: "))
angulo3 = float(input("Ingrese el tercer ángulo en grados: "))

if valor1 + valor2 > valor3:
    if angulo1 + angulo2 + angulo3 == 180:
        print("Los valores y ángulos ingresados pueden formar un triángulo.")
    else:
        print("Los valores ingresados pueden formar un triángulo, pero los ángulos no son válidos.")
else:
    print("Los valores ingresados no pueden formar un triángulo.")