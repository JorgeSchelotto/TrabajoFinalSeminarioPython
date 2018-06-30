import pygame
from pygame.locals import *
import os


class Icono(pygame.sprite.Sprite):
    """Clase que representa un icono"""
    def __init__(self, name, ruta, x, y):
        super(Icono, self).__init__()
        self.name = name
        self.image = pygame.image.load(ruta)#.convert()
        self.image = pygame.transform.scale(self.image,(int(self.image.get_size()[0] / 2), int(self.image.get_size()[1] / 2)))
        #self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.CENTER = (x,y)
        self.hover = False
        self.click = False



    def update(self, surface):
        """Maneja eventos propios de la clase"""

        if self.hover:
            if self.rect.center == self.CENTER and self.rect.center[0] > self.CENTER[0] - 25 :
                self.rect.center = (self.CENTER[0] - 10, self.CENTER[1])
        else:
            self.rect.center = self.CENTER


        if self.click:
            pass
        surface.blit(self.image, self.rect)


