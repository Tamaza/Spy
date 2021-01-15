import pygame
from settings import *

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
       # self.image = pygame.transform.scale(image, (10,10))
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):

        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255, 255, 255), self.rect, 10)


    def collide(self):
        # get mouse position
        action = False
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
        # draw button



