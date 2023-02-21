import pygame
import time
pygame.init()


screen = pygame.display.set_mode((1000, 650))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake game - by Jess Hansen")

# Tuples containing the colours to be used in the game
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (188, 227, 199)

quit_game = False

# snake will be 20 x 20 pixels
snake_x = 480  # Centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 340  # Centre point vertically is (750-20 snake width)/2 = 340

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

pygame.quit()
quit()
