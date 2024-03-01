controlBln = True
computador_escritorioFlt = 3000000
computador_portatilFlt = 2000000
tabletasFlt = 1000000
videobeamFlt = 2000000
televisoresFlt = 1000000

#Valores Finales
cantidad_tv = 0
totales_tv = 0
cantidad_tabletas = 0
totales_tabletas = 0
cantidad_portatil = 0
totales_portatil = 0
cantidad_escritorio = 0
totales_escritorio = 0
cantidad_videobeam = 0
totales_videobeam = 0
import os
while controlBln == True:
    os.system ('cls')
    opcionStr= input('1.Computador de escritorio\n2. Computador portatil\n3.Tabletas\n4. Videobeam\n5. Televisores\n6. FACTURAR\n7. SALIR\n->')
    if opcionStr == '1':
        cantidad_escritorio +=1
        totales_escritorio +=computador_escritorioFlt
    if opcionStr == '2':
        cantidad_portatil +=1
        totales_portatil +=computador_portatilFlt 
    if opcionStr == '3':
        cantidad_tabletas +=1
        totales_tabletas+=tabletasFlt  
    if opcionStr == '4':
        cantidad_videobeam +=1
        totales_videobeam+= videobeamFlt
    if opcionStr == '5':
        cantidad_tv +=1
        totales_tv += televisoresFlt    
    if opcionStr == '6':
        os.system ('cls')
        print('Cantidad de computadores de escritorio......' , cantidad_escritorio , '$' , totales_escritorio)    
        print('Cantidad de computadores portatiles.........' , cantidad_portatil , '$' , totales_portatil  )
        print('Cantidad tabletas...........................' , cantidad_tabletas ,  '$' ,  totales_tabletas)    
        print('Cantidad videobeam..........................' , cantidad_videobeam , '$' , totales_videobeam)
        print('Cantidad de TV..............................' , cantidad_tv, '$' ,  totales_tv)
        print('Total de ventas $' , (totales_videobeam + totales_escritorio + totales_portatil + totales_tv + totales_tabletas))
        enter = input('\<<<ENTER>>>')
        if opcionStr == '7':
            controlBln = False