#coding: utf-8
dicTel={}
def funcionTel():
    nom=input("Dime nombre a introducir: ")
    telefon=input("Dime telefono a introducir: ")
    pregunta=input("Quiere introducir más contactos?")
    if nom in dicTel:
            print ("Error, el nombre está repetido")
    else:
        dicTel[nom]=telefon
    
    while (pregunta=="si" or pregunta=="Si" or pregunta=="SI"):
        nom=input("Dime nombre a introducir: ")
        telefon=input("Dime telefono a introducir: ")
        if nom in dicTel:
            print ("Error, el nombre está repetido")
        else:
            dicTel[nom]=telefon
        pregunta=input("Quiere introducir más contactos?")

funcionTel()
print ("Tu lista de contactos es: ",dicTel)
#Esta es la versión actualizada del programa, compruebo que esta todo correcto