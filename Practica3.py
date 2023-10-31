# Practica3
import numpy as np
import os
import random

# Definir personajes, locaciones y armas
personajes = ["Sr. Blanco", "Prof. Plum", "Miss Scarlet", "Col. Mustard", "Sra. Peacock"]
locaciones = ["Casa", "Hotel", "Cocina", "Sala de estar", "Baño"]
armas = ["Cuchillo", "Candelabro", "Llave inglesa", "Cuerda", "Revólver"]

# Función para generar una historia
def generar_historia():
    personaje_culpable = random.choice(personajes)
    locacion_culpable = random.choice(locaciones)
    arma_culpable = random.choice(armas)
    print("Usted puede preguntar 10 veces ya sea: personaje, locacion y arma.")
    print("Una vez terminadas esas 10 veces debe de responder personaje, locacion y arma del asesinato.")
    for i in range(10):
        print("Acerca de qué desea preguntar:")
        print("1-personaje")
        print("2-localizacion")
        print("3-arma")
        menu1 = input("")

        if menu1 == '1':
            print("Acerca de qué personaje quiere saber: ")
            for i in range(5):
                print(i+1, ":", personajes[i])
            submenupersonaje = int(input(""))
            if personajes[submenupersonaje-1] == personaje_culpable:
                print("No se encontraron grabaciones de:", personajes[submenupersonaje-1], "en las cintas de video a la hora del crimen.")
            else:
                print("Sí se encontraron grabaciones de:", personajes[submenupersonaje-1], "en las cintas de video a la hora del crimen.")
        elif menu1 == '2':
            print("Acerca de qué locación quiere saber: ")
            for i in range(5):
                print(i+1, ":", locaciones[i])
            submenulocacion = int(input(""))
            if locaciones[submenulocacion-1] == locacion_culpable:
                print("No se encontraron grabaciones en:", locaciones[submenulocacion-1], "en las cintas de video a la hora del crimen.")
            else:
                print("Sí se encontraron grabaciones en:", locaciones[submenulocacion-1], "en las cintas de video a la hora del crimen.")
        elif menu1 == '3':
            print("Acerca de qué arma quiere saber: ")
            for i in range(5):
                print(i+1, ":", armas[i])
            submenuarmas = int(input(""))
            if armas[submenuarmas-1] == arma_culpable:
                print("No se encontraron grabaciones del arma:", armas[submenuarmas-1], "en las cintas de video a la hora del crimen.")
            else:
                print("Sí se encontraron grabaciones del arma:", armas[submenuarmas-1], "en las cintas de video a la hora del crimen.")

    print("Listo, has agotado tus preguntas.")
    print("Digite el personaje culpable: ")
    for i in range(5):
        print(i, ":", personajes[i])

    submenupersonaje = int(input(""))
    personaje_elegido = personajes[submenupersonaje-1]
    if personaje_elegido == personaje_culpable:
        print(personaje_elegido, "es el culpable.")
    else:
        print("Este no es el personaje culpable.")
    print("Digite la locación culpable: ")
    for i in range(5):
        print(i, ":", locaciones[i])

    submenulocacion = int(input(""))
    locacion_elegida = locaciones[submenulocacion-1]
    if locacion_elegida == locacion_culpable:
        print(locacion_elegida, "es la locación del asesinato culpable.")
    else:
        print("Locación incorrecta.")
    print("Digite el arma del culpable: ")
    for i in range(5):
        print(i, ":", armas[i])

    submenuarma = int(input(""))
    arma_elegida = armas[submenuarma-1]
    if arma_elegida == arma_culpable:
        print(arma_elegida, "es el arma con la que se ejecutó al incauto.")
    else:
        print("Arma incorrecta.")

# Generar una historia
generar_historia()
