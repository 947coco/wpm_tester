import pygame as pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('mpm testeur')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()