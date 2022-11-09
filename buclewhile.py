num=1
print(
    "cuantas edades promedio")
cantidad= int(input())
prom=0
while num <= cantidad:
    print("ingrese la edad numero:", num)
    edad= float(input())
    prom=prom+edad
    num+=1
print("la edad promedio es igual a :",round(prom/cantidad, 2))