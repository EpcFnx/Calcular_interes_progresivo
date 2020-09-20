def calcular_total():
    ahorros = int(input('Ingresar capital inicial \n'))
    medida = str(input('Ingresar medida de tiempo (mes, año, etc.)\n'))
    if medida == 'año':
        interes = 'anual'
    elif medida == 'Año':
        interes = 'anual'
    elif medida == 'Mes':
         interes = mensual
    elif medida == 'mes':
        interes = 'mensual'       
    else:
         print ('¿Eh?')
    if interes == 'mensual':
        medida_pl = 'meses'
    elif interes == 'anual':
        medida_pl = 'años'           
    tasa_interes = float(input('Ingresar la tasa de interés %s en decimales \n' % interes))
    tiempo = int(input('Ingresar cantidad de %s \n' % medida_pl))
    dash =  '=' * 85
    print('Se muestran los valores correspondientes a cada %s' % medida)
    for x in range(0, (tiempo+1)): 
        if x == 0:
            print('|{}|' .format(dash))
            print('| {:^10s} {:>25s} {:>25s} {:>20s} |' .format(medida.upper(), 'INICIAL', 'INTERÉS', 'TOTAL'))
            print('|{}|' .format(dash))
        else:
            interés = ahorros * tasa_interes
            ahorros = ahorros + interés
            inicial = ahorros - interés
            print('| {:^10d} {:>25} {:>25} {:>20} |' .format(x, inicial, interés, ahorros))
    print('|{}|' .format(dash))            




