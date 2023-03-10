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

clock = pygame.time.Clock()  # sets the speed at which the snake moves

quit_game = False

# snake will be 20 x 20 pixels
snake_x = 480  # Centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 340  # Centre point vertically is (750-20 snake width)/2 = 340

snake_x_change = 0  # holds the value of changes in the x-coordinate
snake_y_change = 0  # holds the value of changes in the y-coordinate

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_x_change = 0
                snake_y_change = -20
            elif event.key == pygame.K_DOWN:
                snake_x_change = 0
                snake_y_change = 20

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green)  # Changes screen (surface) from default black to green

    # Create rectangle for snake
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(5)  # Sets the speed at which each iteration of the game loop
    # runs in frames per second (5fps). In this case it is set to 5fps

pygame.quit()
quit()
