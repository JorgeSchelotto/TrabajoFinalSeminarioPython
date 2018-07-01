__author__ = 'Burgos, Agustin - Schelotto, Jorge'
# -*- coding: utf-8 -*-

# Copyright 2018 autors: Burgos Agustin, Schelotto Jorge
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
#  TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

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


