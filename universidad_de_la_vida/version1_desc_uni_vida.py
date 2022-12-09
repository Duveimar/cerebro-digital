print ("INGRESE SU NOMBRE") 
nombre= input("Nombre/s enter luego apellido/s ").upper()

while str!=(nombre):
    print("ingrese los datos correctos")
    nombre= input("Nombre/s enter luego apellido/s ").upper()
print("listo")    
apellido=input(f"SU APELLIDO {nombre} ").upper()
nombre_completo=nombre+apellido
#while apellido:   
print(F"GRACIAS {nombre} {apellido} ")
edad = int(input(f"ingresa la edad {nombre}  {apellido} "))

while edad<7 or edad>100:
    print("error edad incorrecta")
    edad = int(input(f"ingresa la edad {nombre}  {apellido} "))
print("listo")






#input("ingrese su nombre completo")
