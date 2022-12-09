#***Vamos a diseñar un formulario para la asignación de descuentos para la matricula en la universidad de la vida, y consistirá en preguntarnos NOMBRES Y APELLIDO, DOCUMENTO, EDAD, ESTADO CIVIL, NUMERO DE HIJOS, NIVEL EDUCATIVO, SALARIO.

#Donde cada variable deberá tomar todos los datos en con un patrón especifico mayúsculas y deberá contener las siguiente condicionales

#Si tienes entre 18 y 25 años descuento del 10%, entre 26 y 35 descuento del 5% y mayor a 35 no tiene descuento

#Si eres casado 25%, viudo, 20%, soltero 15%, unión libre no tiene descuento

#Número de hijos 3 hijo 10%, 2 hijos 7%, 1hijos 5% y 0 hijos 0

#Nivel educativo profesional no tiene descuento; bachiller 15%; Sena 10%

#Se debe imprimir en pantalla los descuentos los cuales le se asignaron
#Total, de descuento
print("Bienbenido A la universidad de la vida""     ""Para su inscripsion debera llenar un formulario que le asignara descuentos en la matricula")
print("Su nombre 'si tiene dos ingreselos uno despues de otro")
print("¿Cómo se llama? ", end="")
nombre = input().upper()
print(
    f"Me alegro de conocerle, {nombre} ahora ingresa sus apeliidos de la misma forma uno despues de otro  ", end="")
apellido = input().upper()
print(f"{nombre} {apellido} cual es su numero de identificacion? ")
identi = int(input())
print(f"{apellido} {nombre}  ID: {identi}")
print(f"{nombre} que edad tienes?  ", end=" tengo  ")
a=0
b=0
edad = int(input())
if  26<= edad  <=35:
    print(" siguiente pregunta ")
    a=5
elif  18<= edad  <=25:
    print("continua  ")
    b=10
else  :
    print("continua completando las siguientes preguntas ", end="")    
#print(f"{edad}")
descuento = a or b
print(f"su descuento es de {descuento}%")
d=0
e=0
f=0
print(f"porfavor indica tu estado sivil actual: casado,soltero,viudo,union libre     {nombre} ", end="")
estado_civil=(input()).upper()
if estado_civil=='casado':
    print(f'{nombre}  felicidades estas   {estado_civil}.' )
    d=25
elif estado_civil=='soltero':
    print(f'Sr(a). {nombre}  felisidades {estado_civil}.')
    e=15
elif estado_civil=='viudo':
    print(f'Sr(a). {nombre}continua con la siguiente pregunta {estado_civil}.')
    print('20%')
    f=20
elif estado_civil=='union libre':
    print(f'Sr(a). {nombre}  felisidades {estado_civil}.') 
descuento = a+b+d+f
print(f"su descuento es de {descuento}%")      
g=0
h=0
i=0    
print(f"{apellido}  tiene hijos 1,2,3 o mas ?",end="")  
hijos=input()      
if hijos=="3":
    print("garan familia")
    g=10
elif hijos =="2":
    print("continua con el formulario")
    h=7
elif hijos=="1":
    print("el eredero")
    i=5 
descuento = a+b+d+f+g+h+i
print(f"su descuento es de {descuento}%")    
print(f"Cual es su nivel educativo {nombre}", end="")     
j=0
k=0     
educacion=input(f"su nivel educativo es : profecional, sena, bachiller  ").upper()
if educacion=="sena":
    print(f"hola colega {nombre} soy Duveimar practicando")
    j=10
elif educacion=="bachiller":
    print(f"eres bachiller titulado bien {apellido} ")
elif educacion=="profecional":
    print(f"Eres todo un profecional{apellido}{nombre}")
    k=15                         
descuento = a+b+d+f+g+h+i+j+k
print(f"su descuento para la matricula en la universidad de la vida es: {descuento}% total descuento")
print(f"NOMBRE COMPLETO {nombre} {apellido} EDAD {edad} ESTADO CIVIL {estado_civil}NIVEL EDUCATIVO {educacion} HIJOS {hijos} DESCUENTO TOTAL {descuento}%")