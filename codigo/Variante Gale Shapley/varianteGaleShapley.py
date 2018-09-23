from sys import argv
import random
import os

def genArchivosRandom(cantRecitales, cantBandas,
maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda):
    print ("start gen archivos random")

    #creo archivos de recitales
    for numRecital in range(1,cantRecitales+1):
        nombreArchivo = "recital_" + str(numRecital) + ".dat"
        archivo = open(nombreArchivo, "w")
        preferencias = random.sample(range(1,cantBandas+1),cantBandas)
        for preferencia in preferencias:
            archivo.write(str(preferencia) + os.linesep)
        archivo.close()

    #creo archivos de bandas
    for numBanda in range(1,cantBandas+1):
        nombreArchivo = "banda_" + str(numBanda) + ".dat"
        archivo = open(nombreArchivo, "w")
        preferencias = random.sample(range(1,cantRecitales+1),cantRecitales)
        for preferencia in preferencias:
            archivo.write(str(preferencia) + os.linesep)
        archivo.close()

    print ("archivos random gen ok")

def main():

    argv = [10,10,10,10,10]

    '''verifico que se ingresaron todos los parametros'''
    if(len(argv) < 5):
        print ("cantidad de parametros incorrecta")
        return
    else:
        '''N'''
        cantRecitales = int(argv[1])
        '''M'''
        cantBandas = int(argv[2])
        '''X'''
        maxBandasDistintasAContratar = int(argv[3])
        '''Y'''
        maxRecitalesAParticiparPorBanda = int(argv[4])
        genArchivosRandom(cantRecitales, cantBandas,
            maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda)

main()