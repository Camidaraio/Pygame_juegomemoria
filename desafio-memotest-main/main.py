import pygame
from constantes import *

import tablero
import tarjeta
import utils


def terminar_juego(pantalla, mensaje, color):
    '''
    Función que se encarga de mostrar una imagen con el juego terminado al usuario, la funcion deberia cerrar el juego cuando se presiona el espacio.
    Recibe la pantalla, un mensaje y el color de ese mismo
    '''
    pass

def imprimir_superficie(pantalla, superficie, x, y):
    '''
    Función que se encarga de imprimir una superficie que le paso
    Recibe la pantalla, la superficie para imprimir, una posición X y posición Y
    '''
    pass

def terminar_partida(cronometro, cantidad_movimientos, tablero):
    '''
    Verifico si el usuario ganó o perdio la partida
    si se queda sin movimientos o sin tiempo perdió 
    si todas las tarjetas del tablero están descubiertas el jugador gano
    Recibe el cronometro, los movimientos actuales del jugador y el tablero
    Si el jugador gano cambia la pantalla y muestra (VICTORIA O DERROTA DEPENDIENDO DE LO QUE HAYA PASADO)
    Retorna True si la partida termino y False si no lo terminó.
    '''
    pass

# Configuración inicial de pygame
pygame.init()
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption('Los Simpsons Memotest')
clock_fps = pygame.time.Clock() # Creamos un Clock para poder fijar los FPS

esta_corriendo = True

lista_cartas = tablero.generar_lista_tarjetas(CANTIDAD_TARJETAS_H, CANTIDAD_TARJETAS_V, ANCHO_TARJETA, ALTO_TARJETA)
#tarjeta_uno = tarjeta.crear_tarjeta('./recursos/00.png',1,'./recursos/01.png',0, 0, ANCHO_TARJETA, ALTO_TARJETA)

#print(tarjeta_uno)

while esta_corriendo:
    tiempo = clock_fps.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            esta_corriendo = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
            # if tarjeta_uno['rectangulo'].collidepoint(event.pos):
            #     tarjeta_uno['visible'] = True

    pantalla_juego.fill(COLOR_BLANCO)

    for tarjeta_juego in lista_cartas:
        pantalla_juego.blit(tarjeta_juego["imagen_escondida"], tarjeta_juego["rectangulo"])


    # if tarjeta_uno['visible'] == True:
    #     pantalla_juego.blit(tarjeta_uno['imagen_escondida'], tarjeta_uno['rectangulo'])
    # else:
    #     pantalla_juego.blit(tarjeta_uno['imagen'], tarjeta_uno['rectangulo'])


    pygame.display.flip()

pygame.quit()