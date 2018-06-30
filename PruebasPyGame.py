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

"""Probando pygame"""


import pygame
from pygame.locals import *
from Imagenes import Imagen
from Palabras import Palabras

class Game2():

    def __init__(self):
        self._running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.BLUE = 0, 0, 255
        self.WHITE = 255, 255, 255

    def on_init(self):
        """
            Inicialización de pygame
        """
        pygame.init()
        print("Load!")

    def clean_up(self):
        """
            Limpia los módulos de pygame
        """
        pygame.quit()
        print("Quit!")

    def _check_events(self, Player):
        """
            Verifico los eventos dentro del loop
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self._running = False
            elif event.type == MOUSEBUTTONDOWN:
                if Player.getRect().collidepoint(event.pos):
                    print('Lo toque')
                    Player.setClick(True)
                    #Player.update(self.screen)
                    #fuente = pygame.font.Font(None, 72)
                    #titulo = fuente.render('Lo toque', True, pygame.Color("red"))
                    #titulo_rect = titulo.get_rect()
                    #titulo_rect.centerx = self.screen.get_rect().centerx
                    #self.screen.blit(titulo, titulo_rect)
            elif event.type == MOUSEBUTTONUP:
                Player.setClick(False)





    def execute(self):
        self.on_init()

        #loop = 0
        #x = 200
        perro = Palabras('perro')
        perro.getRect().center = (300, 200)
        imagenPerro = Imagen('perro')

        while self._running:
            self.clock.tick(60)

            """if x >= 640:
                x = 0
            else:
                x += 50"""

            self.screen.fill(self.BLUE)
            #pygame.draw.rect(self.screen, self.WHITE, (x, 200, 100, 100))
            #imagen = perro.getPalabraImagen()
            #palabraImagen= imagenPerro.getImagen()
            #self.screen.blit(perro.getPalabraImagen(), (100, 100))
            self.screen.blit(imagenPerro.getImagen(), (150, 400))


            #loop += 1
            #print("Run! " + str(loop))
            self._check_events(perro)
            perro.update(self.screen)
            pygame.display.update()
            pygame.time.Clock()


        self.clean_up()


if __name__ == "__main__":
    game = Game2()
    game.execute()
