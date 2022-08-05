import math

proteina = float(input("ingrese los gramos de proteina:\n"))
carbohidratos = float(input("ingrese los gr de carbohidratos:\n"))
grasa = float(input("ingrese los gramos de grasa:\n"))

#calculo de calorias
calorias = 4*(proteina+carbohidratos)+9*grasa

print(f"las calorias totales son: {calorias} ")