#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementación del juego numero 4. Al cerrarlo volvera al menu principal"""

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

try:
    import pygame
    from pygame.locals import *
    from Clases import Palabras
except ImportError as error:
    print(error, 'Error de importacion en modulo')


__author__ = 'Burgos, Agustin - Schelotto, Jorge'
__copyright__ = 'Copyright 2018, Burgos Schelotto'
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Burgos, Agustin - Schelotto, Jorge'
__email__ = ' agburgos83@gmail.com - jasfotografo@hotmail.com'
__status__ = 'Production'


class Silaba(Palabras.Palabras):
    def __init__(self, ruta, nombre, x, y, HEIGHT, WEIGHT):
        super().__init__(ruta, nombre, x, y)
        self.image = pygame.transform.scale(self.image, (HEIGHT, WEIGHT))
        self.rect = self.image.get_rect()
        self.correct = True



    def update(self, surface):
        """Controla los eventos y coliciones de los sprites Palabras"""
        if not self.getClick() and not self.collide:
            self.rect.center = (super().getPosX(), super().getPosY())

        if self.getClick():
            # Si se hace click en la imagen
            self.rect.center = pygame.mouse.get_pos()

        if self.collide:
            # Si hay colision
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.correct = False
            self.image = pygame.transform.scale(self.image, (0, 0))
            if self.image.get_rect().size[0] == 0:
                self.rect.center = (0,0)

        surface.blit(self.getPalabraImagen(), super().getRect())