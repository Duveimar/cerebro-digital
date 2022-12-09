# Descuentos para la U de la vida
print ('Universidad de la vida')
print("¿Nombre completo? ", end="")
nombre = input()
nombre_ = nombre . upper()
print(f"completa el formulario para saber cuanto descuento tine para la universidad de la vida, {nombre_}")
print(f"{nombre_} Numero de identificacion?", end="")
numero=int(input())
print("Cual es su edad ?")
edad = int(input())
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
descuento=0

if 18<=edad<=25:
    print(f'hola¡. {nombre_}, 10% de descuento en la matricula por tener {edad} años de edad.')
    print('10%')
    a=10
elif 26<=edad<=35:
    print(f'hola¡. {nombre_}, 5% de descuento en la matricula por tener {edad} años de edad.')
    print('5%')
    b=5
else:
    print(f'hola¡. {nombre_}, no tiene descuentos   {edad} ')
    print('0%')
print("estado civil ? soltero, casado, viudo")
estado_civil=(input())
if estado_civil=='casado':
    print(f'. {nombre_}, 25% de descuento en la matricula por su estado civil de {estado_civil}.' )
    print('25%')
    c=25
elif estado_civil=='soltero':
    print(f'Sr(a). {nombre_},  15% de descuento en la matricula por su estado civil de {estado_civil}.')
    print('15%')
    d=15
elif estado_civil=='viudo':
    print(f'Sr(a). {nombre_}, 20% de descuento en la matricula por su estado civil de {estado_civil}.')
    print('20%')
    e=20
else:
    print(f'Sr(a). {nombre_}, no tiene descuentos  estado civil de {estado_civil}.')
    print('0%')
    l=0
print(' NÚMERO DE HIJOS:')
hijos=int(input())
if hijos==3:
    print(f'Sr(a). {nombre_},  10% de descuento en la matricula por tener {hijos} hijos.' )
    print('10%')
    f=10
elif hijos==2:
    print(f'Sr(a). {nombre_},  7% de descuento en la matricula por tener {hijos} hijos.')
    print('7%')
    g=7
elif hijos==1:
    print(f'Sr(a). {nombre_},  5% de descuento en la matricula por tener {hijos} hijo.')
    print('5%')
    h=5
else:
    print(f'Sr(a). {nombre_}, no tiene descuentos  por tener {hijos} hijos ')
    print('0%')
    m=0
print('Nivel educativo? sena, bachiller,profecional')
educacion =(input())
if educacion=='sena':
    print(f'hola¡. {nombre_}, 10% de descuento en la matricula por pertenecer al {educacion}.' )
    print('10%')
    i=10
elif educacion=='bachiller':
    print(f'hola¡. {nombre_},  15% de descuento en la matricula por ser {educacion}.')
    print('15%')
    j=15
else:
    print(f'hola¡. {nombre_}, sin descuentos en la matricula por ser {educacion}')
    print('0%')
    n=0
salario=int(input('F. Ingrese su salario $: '))
print(f'hola¡.{nombre_},su salario {salario}')
print('-------------------------------------------------------------------')
print('TOTAL DESCUENTO:')
descuento=a+b+c+d+f+g+h+i+j+k+l+m+n
print(f'{descuento} % descuento para la universidad de la vida {nombre_}' )
print('gracias feliz dia')