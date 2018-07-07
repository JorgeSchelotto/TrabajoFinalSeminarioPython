#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementación del juego numero 2. Al cerrarlo volvera al menu principal"""


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
    from Icono import Icono
    from Imagenes import Imagen
    import os
    import random
    import MainMenu
    from Palabras import Palabras
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
IMAGE_FOLDER = os.path.join(FOLDER, "j4")
MUSIC_FOLDER = None
SOUNDS_FOLDER = None
HEIGHT = 200
WEIGHT = 80



class JuegoDos:
    """Menu principal del juego"""
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(IMAGE_FOLDER, "fondo-04.png")).convert()
        self.image = pygame.transform.scale(self.load, self.screen.get_size())



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

    def check_events(self, iconos, player, enemigos):
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
                            pass
                        elif icono.name == 'credits':
                            pass
                        elif icono.name == 'help':
                            pass
                for Player in player:
                    if Player.getRect().collidepoint(event.pos):
                        Player.setClick(True)
            elif event.type == MOUSEBUTTONUP:
                for Player in player:
                    Player.setClick(False)
                    for Enemigo in enemigos:
                        if pygame.sprite.collide_rect(Player, Enemigo):
                            print('Toque un enemigo!', Enemigo.getNombre())
                            if Player.getPalabra().upper() == Enemigo.getNombre():
                                print(Player.getPalabra()[0].upper(), Enemigo.getNombre() )
                                Player.rect.center = Enemigo.rect.center
                                print('Palabra {} toco a Imagen {}. Suma 10!'.format(Player.getPalabra(), Enemigo.getNombre()))
                                Player.collide = True


    def randomEnemigos(self):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de letras"""
        game_folder = os.path.dirname(__file__)
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j4"), "imagenes"), "faciles"), "palabras")
        lista_enemigos = os.listdir(enemies_folder)

        letra = ['A', 'E', 'I', 'O', 'U']


        con=[]
        while len(con) != 4:
            valor = random.randrange(len(lista_enemigos)-1)
            print(valor)
            if valor not in con:
                con.append(valor)


        lista = []
        for num in con:
            lista.append(lista_enemigos[num])


        pal2 = {}
        for palabras in lista:
            pal2[palabras.replace('\n', '').upper()] = os.path.join(enemies_folder, palabras)

        print(pal2)

        return pal2

    def randomPlayers(self, dic_letras):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de imagenes"""
        game_folder = os.path.dirname(__file__)
        folder = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j4"), "Imagenes"), 'faciles'), 'imagenes')
        players_folder = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j4"), "imagenes"), "faciles"), "palabras")
        lista_players = os.listdir(players_folder)



        # Creo una lista de numeros aleatorios.
        con = []
        while len(con) < 4:
            valor = random.randrange(len(lista_players)-1)
            if valor not in con:
                con.append(valor)
        print(con)

        lista = []
        num = 0
        print('Tamaño del archivo: ', len(lista_players))
        print(dic_letras)
        letras =[]
        while len(lista) < 4:
            if lista_players[num].upper() in dic_letras:
                print(lista_players[num].upper())
                # si esta en el diccionario de palabras
                lista.append(lista_players[num])
                letras.append(lista_players[num][0].upper())
            num = num +1

            print('no se cumple condicion')
            print(lista_players[num].upper())
            print(dic_letras)
            print(lista)
            #buscar mas con I y con O
        for palabra in lista_players:
            if lista[random.randrange(2)][0] == palabra[0] and lista[random.randrange(2)] != palabra:
                lista.append(palabra)
                break
        print(lista)

        pal2 = {}
        for palabras in lista:
            pal2[palabras.replace('\n', '')] = os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j1"), "Imagenes"),
                             'facil'), palabras).replace('\n', '')

        print(pal2)

        return pal2



    def execute(self):
        """Loop del juego"""

        self.on_init()
        iconos = [Icono('quit', os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J4.png"), 1300, 50),
                  Icono('music_on', os.path.join(IMAGE_FOLDER, "musica_ON_J4.png"), 1300, 135),
                  Icono('help', os.path.join(IMAGE_FOLDER, "ayuda_J4.png"), 1300, 220)]

        dic_letras = self.randomEnemigos()
        letras_x = 160
        letras_y= 320
        letras = []
        for key, value in dic_letras.items():
            letras.append(Imagen(key, value, letras_x, letras_y, HEIGHT, WEIGHT))
            letras_x = letras_x + 345

        dic_jugadores = self.randomPlayers(dic_letras).copy()
        jugadores = []

        PALABRAS_X = 200
        PALABRAS_Y = 570
        for nombre, ruta in dic_jugadores.items():
            jugadores.append(Palabras(ruta, nombre, PALABRAS_X, PALABRAS_Y))
            PALABRAS_X = PALABRAS_X + 320



        while self.running:


            """Loop principal del programa"""
            self.clock.tick(self.FPS)
            self.screen.blit(self.image, (0, 0))


            # Update
            self.check_events(iconos, jugadores, letras)
            for icono in iconos:
                icono.update(self.screen)
                if icono.rect.collidepoint(pygame.mouse.get_pos()):
                    icono.hover = True
                else:
                    icono.hover = False

            for enemy in letras:
                enemy.update(self.screen)

            for jugador in jugadores:
                jugador.update(self.screen)



            # Draw / Render



            # update la pantalla
            pygame.display.update()

        self.clean_up()
        mainMenu = MainMenu.MainMenu()
        mainMenu.execute()

if __name__ == "__main__":
    game = JuegoDos()
    game.execute()