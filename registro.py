#registro

import csv
import random

registros = []
dias = 30

horas = 24

class Registro:
    __temperatura = int
    __humedad = int
    __presion = int
    def __init__(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def gettemperatura(self):
        return self.__temperatura
   
    def gethumedad(self):
        return self.__humedad
   
    def getpresion (self):
        return self.__presion    
   
    def escribirarchivo(self):
        with open ('datosmetereologicos.csv', 'w') as archivo:
            for dia in range (1,dias+1):
                for hora in range (1,horas+1):
                    temperatura = round(random.uniform(10, 30),2)
                    humedad = round (random.uniform(0,100),2)
                    presion = round (random.uniform(900,1000),2)
                    archivo.write(f"{dia}\t,{hora}\t,{temperatura}\t,{humedad}\t,{presion} \n")
            archivo.close()

    def crear (self):
        for dia in range (1, dias+1):
            registros_dia =[]
            for hora in range (horas):
                registros_dia.append(None)
            registros.append(registros_dia)     
   
    def cargar (self):
        with open ('datosmetereologicos.csv', "r") as archivo:
            lector = csv.reader(archivo, delimiter= ',')
            next(lector)
            for row in lector:
                dia = int(row[0])
                hora = int(row[1])
                temperatura = float(row[2])
                humedad = float(row[3])
                presion = float(row[4])
                registro = Registro(temperatura, humedad, presion)
                if not registros[dia-1][hora-1]:
                    registros[dia-1][hora-1] =[registro]
                else:
                    registros[dia-1][hora-1].append(registro)
            archivo.close()
    def mostrarregistro(self):
        for dia in range(dias):
            for hora in range(horas):
                registro =  registros[dia-1][hora-1][0]if registros[dia-1][hora-1] else None
                if registro:
                    print(f"Dia {dia+1}, Hora {hora+1}, Temperatura={registro.gettemperatura()}, Humedad={registro.gethumedad()}, Presion={registro.getpresion()}")
    
    def buscar(self,auxdia):
        encontrado = False
        while auxdia < dias and not encontrado:
            if registros[dias-1][horas-1] == auxdia:
                indice = dias
                encontrado = True
        return print("Encontrado")
    def mostrarmatriz(self):
        for dia in range(dias):
            for hora in range(horas):
                if registros[dia-1][hora]:
                    lista = registros[dia-1][hora-1][0]if registros[dia-1][hora-1] else None
                    if lista:
                        print(f"Dia {dia+1}, Hora {hora+1}, Temperatura={lista.gettemperatura()}, Humedad={lista.gethumedad()}, Presion={lista.getpresion()}")

