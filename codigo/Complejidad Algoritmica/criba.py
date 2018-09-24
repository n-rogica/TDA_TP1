from sys import argv
import datetime

def esPrimo(numero):
    for divisor in range(2,numero):
        if (numero % divisor) == 0:
            return False
    return True

def primosPorFuerzaBruta(max):
    numeros = []
    primos = []

    '''inicializo el vector de numeros'''
    for numero in range(2,max):
        numeros.append(numero)

    '''calculo los primos'''
    for numero in numeros:
        if (esPrimo(numero)):
            primos.append(numero)
    print(primos)

def cribaEratostenes(max):
    '''inicializo el vector de numeros
    suponiendo que todos son primos'''
    numeros = [0 for numero in range(max)]
    primos = []

    '''descarto el 0 y el 1 pues no son primos'''
    for indice in range(2, max):

        if (numeros[indice] == 0):
            numeros[indice] = indice
            primos.append(indice)
        indice2 = 0
        while (indice2 < len(primos) and primos[indice2] <= numeros[indice]
               and indice * primos[indice2] <=  (max- 1)):
            '''descarto aquellos numeros cuyo factor primo de menor valor
            es un primo que ya encontre previamente'''
            numeros[indice * primos[indice2]] = primos[indice2]
            indice2 += 1
    print(primos)

def main():
    if (len(argv) != 3):
        print ("error cantidad de parametros incorrecta")
        return
    else:
        inicio = datetime.datetime.now()
        max = int(argv[1]) + 1
        modo = argv[2].upper()
        if (modo == 'F'):
            primosPorFuerzaBruta(max)
        elif (modo == 'E'):
            cribaEratostenes(max)
        else:
            print ("el modo de ejecucion ingresado es incorrecto")
        fin = datetime.datetime.now()
        ejecucion = fin - inicio
        print("tiempo de ejecucion: (hh:mm:ss:ms) ", ejecucion)
main()
