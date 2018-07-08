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
    from ImagenNula import ImagenNula
    from Palabras import Palabras
    from Silabas import Silaba
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
IMAGE_FOLDER = os.path.join(FOLDER, "j2")
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
        self.load = pygame.image.load(os.path.join(IMAGE_FOLDER, "00_fondo-02.png")).convert()
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
                    if Player.getRect().collidepoint(event.pos) and Player.correct:
                        # Player.correct verfica que la silaba no este ya hubicada en el lugar correcto.
                        # Si la silaba esta en el lugar correcto ya no se permite moverla
                        Player.setClick(True)
            elif event.type == MOUSEBUTTONUP:
                for Player in player:
                    Player.setClick(False)
                    for Enemigo in enemigos:
                        if pygame.sprite.collide_rect(Player, Enemigo):
                            print('Colicion incorrecta entre {} y {}'.format(Player.getPalabra(), Enemigo.getNombre()))
                            if Player.getPalabra().upper() == Enemigo.getNombre().upper():
                                print(Player.getPalabra()[0].upper(), Enemigo.getNombre())
                                # La lina de abajo hace que la ficha se quede en el centro de la caja para silabas
                                Player.rect.center = Enemigo.rect.center
                                print('Palabra {} toco a Imagen {}. Suma 10!'.format(Player.getPalabra(), Enemigo.getNombre()))
                                Player.collide = True


    def ImagenesNulasRandom(self):
        """Genera una lista de dos imagenes que serviran de muestras para armar las dos palabras con las silabas."""
        imagenesNulas_folder = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "imagenes"), "faciles")
        lista_imagenesNulas = os.listdir(imagenesNulas_folder)
        # Mezclo la lista de imagenes
        random.shuffle(lista_imagenesNulas)


        # Creo diccionarios segun la dificultad de juego
        faciles = {'abanico':['a', 'ba', 'ni', 'co'], 'auto': ['au', 'to'], 'banana': ['ba','na','na'], 'elefante': ['e', 'le', 'fan', 'te'],
                   'gato': ['ga', 'to'], 'goma': ['go', 'ma'], 'luna': ['lu', 'na'], 'mesa': ['me', 'sa'], 'moto': ['mo', 'to'],
                   'oro': ['o', 'ro'],'oso': ['o', 'so'], 'oveja': ['o', 've', 'ja'], 'paleta': ['pa', 'le', 'ta'], 'pelota': ['pe', 'lo', 'ta'],
                   'pato': ['pa', 'to'], 'sopa': ['so', 'pa'], 'uvas': ['u', 'vas'], 'vaca': ['va', 'ca'], 'gota': ['go', 'ta']}

        # cargo en forma aleatoria un diccionario con dos palabras y sus correspondiente división en silabas
        dict_img = {}
        num = 0
        for num in range(2):
            img = lista_imagenesNulas[num]
            dict_img[img] = [faciles[img.replace('.png', '')], os.path.join(imagenesNulas_folder, img)]

        print('Imagenes Nulas ', dict_img)

        return dict_img





    def randomEnemigos(self):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de letras"""
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "silabas"), "faciles")
        lista_enemigos = os.listdir(enemies_folder)


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

    def randomPlayers(self, dic_silabas):

        """Genera un diccionario aleatorio y sin repeticiones con las silabas y las direcciones de los archivos de imagenes"""
        players_folder = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "silabas"), "faciles")
        lista_players = os.listdir(players_folder)

        print('Begin randomPlayers()')


        silabas = []
        numeros = random.sample(range(0, len(lista_players)-1), len(lista_players)-1)
        print('numeros', numeros)
        while len(silabas) < 16:
            print('While')
            for key, value in dic_silabas.items():
                # Nivel Palabra
                print('1 For')
                for silaba in value[0]:
                    print('2 For')
                    # Nivel silaba
                    silabas.append(silaba.upper() + '.png')
            for num in numeros:
                print('3 For')
                # Cargo la lista con silabas al azar
                if len(silabas) < 16:
                    if not(lista_players[num] in silabas):
                        silabas.append(lista_players[num])
                else:
                    break
        print('silabas', silabas)
        print('silabas', len(silabas))

        # Desordeno silabas
        random.shuffle(silabas)
        print('silabas caos', silabas)


        # Cargo el diccionario final que retornara el metodo
        pal2 = {}
        for palabras in silabas:
            pal2[palabras.replace('\n', '')] = os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "silabas"),
                             'faciles'), palabras).replace('\n', '')

        print(pal2)
        print('End randomPlayers()')

        return pal2



    def execute(self):
        """Loop del juego"""

        self.on_init()

        # Setea los iconos
        iconos = [Icono('quit', os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J2.png"), 1300, 50),
                  Icono('music_on', os.path.join(IMAGE_FOLDER, "musica_ON_J2.png"), 1300, 135),
                  Icono('help', os.path.join(IMAGE_FOLDER, "ayuda_J2.png"), 1300, 220)]

        # Setea imagenes estaticas que sirven como muestra
        imagenesNulas = self.ImagenesNulasRandom()
        img_x = 350
        img_y = 250
        img = []
        for key, value in imagenesNulas.items():
            img.append(ImagenNula(key, value[1], img_x, img_y, 175, 175))
            img_x = img_x + 700

        # Setea las cajas a llenar con silabas
        nulo_folder = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "imagenes"), "nulo.png")
        dic_letras = self.randomEnemigos()
        letras_x = 160
        letras_y= 400
        letras = []
        for key, value in imagenesNulas.items():
            for silaba in value[0]:
                # Si len(silaba) = 2, medida x, si es 3 medida y y si es 4 medida z (implementar para que este balanceado)
                # esta medida esta bien si len() == 4
                letras.append(Imagen(silaba.replace('.png', ''), nulo_folder, letras_x, letras_y, 100, 50))
                letras_x = letras_x + 150
            letras_x = 800



        # Setea las fichas de los jugadores (Silabas)
        dic_jugadores = self.randomPlayers(imagenesNulas)
        jugadores = []
        PALABRAS_Y = 570
        PALABRAS_X = 250
        PALABRAS_X_ABAJO = 250
        PALABRAS_Y_ABAJO = 670
        count = 1
        print(len(dic_jugadores) ,dic_jugadores)
        for nombre, ruta in dic_jugadores.items():
            if count <= 8:
                jugadores.append(Silaba(ruta, nombre.replace('.png', ''), PALABRAS_X, PALABRAS_Y, 100, 40))
                PALABRAS_X = PALABRAS_X + 120
                count = count + 1
            elif count > 8:
                PALABRAS_Y = 670
                jugadores.append(Silaba(ruta, nombre.replace('.png', ''), PALABRAS_X_ABAJO, PALABRAS_Y_ABAJO, 100, 40))
                PALABRAS_X_ABAJO = PALABRAS_X_ABAJO + 120
                count = count + 1
            elif count > 16:
                break

            # if count < 8:
            #     jugadores.append(Silaba(ruta, nombre.replace('.png', ''), PALABRAS_X, PALABRAS_Y, 100, 40))
            #     PALABRAS_X = PALABRAS_X + 100
            #     count = count + 1
            # elif count > 8:
            #     PALABRAS_Y = 670
            #     jugadores.append(Silaba(ruta, nombre.replace('.png', ''), PALABRAS_X, PALABRAS_Y, 100, 40))
            #     PALABRAS_X = PALABRAS_X + 150
            #     count = count + 1



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

            for imagen in img:
                imagen.update(self.screen)

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