from constantes import *
import tarjeta
import random

def crear_tablero():
    '''
    Crea un diccionario con toda la informacion necesaria para el tablero, creando la lista de tarjetas y todos sus parametros.
    Retorna un diccionario con el tablero
    '''
    #Creo el diccionario del tablero 
    pass

def generar_lista_tarjetas(tarjetas_horizontal: int, tarjetas_vertical: int, ancho_tarjeta: int, alto_tarjeta: int)->list:
    
    '''
    Función que se encarga de generar una lista de tarjetas.
    Va a generar la cantidad de tarjetas que le especifique anteriormente con las constantes teniendo en cuenta el eje X y el eje Y correspondiente de las superficies de cada una de las tarjetas.
    Retorna la lista de las tarjetas generadas
    '''

    lista_tarjetas = []
    indice = 0
    lista_id = generar_lista_ids_tarjetas(CANTIDAD_TARJETAS_UNICAS) 
    pos_x = 0
    pos_y = 0
    for x in range(CANTIDAD_TARJETAS_H):
        pos_x = ANCHO_TARJETA * x
        for y in range(CANTIDAD_TARJETAS_V):
            pos_y = ALTO_TARJETA * y
            print(f"{pos_x} {pos_y}")
            
            print(indice)
            path = f"./recursos/0{lista_id[indice]}.png"
            img = tarjeta.crear_tarjeta(path, lista_id[indice], "./recursos/00.png", pos_x, pos_y, ANCHO_TARJETA, ALTO_TARJETA)
            indice += 1
            lista_tarjetas.append(img)

    return lista_tarjetas
    #Guardo cada una de las tarjetas (Tener en cuenta la posicion X e Y de las mismas)


def generar_lista_ids_tarjetas(cantidad_de_tajetas_unicas: int):
    '''
    Funcion que se encarga de ordenar de forma aleatoria los id de las tarjetas para que las mismas tengan un orden aleatorio en cada partida.
    '''
    lista_ids = []
    for tarjeta in range (1,cantidad_de_tajetas_unicas+1):
        lista_ids.append(tarjeta)
        lista_ids.append(tarjeta)
    
    random.shuffle(lista_ids)

    return lista_ids


    #Creo la lista con los id de todas las tarjetas que voy a jugar
    #Ordeno aleatoriamente los id de las mismas
    
#print(generar_lista_ids_tarjetas(CANTIDAD_TARJETAS_UNICAS))
   
generar_lista_tarjetas(CANTIDAD_TARJETAS_H, CANTIDAD_TARJETAS_V, ANCHO_TARJETA, ALTO_TARJETA) 
def detectar_colision(tablero,pos_xy):
    '''
    verifica si existe una colision alguna tarjetas del tablero y la coordenada recibida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el identificador de la tarjeta que colisiono con el mouse y sino retorna None
    '''
    #Manejo de colisiones
    pass

def actualizar_tablero(tablero):
    '''
    Verifica si es necesario actualizar el estado de alguna tarjeta, en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero
    '''
    #Actualiza el tablero en tiempo real mientras se juega
    pass

def descubrir_tarjetas(lista_tarjetas, identificador):
    '''
        Función que se encarga de cambiarle la bandera a las tarjetas a las que el usuario haya acertado en el memotest y por ende mostrarlas.
        Recorre las tarjetas de la lista y si tiene el mismo identificador que el pasado por parametro y tambien la misma no ha sido descubierta anteriormente cambia la bandera de la clave descubierto a True
        Recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
    '''
    #Cambio la bandera de desubierto a True si la misma no se descubrio anteriormente.
    pass

def comparar_tarjetas(tablero):
    '''
    Funcion que se encarga de encontrar un match en la selección de las tarjetas del usuario.
    Si el usuario selecciono dos tarjetas está función se encargara de verificar si el identificador 
    de las mismas corresponde si es así retorna True, sino False. 
    En caso de que no hayan dos tarjetas seleccionadas retorna None
    '''
    #Verifico si las tarjetas seleccionadas por el jugador coinciden o no (Llamar a la funcion de arriba descubrir_tarjetas si hay match)
    pass

def dibujar_tablero(tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    #Dibuja el tablero con todas las cartas en la pantalla de mi juego
    pass
     