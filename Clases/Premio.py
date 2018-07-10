__author__ = 'Burgos, Agustin - Schelotto, Jorge'
# -*- coding: utf-8 -*-

import pygame

class Cartel_Premio:
    def __init__(self,nombre, x,y):
        ''''instancia el objeto de la clase cargando la imagen'''
        self.image = pygame.transform.scale(pygame.image.load(nombre), (800, 295)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self, surface):
        surface.blit(self.image, self.rect)





