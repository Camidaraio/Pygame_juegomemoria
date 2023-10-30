import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Tamaño de celda y velocidad de la serpiente
cell_size = 20
snake_speed = 15

# Inicializar serpiente
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'

# Inicializar comida
food_pos = [random.randrange(1, (window_width//cell_size)) * cell_size,
            random.randrange(1, (window_height//cell_size)) * cell_size]

# Puntuación
score = 0

# Función para mostrar la puntuación
def show_score():
    font = pygame.font.Font(None, 36)
    text = font.render(f'Puntuación: {score}', True, white)
    window.blit(text, (10, 10))

# Función para mostrar el mensaje de Game Over
def game_over():
    myFont = pygame.font.SysFont('times new roman', 90)
    game_over_surface = myFont.render('Tu puntaje es: ' + str(score), True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_width/2, window_height/4)
    window.fill(black)
    window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.quit()
    quit()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            if event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            if event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            if event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

    # Mover la serpiente
    if snake_direction == 'UP':
        snake_pos[1] -= cell_size
    if snake_direction == 'DOWN':
        snake_pos[1] += cell_size
    if snake_direction == 'LEFT':
        snake_pos[0] -= cell_size
    if snake_direction == 'RIGHT':
        snake_pos[0] += cell_size

    # Comprobar si la serpiente ha comido la comida
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_pos = [random.randrange(1, (window_width//cell_size)) * cell_size,
                    random.randrange(1, (window_height//cell_size)) * cell_size]

    # Crear el cuerpo de la serpiente
    snake_body.insert(0, list(snake_pos))

    # Dibujar la serpiente y la comida
    window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(window, red, pygame.Rect(pos[0], pos[1], cell_size, cell_size))
    pygame.draw.rect(window, white, pygame.Rect(food_pos[0], food_pos[1], cell_size, cell_size))

    # Game Over si la serpiente toca los bordes
    if snake_pos[0] < 0 or snake_pos[0] > window_width-20 or snake_pos[1] < 0 or snake_pos[1] > window_height-20:
        game_over()

    # Game Over si la serpiente se come a sí misma
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # Mostrar la puntuación
    show_score()

    pygame.display.update()

    # Controlar la velocidad de la serpiente
    pygame.time.Clock().tick(snake_speed)

# Salir del juego
pygame.quit()
quit()
