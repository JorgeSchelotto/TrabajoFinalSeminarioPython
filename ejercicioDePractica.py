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
import random
from PruebasPyGame import Game2

class Game():

    def __init__(self):
        self.name = 'j1'
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

    def _check_events(self, player, lista):
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
                for Player in player:
                    if Player.getRect().collidepoint(event.pos):
                        #print('Click palabra')
                        Player.setClick(True)
            elif event.type == MOUSEBUTTONUP:
                fin = 3
                for Player in player:
                    Player.setClick(False)
                    #print('Levante el mouse')
                    for Enemigo in lista:
                        if pygame.sprite.collide_rect(Player, Enemigo):
                            print('Toque un enemigo!', Enemigo.getNombre())
                            if Player.getPalabra() == Enemigo.getNombre():
                                Player.rect.center = Enemigo.rect.center
                                print('Palabra {} toco a Imagen {}. Suma 10!'.format(Player.getPalabra(), Enemigo.getNombre()))
                                Player.collide = True
                                """fin = fin - 1
                                print(fin)
                                if fin <= 0:
                                    print(fin)

                                    game = Game()
                                    game.execute()
                                    #self.clean_up()"""

    def execute(self):
        self.on_init()
        palabras = ['perro', 'pato', 'pajaro']

        con = []
        while len(con) < 3:
            valor = random.randrange(3)
            if valor not in con:
                con.append(valor)

        perro = Palabras(palabras[con[0]], 200, 500)
        pato = Palabras(palabras[con[1]], 600, 500)
        pajaro = Palabras(palabras[con[2]], 1000, 500)
        player = [perro, pato, pajaro]



        con = []
        while len(con) < 3:
            valor = random.randrange(3)
            if valor not in con:
                con.append(valor)

        imagenPerro = Imagen(palabras[con[0]])
        imagenPerro.getRect().center = (200, 200)
        imagenPato = Imagen(palabras[con[1]])
        imagenPato.getRect().center = (600, 200)
        imagenPajaro = Imagen(palabras[con[2]])
        imagenPajaro.getRect().center = (1000, 200)
        lista = [imagenPerro, imagenPato, imagenPajaro]



        while self._running:
            self.clock.tick(30)
            self.screen.fill(self.BLUE)



            #Chequea eventos


            self._check_events(player, lista)

            imagenPerro.update(self.screen)
            imagenPajaro.update(self.screen)
            imagenPato.update(self.screen)
            perro.update(self.screen)
            pajaro.update(self.screen)
            pato.update(self.screen)
            pygame.display.update()
            pygame.time.Clock()



        self.clean_up()


if __name__ == "__main__":
    game = Game()
    game.execute()