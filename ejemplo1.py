#ejercicio 1: Programa que permite capturar una cantidad de numeros y determina cuantos de estos numeros 
#estan en el rango de 10-20

cantidadInt = int(input('¿Cantidad de números?->'))
contadorInt = 1
acumuladorInt = 0
contadornúmerosInt = 0
while contadorInt <= cantidadInt:
    númeroInt = int(input('Ingrese un número ->'))
    if númeroInt >=10 and númeroInt <=20:
        contadornúmerosInt += 1
    contadorInt += 1
print('La cantidad de números en el rango de 10 a 20 son:' , contadornúmerosInt)
        
