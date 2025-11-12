numero = int(input("ingrese un número entre 0 y 15:"))

resultados = []
temporal = numero

while temporal > 0 and temporal <= 15:
    mod = temporal % 2
    resultados.append(mod)
    temporal //= 2

if numero == 0:
    resultados.append(0)

resultados.reverse()
print(resultados)