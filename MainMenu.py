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
from Icono import Icono
import JuegoUno
import os

# Set Up el arte y sonido (assets)
game_folder = os.path.dirname(__file__)
folder = os.path.join(game_folder, "Imagenes")
img_folder = os.path.join(folder, "main")
j1_folder = os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j1"), "logo_J1.png")
j2_folder = os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j2"), "logo_J2.png")
j3_folder = os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "logo_J3b.png")
j4_folder = os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j4"), "logo_J4.png")

class MainMenu:
    """Menu principal del juego"""
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(img_folder, "fondo_main.png")).convert()
        self.image = pygame.transform.scale(self.load, self.screen.get_size())
        self.juego = ''



    def on_init(self):
        """Inicializo pygame y creo la ventana principal"""
        print("Load!")
        pygame.init()
        pygame.mixer.init()
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Main Menu")

    def clean_up(self):
        """Limpia los módulos de pygame"""
        pygame.quit()
        print("Quit!")

    def check_events(self, iconos):
        """Verifico los eventos dentro del loop"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                for icono in iconos:
                    if icono.rect.collidepoint(event.pos):
                        if icono.name == 'quit':
                            self.running = False

                        print('Click icono: {}'.format(icono.name))
                        if icono.name == 'j1':
                            self.juego = 'j1'
                            self.running = False





    def execute(self):
        """Loop del juego"""

        self.on_init()
        iconos = [Icono('j1', j1_folder, 240, 610), Icono('j2', j2_folder, 540, 610), Icono('j3',j3_folder, 840, 610),
                  Icono('j4', j4_folder, 1140, 610), Icono('quit', os.path.join(img_folder, "quit_suite.png"), 1250, 100 )]
        escenas = []
        while self.running:
            """Loop principal del programa"""
            self.clock.tick(self.FPS)
            self.screen.blit(self.image, (0, 0))




            # Update
            self.check_events(iconos)
            for icono in iconos:
                icono.update(self.screen)
                if icono.rect.collidepoint(pygame.mouse.get_pos()):
                    icono.hover = True
                else:
                    icono.hover = False



            # Draw / Render



            # flipea la pantalla
            pygame.display.update()

        self.clean_up()

        if self.juego == 'j1':
            j1 = JuegoUno.JuegoUno()
            j1.execute()

if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.execute()


