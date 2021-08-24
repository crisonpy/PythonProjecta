import pygame
import math

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PI = math.pi

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sanjeevi's Cool Game")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        screen.fill(WHITE)
        font_size = 60
        y_text = 450
        while font_size > 10 and y_text > 50:
            y_text -= 60 - (60 - font_size)
            font_size -= 10
            font = pygame.font.SysFont('Calibri', font_size, True, False)
            text = font.render("BOB my name is", True, BLACK)
            screen.blit(text, [20, y_text])


#        y_offset = 0
#        while y_offset < 300:
#            pygame.draw.line(screen, GREEN, [100, 50 + y_offset], [500, 50 + y_offset], 5)
#            y_offset += 35
        pygame.display.flip()
        clock.tick(60)


pygame.quit()

