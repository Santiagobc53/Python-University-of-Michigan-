import re

# Abrimos el archivo
with open("regex_sum_2224654.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

# Extraemos todos los números con expresión regular
numeros = re.findall(r'[0-9]+', texto)

# Convertimos a enteros y sumamos
suma_total = sum(int(n) for n in numeros)

# Mostramos el resultado
print("Suma total:", suma_total)
