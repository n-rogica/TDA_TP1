from sys import argv
import random
import os

DATA_PATH = "data/"
BANDA = "banda"
RECITAL = "recital"

def genArchivoRandom(cant, nombre):
    for num in range(1, cant + 1):
        nombreArchivo = DATA_PATH + nombre + "_" + str(num) + ".dat"
        archivo = open(nombreArchivo, "w")
        preferencias = random.sample(range(1, cant + 1), cant)
        for preferencia in preferencias:
            archivo.write(str(preferencia) + os.linesep)
        archivo.close()

def genArchivosRandom(cantRecitales, cantBandas):
    print ("start gen archivos random")

    genArchivoRandom(cantRecitales, RECITAL)
    genArchivoRandom(cantBandas, BANDA)

    print ("archivos random gen ok")

def getDic(cant, nombre):

    print("get dic ok")

def match(cantRecitales, cantBandas, 
        maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda):

    print("match ok")

def main():

    argv = [True,10,10,10,10] # TODO: Delete this test line

    if(len(argv) < 5):
        print ("cantidad de parametros incorrecta")
        return
    else:
        hayQueGenerarArchivos = argv[0] 
        cantRecitales = int(argv[1]) #N
        cantBandas = int(argv[2]) #M
        maxBandasDistintasAContratar = int(argv[3]) #X
        maxRecitalesAParticiparPorBanda = int(argv[4]) #Y

        if hayQueGenerarArchivos:
            genArchivosRandom(cantRecitales, cantBandas)
        
        match(cantRecitales, cantBandas, 
            maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda)

main()