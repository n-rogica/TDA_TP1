from sys import argv
from collections import defaultdict
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

    rank = defaultdict(dict)
    
    for num in range(1, cant + 1):
        snum = str(num)
        nombreArchivo = DATA_PATH + nombre + "_" + snum + ".dat"
        with open(nombreArchivo) as f:
            preferencias = f.read().splitlines()
        for i, preferencia in enumerate(preferencias):
            rank[snum][i] = preferencia

    print("get " + nombre + " dic ok")
    return rank

def init(generarArchivos, cantRecitales, cantBandas, 
        maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda):

    if generarArchivos:
        genArchivosRandom(cantRecitales, cantBandas)

    ranking = defaultdict(dict)
    ranking[BANDA] = getDic(cantBandas, BANDA)
    ranking[RECITAL] = getDic(cantRecitales, RECITAL)

    print("init ok")

    return ranking

def match(bandasRanking, recitalesRanking, 
        maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda):

    print("match ok")

def main():

    argv = [False,10,10,10,10] # TODO: Delete this test line

    if(len(argv) < 5):
        print ("cantidad de parametros incorrecta")
        return
    else:

        # Parse arguments

        generarArchivos = argv[0] 
        cantRecitales = int(argv[1]) #N
        cantBandas = int(argv[2]) #M
        maxBandasDistintasAContratar = int(argv[3]) #X
        maxRecitalesAParticiparPorBanda = int(argv[4]) #Y

        # Initialize data:
        #   - write/read files
        #   - get rankings dictionary:
        #       - [BAND_NUMBER][PREFERENCE ORDER] = RECITAL_NUMBER
        #       - [RECITAL_NUMBER][PREFERENCE ORDER] = BAND_NUMBER

        data = init(generarArchivos, cantRecitales, cantBandas, 
            maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda)

        bandasRanking = data[BANDA]
        recitalesRanking = data[RECITAL]

        # Perform matching
        
        match(bandasRanking, recitalesRanking, 
            maxBandasDistintasAContratar, maxRecitalesAParticiparPorBanda)

main()