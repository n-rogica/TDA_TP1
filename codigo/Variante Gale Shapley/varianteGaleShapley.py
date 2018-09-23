from sys import argv
import random
import os

def genArchivosRandom(cantRecitales, cantBandas,
maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda):
    print ("archivos random")

    #creo archivos de recitales
    for numRecital in range(1,cantRecitales+1):
        nombreArchivo = "recital_" + str(numRecital)
        archivo = open(nombreArchivo, "w")
        preferencias = random.sample(range(1,cantBandas+1),cantBandas)
        for preferencia in preferencias:
            archivo.write(str(preferencia) + os.linesep)
        archivo.close()

    #creo archivos de bandas
    for numBanda in range(1,cantBandas+1):
        nombreArchivo = "banda_" + str(numBanda)
        archivo = open(nombreArchivo, "w")
        preferencias = random.sample(range(1,cantRecitales+1),cantRecitales)
        for preferencia in preferencias:
            archivo.write(str(preferencia) + os.linesep)
        archivo.close()



def main():

    '''verifico que se ingresaron todos los parametros'''
    if(len(argv) < 5):
        print ("cantidad de parametros incorrecta")
        return
    else:
        cantRecitales = int(argv[1])
        cantBandas = int(argv[2])
        maxBandasDistintasAContratar = int(argv[3])
        maxRecitalesAParticiparPorBanda = int(argv[4])
        genArchivosRandom(cantRecitales, cantBandas,
            maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda)
        






main()
