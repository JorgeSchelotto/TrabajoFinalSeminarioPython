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
    from Clases.Icono import Icono
    from Clases.Imagenes import Imagen
    import os
    import random
    import MainMenu
    from Clases.ImagenNula import ImagenNula
    from Clases.Palabras import Palabras
    from Clases.Silabas import Silaba
    from J5.JuegoCinco import Game
    from Clases import Premio
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
    """Implementa el juego dos. El objetivo es llevar hacia cada imagen las silabas que componen su nombre"""

    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(IMAGE_FOLDER, "00_fondo-02.png")).convert_alpha()
        self.image = pygame.transform.scale(self.load, self.screen.get_size())
        self.goal = 0
        self.hits = 0
        self.crash = False
        self.phantom = []
        self.masc = False
        self.music = True
        self.help = True
        self.nivel = None


    def text(self, txt, x, y):
        font = pygame.font.SysFont("Impact.otf", 40)
        text = font.render(txt, True, (255,255,0))
        text_rect = text.get_rect()
        text_rect.centerx = x
        text_rect.centery = y
        self.screen.blit(text, text_rect)

    def dificultyLevels(self, facil, intermedio, dificil):
        """Loop que realiza la seleccion de nivel de dificultad.
        El for del final funciona como una pausa para que el juego cargue las fichas."""
        # Loop de la seleccion de nivel
        while self.nivel == None:
            # Nosale si no elige nivel

            pygame.draw.rect(self.screen, (50, 100, 255), (300, 50, 800, 600), 0)
            pygame.draw.rect(self.screen, (50, 200, 200), (350, 200, 700, 400), 0)
            self.text('Elegi el nivel de dificultad', 700, 100)
            facil.update(self.screen)
            intermedio.update(self.screen)
            dificil.update(self.screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if facil.rect.collidepoint(event.pos):
                        self.nivel = 'faciles'
                    if intermedio.rect.collidepoint(event.pos):
                        self.nivel = 'intermedias'
                    if dificil.rect.collidepoint(event.pos):
                        self.nivel = 'dificiles'
            for m in range(300):
                pass


    def on_init(self):
        """Inicializo pygame y creo la ventana principal"""
        print("Load!")
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Main Menu")
        pygame.display.set_caption("juego Dos")
        pygame.mixer.music.load(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'JuegoDos.mp3'))
        pygame.mixer.music.play(loops=-1)

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

    def clean_up(self):
        """Limpia los módulos de pygame"""
        pygame.quit()
        print("Quit!")

    def check_events(self, iconos, player, enemigos, mascara, phantons):
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
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_ON_J2.png")), (73, 73))
                            else:
                                pygame.mixer.music.pause()
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_OFF_J2.png")), (73, 73))
                        elif icono.name == 'help':
                            self.help = not self.help
                        if not self.help:
                            icono.image = pygame.transform.scale(
                                pygame.image.load(os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J2.png")), (73, 73))
                        else:
                            icono.image = pygame.transform.scale(
                                pygame.image.load(os.path.join(IMAGE_FOLDER, "ayuda_J2.png")), (73, 73))
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
                            if Player.getPalabra().upper() != Enemigo.getNombre().upper():
                                self.beepLose()
                            if Player.getPalabra().upper() == Enemigo.getNombre().upper():
                                Player.collide = True
                                self.beepWin()
                                if Enemigo.getNombre() not in self.phantom:
                                    self.phantom.append(Enemigo.getNombre())
                                    # Si hubo colicion, reemplaza la imagen nula por la silaba corrspondiente.
                                    for Enemigo in enemigos:
                                        if Enemigo.getNombre().lower() in self.phantom:
                                            mascara.append(
                                                ImagenNula(Enemigo.getNombre(),
                                                           os.path.join(phantons, Enemigo.getNombre().upper() + '.png'),
                                                           Enemigo.rect.center[0], Enemigo.rect.center[1], 100, 50))
                                self.crash = True
                                self.masc = True
                                if self.crash:
                                    self.hits = self.hits + 1
                                    self.crash = False


    def ImagenesNulasRandom(self):
        """Genera una lista de dos imagenes que serviran de muestras para armar las dos palabras con las silabas."""

        imagenesNulas_folder = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "imagenes"), "faciles")
        lista_imagenesNulas = os.listdir(imagenesNulas_folder)

        # Mezclo la lista de imagenes
        random.shuffle(lista_imagenesNulas)

        # Creo diccionarios segun la dificultad de juego
        faciles = {'abanico': ['a', 'ba', 'ni', 'co'], 'elefante': ['e', 'le', 'fan', 'te'],
                   'gato': ['ga', 'to'], 'goma': ['go', 'ma'], 'luna': ['lu', 'na'], 'mesa': ['me', 'sa'],
                   'oro': ['o', 'ro'], 'oveja': ['o', 've', 'ja'], 'pelota': ['pe', 'lo', 'ta'],
                   'uvas': ['u', 'vas'], 'vaca': ['va', 'ca'], 'perro': ['pe', 'rro'], 'percha': ['per', 'cha'],
                   'sombrero': ['som', 'bre', 'ro'], 'diario': ['dia', 'rio']}





        # cargo en forma aleatoria un diccionario con dos palabras y sus correspondiente división en silabas
        dict_img = {}
        nivel = []
        for num in range(2):
            if self.nivel != None:
                # si se eligio nivel
                nivel = faciles.copy()
            img = lista_imagenesNulas[num]
            dict_img[img] = [nivel[img.replace('.png', '')], os.path.join(imagenesNulas_folder, img)]

        return dict_img

    def randomEnemigos(self):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de letras"""
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "silabas"), "faciles")
        lista_enemigos = os.listdir(enemies_folder)


        con=[]
        while len(con) != 4:
            valor = random.randrange(len(lista_enemigos)-1)
            if valor not in con:
                con.append(valor)

        lista = []
        for num in con:
            lista.append(lista_enemigos[num])

        pal2 = {}
        for palabras in lista:
            pal2[palabras.replace('\n', '').upper()] = os.path.join(enemies_folder, palabras)

        return pal2

    def randomPlayers(self, dic_silabas):

        """Genera un diccionario aleatorio y sin repeticiones con las silabas y las direcciones de los archivos de imagenes"""
        players_folder = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "silabas"), "faciles")
        lista_players = os.listdir(players_folder)

        silabas = []
        numeros = random.sample(range(0, len(lista_players)-1), len(lista_players)-1)
        while len(silabas) < 16:
            print('While')
            for key, value in dic_silabas.items():
                # Nivel Palabra
                for silaba in value[0]:
                    # Nivel silaba
                    silabas.append(silaba.upper() + '.png')
            for num in numeros:

                # Cargo la lista con silabas al azar
                if len(silabas) < 16:
                    if not(lista_players[num] in silabas):
                        silabas.append(lista_players[num])
                else:
                    break

        # Desordeno silabas
        random.shuffle(silabas)

        # Cargo el diccionario final que retornara el metodo
        pal2 = {}
        for palabras in silabas:
            pal2[palabras.replace('\n', '')] = os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "silabas"),
                             'faciles'), palabras).replace('\n', '')
        return pal2

    def win(self, image):
        """Imprime una patalla de felicitaciones si se gano la partida."""
        bool = False
        if self.goal != 0 and self.hits == self.goal:
            bool = True
            self.winMusic()
            pygame.mixer.music.pause()
            for clock in range(390):
                image.update(self.screen)
                pygame.display.update()
        return bool

    def execute(self):
        """Loop del juego"""

        self.on_init()

        # Seteo niveles
        facil = Icono('facil', os.path.join(IMAGE_FOLDER, "1.png"), 500, 400)
        intermedio = Icono('intermedio', os.path.join(IMAGE_FOLDER, "2.png"), 700, 400)
        dificil = Icono('dificil', os.path.join(IMAGE_FOLDER, "3.png"), 900, 400)


        # Pantalla de seleccion de nivel
        self.dificultyLevels(facil, intermedio, dificil)

        # Seteo imagen que se mostrará al ganar
        image = Premio.Cartel_Premio('ganaste.png',700, 300)
        cartel = Imagen('cartel', os.path.join(IMAGE_FOLDER, "cartel_ayuda_J2.png"), 1100, 300, 317, 100)

        # Setea los iconos
        iconos = [Icono('quit', os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J2.png"), 1300, 50),
                  Icono('music', os.path.join(IMAGE_FOLDER, "musica_ON_J2.png"), 1300, 135),
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
        letras_x = 160
        letras_y= 400
        letras = []
        for key, value in imagenesNulas.items():
            for silaba in value[0]:
                # Si len(silaba) = 2, medida x, si es 3 medida y y si es 4 medida z (implementar para que este balanceado)
                # esta medida esta bien si len() == 4
                letras.append(Imagen(silaba.replace('.png', ''), nulo_folder, letras_x, letras_y, 100, 50))
                letras_x = letras_x + 150
                # Establesco la meta segun la cantidad de silbas cargadas
            self.goal = self.goal + len(value[0])
            letras_x = 800



        # Setea las fichas de los jugadores (Silabas)
        dic_jugadores = self.randomPlayers(imagenesNulas)
        jugadores = []
        PALABRAS_Y = 570
        PALABRAS_X = 250
        PALABRAS_X_ABAJO = 250
        PALABRAS_Y_ABAJO = 670
        count = 1
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

        mascara = []

        phantons = os.path.join(os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j2"), "silabas"), "faciles")

        while self.running:

            """Loop principal del programa"""
            self.clock.tick(self.FPS)
            self.screen.blit(self.image, (0, 0))

            # Update
            self.check_events(iconos, jugadores, letras, mascara, phantons)

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

            for masc in mascara:
                masc.update(self.screen)

            for jugador in jugadores:
                jugador.update(self.screen)


            if not self.help:
                cartel.update(self.screen)

            # Draw / Render
            if self.win(image):
                break

            # update la pantalla
            pygame.display.update()

        self.clean_up()
        if self.goal != 0 and self.hits == self.goal :
            j5 = Game()
            j5.execute()
        else:
            mainMenu = MainMenu.MainMenu()
            mainMenu.execute()

if __name__ == "__main__":
    game = JuegoDos()
    game.execute()