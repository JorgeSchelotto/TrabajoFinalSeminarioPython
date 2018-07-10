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
    from J1 import JuegoUno
    from J2 import JuegoDos
    from J3 import JuegoTres
    from J4 import JuegoCuatro
    import os
    import random
    from Clases import Premio
    from PantallaPuntos import pantalla_puntos_clases
except ImportError as error:
    print(error, 'Error de importacion en modulo')


__author__ = 'Burgos, Agustin - Schelotto, Jorge'
__copyright__ = 'Copyright 2018, Burgos Schelotto'
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Burgos, Agustin - Schelotto, Jorge'
__email__ = ' agburgos83@gmail.com - jasfotografo@hotmail.com'
__status__ = 'Production'

# Set Up el arte y sonido (assets)
GAME_FOLDER = os.path.dirname(__file__)
FOLDER = os.path.join(GAME_FOLDER, "Imagenes")
IMAGE_FOLDER = os.path.join(FOLDER, "main")
JUEGOUNO_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j1"), "logo_J1.png")
JUEGODOS_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "logo_J2.png")
JUEGOTRES_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j3"), "logo_J3b.png")
JUEGOCUATRO_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j4"), "logo_J4.png")
MUSIC_FOLDER = None
SOUNDS_FOLDER = None

class MainMenu:
    """Menu principal del juego"""
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(IMAGE_FOLDER, "fondo_main.png")).convert_alpha()
        self.image = pygame.transform.scale(self.load, self.screen.get_size())
        self.juego = ''
        self.music = True



    def on_init(self):
        """Inicializo pygame y creo la ventana principal"""
        print("Load!")
        pygame.init()
        pygame.mixer.init()
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Main Menu")
        pygame.mixer.music.load(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'MainMenu.mp3'))
        pygame.mixer.music.play(loops=-1)

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
                        elif icono.name == 'music':
                            self.music = not self.music
                            if self.music:
                                pygame.mixer.music.unpause()
                                icono.image = pygame.transform.scale(pygame.image.load(os.path.join(IMAGE_FOLDER, "sonido_on.png")), (73, 73))
                            else:
                                pygame.mixer.music.pause()
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "sonido_off.png")), (73, 73))
                        elif icono.name == 'credits':
                            self.juego = 'puntos'
                            self.running = False
                        elif icono.name == 'j1':
                            self.juego = 'j1'
                            self.running = False
                        elif icono.name == 'j2':
                            self.juego = 'j2'
                            self.running = False
                        elif icono.name == 'j3':
                            self.juego = 'j3'
                            self.running = False
                        elif icono.name == 'j4':
                            self.juego = 'j4'
                            self.running = False
                        elif icono.name == 'random':
                            ran = ['j1', 'j2', 'j3', 'j4']
                            self.juego = ran[random.randint(0,3)]
                            self.running = False







    def execute(self):
        """Loop del juego"""

        self.on_init()
        iconos = [Icono('j1', JUEGOUNO_FOLDER, 240, 610), Icono('j2', JUEGODOS_FOLDER, 540, 610), Icono('j3', JUEGOTRES_FOLDER, 840, 610),
                  Icono('j4', JUEGOCUATRO_FOLDER, 1140, 610), Icono('quit', os.path.join(IMAGE_FOLDER, "quit_suite.png"), 1250, 85),
                  Icono('j4', JUEGOCUATRO_FOLDER, 1140, 610),
                  Icono('random', os.path.join(IMAGE_FOLDER, "shuffle.png"),190, 300),
                  Icono('music', os.path.join(IMAGE_FOLDER, "sonido_on.png"), 1250, 185),
                  Icono('credits', os.path.join(IMAGE_FOLDER, "creditos.png"), 1250, 290)]


        while self.running:

            """Loop principal del programa"""
            self.clock.tick(self.FPS)
            self.screen.blit(self.image, (0, 0))






            # Update
            self.check_events(iconos)
            # Eventos de los iconos
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
            juego = JuegoUno.JuegoUno()
            juego.execute()
        elif self.juego == 'j2':
            juego = JuegoDos.JuegoDos()
            juego.execute()
        elif self.juego == 'j3':
            juego = JuegoTres.JuegoTres()
            juego.execute()
        elif self.juego == 'j4':
            juego = JuegoCuatro.JuegoCuatro()
            juego.execute()
        elif self.juego== 'puntos':
            juego = pantalla_puntos_clases.pantalla_puntos()
            juego.execute()

if __name__ == "__main__":
    mainMenu = MainMenu()
    mainMenu.execute()


