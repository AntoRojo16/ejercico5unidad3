from ClaseMenu import Menu
from ClaseUsado import Usado
from ClaseNuevo import Nuevo
from ClaseDecodificador import ObjectEnconder
import os
if __name__=='__main__':
    Json=ObjectEnconder()
    Diccionario=Json.LeerArchivo('C:/Users/ThinkPad T420/Desktop/Mis cosas/FCEFN/POO/Unidad 3/2020/Practica/Ejercicio 6/vehiculos.json')
    vehiculos=Json.DecodificarDiccionario(Diccionario)
    menu=Menu()
    ban=False
    while not ban:
        os.system('cls')
        print("1. Insertar vehiculo")
        print("2. Agregar vehiculo")
        print("3. Mostrar tipo de objeto")
        print("4. Modificar precio base")
        print("0. Salir")
        op=int(input("Ingrese su opcion."))
        menu.opcion(op,vehiculos)
        ban= op == 0
