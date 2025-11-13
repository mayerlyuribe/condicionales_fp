numero = int(input("ingrese un número entre 0 y 15: "))

resultados_bin = []
temporal = numero

while (True):
    if temporal > 0 and temporal <= 15:
        mod = temporal % 2
        resultados_bin.append(mod)
        temporal //= 2
    elif temporal == 0:
        resultados_bin.append(0)
        break;
    else:
        print("número inválido")
        break;

num_invertido = ""

for i in range(0, len(resultados_bin)):
    cont = -i-1
    num_invertido += str(resultados_bin[cont])

print("número en binario:", num_invertido)

#---------------------------------------------

hexa_dicc = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

if numero >=0 and numero <=9:
    print("número en hexadecimal:", numero)
elif numero >=10 and numero <=15:
    print("número en hexadecimal:", hexa_dicc[numero])