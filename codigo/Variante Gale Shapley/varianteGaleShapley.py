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

def getBandasDic(cant, nombre):

    rank = defaultdict(dict)
    
    for num in range(1, cant + 1):
        snum = str(num)
        nombreArchivo = DATA_PATH + nombre + "_" + snum + ".dat"
        with open(nombreArchivo) as f:
            preferencias = f.read().splitlines()
        for i, preferencia in enumerate(preferencias):
            rank[snum][preferencia] = i

    print("get " + nombre + " dic ok")
    return rank

def getRecitalesDic(cant, nombre):

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
    ranking[BANDA] = getBandasDic(cantBandas, BANDA)
    ranking[RECITAL] = getRecitalesDic(cantRecitales, RECITAL)

    print("init ok")

    return ranking

def bandaPrefiereEsteRecital(banda, recitalNuevo, recitalesQueToca, prefsPorRecital):
    
    prefiereEsteRecital = False
    prefPorNuevoRecital = prefsPorRecital[recitalNuevo]
    
    for recital in recitalesQueToca:
        pref = prefsPorRecital[recital]
        if prefPorNuevoRecital < pref:
            prefiereEsteRecital = True
            break

    return prefiereEsteRecital

def cambiarRecitalDeBanda(recitalesXbanda):
    print("a")

def match(recitalesPrefXBanda, bandasPrefXRecital, maxBandasXRecital, maxRecitalesXBanda):

    # [Recital, Bandas]
    bandasXrecital = dict()
    # [Banda, Recitales]
    recitalesXbanda = dict()

    recitalesLibres = bandasPrefXRecital.keys()

    while (len(recitalesLibres) > 0):
        recital = recitalesLibres.pop(0)
        bandasPreferidas = bandasPrefXRecital[recital].keys()
        bandasXrecital[recital] = list()
        while (len(bandasPreferidas) > 0):
            bandasEnRecital = bandasXrecital[recital]
            if (len(bandasEnRecital) < maxBandasXRecital):
                for i in bandasPreferidas:
                    banda = bandasPrefXRecital[recital].pop(i)
                    if banda in recitalesXbanda:
                        # la banda ya esta asociada a uno o mas recital/es
                        recitalesQueTocaBanda = recitalesXbanda[banda]
                        if (len(recitalesQueTocaBanda) < maxRecitalesXBanda):
                            bandasXrecital[recital].append(banda)
                            recitalesXbanda[banda].append(recital)
                        else:
                            if (bandaPrefiereEsteRecital(banda,
                                                        recital,
                                                        recitalesXbanda[banda],
                                                        recitalesPrefXBanda[banda])):

                                cambiarRecitalDeBanda(recitalesXbanda)

                                print("ea")
                    else:
                        recitalesXbanda[banda] = list()
                        recitalesXbanda[banda].append(recital)
                        bandasXrecital[recital].append(banda)
                else:
                    # Recital esta lleno -> Paso al siguiente
                    break



    print("match ok")

def main():

    argv = [False,10,10,2,2] # TODO: Delete this test line

    if(len(argv) < 5):
        print ("cantidad de parametros incorrecta")
        return
    else:

        # Parse arguments

        generarArchivos = argv[0] 
        cantRecitales = int(argv[1]) #N
        cantBandas = int(argv[2]) #M
        maxBandasXRecital = int(argv[3]) #X
        maxRecitalesXBanda = int(argv[4]) #Y

        # Initialize data:
        #   - write/read files
        #   - get rankings dictionary:
        #       - [BAND_ID][PREFERENCE ORDER] = RECITAL_ID
        #       - [RECITAL_ID][PREFERENCE ORDER] = BAND_ID

        data = init(generarArchivos, cantRecitales, cantBandas, 
            maxBandasXRecital, maxRecitalesXBanda)

        bandasRanking = data[BANDA]
        recitalesRanking = data[RECITAL]

        # Perform matching
        
        match(bandasRanking, recitalesRanking, 
            maxBandasXRecital, maxRecitalesXBanda)

main()