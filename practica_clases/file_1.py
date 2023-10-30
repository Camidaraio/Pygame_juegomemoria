import sys #Hace que se mueva
import pygame as pg

pg.init()

rHeight = 700
rWidth = 550

color_del_fondo = (0, 0, 0)
baseC = (73, 0, 230)

x_pos = 332.5
y_pos = 500

screen = pg.display.set_mode((rHeight, rWidth))

end = False

while not end:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x_pos = max(x_pos - 30, 0)  # Limita el movimiento a la izquierda
            elif event.key == pg.K_RIGHT:
                x_pos = min(x_pos + 30, rHeight - 35)  # Limita el movimiento a la derecha
            elif event.key == pg.K_DOWN:
                y_pos = min(y_pos + 30, rWidth - 35)  # Limita el movimiento hacia abajo
            elif event.key == pg.K_UP:
                y_pos = max(y_pos - 30, 0)  # Limita el movimiento hacia arriba

    screen.fill(color_del_fondo)
    pg.draw.rect(screen, baseC, (x_pos, y_pos, 35, 35))
    pg.display.update()