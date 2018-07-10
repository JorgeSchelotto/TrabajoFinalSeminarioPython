#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementación del juego numero 1. Al cerrarlo volvera al menu principal"""

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
    from Clases.Icono import Icono
    from Clases.Imagenes import Imagen
    import os
    import random
    from Clases.Palabras import Palabras
    import MainMenu
    from Clases import Premio
    from J5.JuegoCinco import Game
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
IMAGE_FOLDER = os.path.join(FOLDER, "j1")
A_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j1"), "A.png")
E_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j1"), "E.png")
I_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j1"), "I.png")
O_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j1"), "O.png")
U_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j1"), "U.png")
ERROR_FOLDER = U_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j1"), "error.png")
HEIGHT = 180
WEIGHT = 170



class JuegoUno:
    """Menu principal del juego"""
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(IMAGE_FOLDER, "00_fondo-01.png")).convert_alpha()
        self.image = pygame.transform.scale(self.load, self.screen.get_size())
        self.hits = 0
        self.crash = False
        self.finish = False
        self.music = True
        self.help = True



    def on_init(self):
        """Inicializo pygame y creo la ventana principal"""
        print("Load!")
        pygame.init()
        pygame.mixer.init()
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Main Menu")
        pygame.mixer.music.load(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'JuegoDos.mp3'))
        pygame.mixer.music.play(loops=-1)

    def clean_up(self):
        """Limpia los módulos de pygame"""
        pygame.quit()
        print("Quit!")

    def winMusic(self):
        """Reproduce sonido de ganador"""
        beep = pygame.mixer.Sound(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'Win.wav'))
        beep.play()

    def beepWin(self):
        """Reproduce de que acerto una combinacion correctamente"""
        beep = pygame.mixer.Sound(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'Pop.wav'))
        beep.play()

    def beepLose(self):
        """Reproduce sonido si no acerto correctamente."""
        beep = pygame.mixer.Sound(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'Mal.wav'))
        beep.play()

    def check_events(self, iconos, player, enemigos, image):
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
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_ON_J1.png")), (73, 73))
                            else:
                                pygame.mixer.music.pause()
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_OFF_J1.png")), (73, 73))
                        elif icono.name == 'help':
                            self.help = not self.help
                            if not self.help:
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J1.png")), (73, 73))
                            else:
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "ayuda_J1.png")), (73, 73))
                for Player in player:
                    if Player.getRect().collidepoint(event.pos):
                        #print('Click palabra')
                        Player.setClick(True)
            elif event.type == MOUSEBUTTONUP:
                for Player in player:
                    Player.setClick(False)
                    for Enemigo in enemigos:
                        if pygame.sprite.collide_rect(Player, Enemigo):
                            if Player.getPalabra()[0].upper() != Enemigo.getNombre():
                                self.beepLose()
                                self.nop(image)
                            if Player.getPalabra()[0].upper() == Enemigo.getNombre():
                                self.beepWin()
                                Player.rect.center = Enemigo.rect.center
                                Player.collide = True
                                self.crash = True
                                if self.crash:
                                    self.hits = self.hits + 1
                                    self.crash = False

    def randomEnemigos(self):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de letras"""
        game_folder = os.path.dirname(__file__)

        letra = ['A', 'E', 'I', 'O', 'U']

        con=[]
        while len(con) != 3:
            valor = random.randrange(5)
            if valor not in con:
                con.append(valor)


        lista = []
        for num in con:
            lista.append(letra[num])


        pal2 = {}
        for letras in lista:
            pal2[letras.replace('\n', '')] = os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j1"), letras + '.png').replace('\n', '')))


        return pal2

    def randomPlayers(self, dic_letras):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de imagenes"""
        game_folder = os.path.dirname(__file__)
        folder = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j1"), "Imagenes"), 'facil'), 'facil.txt')

        file = open(folder, 'r')
        #Creo lista con las palabras del archivo
        pal = []
        for palabras in file:
            pal.append(palabras.replace('\n', ''))

        file.close()

        # Creo una lista de numeros aleatorios.
        con = []
        while len(con) < 4:
            valor = random.randrange(6)
            if valor not in con:
                con.append(valor)

        lista = []
        num = random.randrange(len(pal))
        letras =[]
        repetida = ''
        while len(lista) < 3:
            if pal[num][0].upper() in dic_letras:
                if pal[num] not in lista:
                    if pal[num][0].upper() not in letras:
                        lista.append(pal[num])
                        letras.append(pal[num][0].upper())
                    repetida = pal[num]
            num = random.randrange(len(pal))
            #buscar mas con I y con O
        for palabra in pal:
            if lista[random.randrange(2)][0] == palabra[0] and lista[random.randrange(2)] != palabra:
                lista.append(palabra)
                break

        pal2 = {}
        for palabras in lista:
            pal2[palabras.replace('\n', '')] = os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j1"), "Imagenes"),
                             'facil'), palabras + '.png').replace('\n', '')


        return pal2

    def win(self, image):
        """Imprime una patalla de felicitaciones si se gano la partida."""
        bool = False
        if self.hits >= 3:
            bool = True
            self.winMusic()
            pygame.mixer.music.pause()
            for clock in range(900):
                image.update(self.screen)
                pygame.display.update()
        return bool

    def nop(self, image):
        """Imprime una patalla de error si se gano la partida."""
        for clock in range(700):
            image.update(self.screen)
            pygame.display.update()

    def execute(self):
        """Loop del juego"""

        self.on_init()
        iconos = [Icono('quit', os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J1.png"), 1300, 50),
                  Icono('music', os.path.join(IMAGE_FOLDER, "musica_ON_J1.png"), 1300, 155),
                  Icono('help', os.path.join(IMAGE_FOLDER, "ayuda_j1.png"), 1300, 255)]

        dic_letras = self.randomEnemigos()
        letras_x = 200
        letras_y= 320
        letras = []

        for key, value in dic_letras.items():
            letras.append(Imagen(key, value, letras_x, letras_y, HEIGHT, WEIGHT))
            letras_x = letras_x + 475

        dic_jugadores = self.randomPlayers(dic_letras).copy()
        jugadores = []

        PALABRAS_X = 200
        PALABRAS_Y = 570
        for nombre, ruta in dic_jugadores.items():
            jugadores.append(Palabras(ruta, nombre, PALABRAS_X, PALABRAS_Y))
            PALABRAS_X = PALABRAS_X + 320



        # Seteo imagen que se mostrará al ganar
        image = Premio.Cartel_Premio('ganaste.png', 700, 300)
        cartel =Imagen('cartel', os.path.join(IMAGE_FOLDER, "cartel_ayuda_J1.png"), 1100, 300, 317, 100)
        nop = Premio.Cartel_Premio(ERROR_FOLDER, 700, 300)



        while self.running:
            """Loop principal del programa"""
            self.clock.tick(self.FPS)
            self.screen.blit(self.image, (0, 0))




            # Update
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

            if not self.help:
                cartel.update(self.screen)

            if self.hits == 3:
                self.finish = True


            # Draw / Render

            if self.win(image):
                break

            self.check_events(iconos, jugadores, letras, nop)


            # update la pantalla
            pygame.display.update()




        self.clean_up()
        print(self.hits)

        if self.hits >= 3 :
            j5 = Game()
            j5.execute()
        else:
            mainMenu = MainMenu.MainMenu()
            mainMenu.execute()

if __name__ == "__main__":
    game = JuegoUno()
    game.execute()
