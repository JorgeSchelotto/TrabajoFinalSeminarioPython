#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementación del menu principal. Clase base para acceder a los juegos de la suit.
Al cerrarla, se cerrara el programa"""

# Copyright 2018 autors: Burgos Agustin, Schelotto Jorge
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
#  TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

try:

    import pygame
    from pygame.locals import *
    from Clases.Icono import Icono
    import MainMenu
    import os
    import random
    from Clases import Premio
    import os.path as path
    import sys
    from J5 import *

except ImportError as error:
    print(error, 'Error de importacion en modulo')


__author__ = 'Burgos, Agustin - Schelotto, Jorge'
__copyright__ = 'Copyright 2018, Burgos Schelotto'
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Burgos, Agustin - Schelotto, Jorge'
__email__ = ' agburgos83@gmail.com - jasfotografo@hotmail.com'
__status__ = 'Production'




BLANCO = (255, 255, 255)
NARANJA = (253,106,2)
TAMAÑO = (650, 380)
FPS = 30
GAME_FOLDER = os.path.dirname(__file__)
print(GAME_FOLDER)
FOLDER = os.path.join(GAME_FOLDER, "J5")
FOLDER2 = os.path.join(GAME_FOLDER, "Imagenes")
IMAGE_FOLDER = os.path.join(FOLDER2, "main")
IMAGE_FOLDER = os.path.join(FOLDER2, "main")
# Sube dos niveles
ARCHIVO = path.abspath(path.join(__file__, "../.."))


class pantalla_puntos():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.running = True
        self.screen = pygame.display.set_mode((0,0), FULLSCREEN)
        self.image = pygame.Surface((0, 0), FULLSCREEN)
        self.lista_final = []



    def on_init(self):
        """Inicializo pygame y creo la ventana principal"""
        print("Load!")
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Main Menu")
        pygame.mixer.music.load(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'Creditos.mp3'))
        pygame.mixer.music.play(loops=-1)

    def clean_up(self):
        """Limpia los módulos de pygame"""
        pygame.quit()
        print("Quit!")

    def check_events(self, icono):
        """Verifico los eventos dentro del loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                if icono.rect.collidepoint(event.pos):
                    if icono.name == 'quit':
                        self.running = False


    def imprime_texto(self, NARANJA, TAMAÑO):

        font = pygame.font.SysFont("Comic Sans.otf", 30)
        text = font.render('LOS MEJORES 10 PUNTAJES SON', True, NARANJA)
        text_rect = text.get_rect()
        text_rect.centerx = 650
        text_rect.centery = 100
        self.screen.blit(text, text_rect)

        for n, linea in enumerate(self.lista_final[0:10]):
            text = font.render(linea, True, NARANJA)
            text_rect = text.get_rect()
            text_rect.centerx = TAMAÑO[0]
            text_rect.centery = n * 50 + 150
            self.screen.blit(text, text_rect)




    def execute(self):

        self.on_init()
        icono = Icono('quit', os.path.join(IMAGE_FOLDER, "quit_suite.png"), 1250, 85)
        lista_puntajes = []
        ruta = os.path.join(os.path.join(ARCHIVO, 'J5'), 'Puntajes.txt')
        try:
            f = open(os.path.join(FOLDER, ruta), 'r')
            for lineas in f:
                linea = lineas.replace('\n', '').split()
                lista_puntajes.append(linea)
            lista_puntajes2 = sorted(lista_puntajes, key= lambda x: int(x[9]), reverse=True)
            for elem in lista_puntajes2:
                elem2 = ' '.join(elem)
                self.lista_final.append(elem2)
            f.close()

        except IOError as e:
            print(e)


        while self.running:
            print(ARCHIVO)
            """Loop principal del programa"""
            self.clock.tick(self.FPS)
            self.screen.blit(self.image, (0, 0))
            self.check_events(icono)




            # Draw / Render
            icono.update(self.screen)
            self.imprime_texto(NARANJA, TAMAÑO)



            # flipea la pantalla
            pygame.display.update()

        self.clean_up()


        menu = MainMenu.MainMenu()
        menu.execute()




if __name__ == '__main__':
    pantalla = pantalla_puntos()
    pantalla.execute()
