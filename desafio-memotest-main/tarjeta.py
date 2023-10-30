import pygame
from constantes import *


def crear_tarjeta(nombre_imagen: str, identificador: int, nombre_imagen_escondida: str, x: int, y: int, ancho:int, alto:int) -> dict:
    dict_tarjeta = {}
    dict_tarjeta['imagen'] = pygame.image.load(nombre_imagen)
    dict_tarjeta['imagen'] = pygame.transform.scale(dict_tarjeta['imagen'], (ancho, alto))
    dict_tarjeta['imagen_escondida'] = pygame.image.load(nombre_imagen_escondida)
    dict_tarjeta['imagen_escondida'] = pygame.transform.scale(dict_tarjeta['imagen_escondida'], (ancho, alto))
    dict_tarjeta['identificador'] = identificador
    dict_tarjeta['visible'] = False
    dict_tarjeta['descubierto'] = False
    dict_tarjeta['rectangulo'] = dict_tarjeta['imagen'].get_rect()
    dict_tarjeta['rectangulo'].x = x
    dict_tarjeta['rectangulo'].y = y
    return dict_tarjeta

    '''
    Crea una nueva tarjeta
    Recibe como parametro el path donde estan los recursos, el nombre de la imagen y el tamaño que esta debera tener
    Retorna el diccionario que hace referencia a la tarjeta creada
    '''
    #Creo el diccionario de tarjeta
    # pass

def obtener_cantidad_cartas(lista_tarjetas, estado):
    '''
        Funcion que se encarga de obtener la cantidad de cartas que estan visibles ya hayan estado descubiertas o no
        Recibe la lista de listas y un estado (True o False) si es True me devuelve las cartas descubieras sino me devuelve las cubiertas.
        Retorna dicha cantidad
    '''
    #contador
    pass
