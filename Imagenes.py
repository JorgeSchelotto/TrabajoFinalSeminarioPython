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

class Imagen(pygame.sprite.Sprite):
    def __init__(self, nombre, ruta, x, y, H, W):
        super(Imagen, self).__init__()
        self.__nombre = nombre
        self.image = pygame.image.load(ruta)
        self.image = pygame.transform.scale(self.image, (H, W))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.mask = pygame.mask.from_surface(self.image)

    def getNombre(self):
        return self.__nombre

    def getImagen(self):
        return self.image

    def getRect(self):
        return self.rect

    def update(self, surface):
        surface.blit(self.getImagen(), self.getRect())












