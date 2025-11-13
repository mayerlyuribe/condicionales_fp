numero = int(input("ingrese un número entre 0 y 15: "))

resultados = []
temporal = numero

while (True):
    if temporal > 0 and temporal <= 15:
        mod = temporal % 2
        resultados.append(mod)
        temporal //= 2
    elif temporal == 0:
        resultados.append(0)
        break;
    else:
        print("número inválido")
        break;

num_invertido = ""

for i in range(0, len(resultados)):
    cont = -i-1
    num_invertido += str(resultados[cont])

print("número en binario:", num_invertido)