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
    from Clases.Icono import Icono
    from Clases.Imagenes import Imagen
    import os
    import random
    import MainMenu
    from Clases.Palabras import Palabras
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
IMAGE_FOLDER = os.path.join(FOLDER, "j4")
MUSIC_FOLDER = None
SOUNDS_FOLDER = None
HEIGHT = 200
WEIGHT = 80



class JuegoCuatro:
    """Implementa el juego cuatro. El objetivo es llevar hacia cada palabra la imagen que representa a esa palabra"""
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(IMAGE_FOLDER, "fondo-04.png")).convert_alpha()
        self.image = pygame.transform.scale(self.load, self.screen.get_size())
        self.hits = 0
        self.crash = False
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


    def on_init(self):
        """Inicializo pygame y creo la ventana principal"""
        print("Load!")
        pygame.init()
        pygame.mixer.init()
        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Main Menu")
        pygame.display.set_caption("Main Menu")
        pygame.mixer.music.load(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'JuegoCuatro.mp3'))
        pygame.mixer.music.play(loops=-1)

    def dificultyLevels(self, facil, intermedio, dificil):
        """Loop que realiza la seleccion de nivel de dificultad.
        El for del final funciona como una pausa para que el juego cargue las fichas."""
        # Loop de la seleccion de nivel
        while self.nivel == None:
            # Nosale si no elige nivel
            pygame.draw.rect(self.screen, (50, 100, 255), (300, 50, 800, 600), 0)
            pygame.draw.rect(self.screen, (50, 200, 200), (350, 200, 700, 400), 0)
            self.text('Elegi el nivel de dificultad', 650, 100)
            pygame.draw.rect(self.screen, (50, 200, 200), (350, 200, 700, 400), 0)
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
                        self.nivel = 'difíciles'
            for m in range(300):
                pass

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
                            self.music = not self.music
                            if self.music:
                                pygame.mixer.music.unpause()
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_ON_J4.png")), (73, 73))
                            else:
                                pygame.mixer.music.pause()
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_OFF_J4.png")), (73, 73))
                        elif icono.name == 'help':
                            self.help = not self.help
                            if not self.help:
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J4.png")), (73, 73))
                            else:
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "ayuda_J4.png")), (73, 73))
                for Player in player:
                    if Player.getRect().collidepoint(event.pos):
                        Player.setClick(True)
            elif event.type == MOUSEBUTTONUP:
                for Player in player:
                    Player.setClick(False)
                    for Enemigo in enemigos:
                        if pygame.sprite.collide_rect(Player, Enemigo):
                            if Player.getPalabra().lower() != Enemigo.getNombre().lower():
                                self.beepLose()
                            if Player.getPalabra().lower() == Enemigo.getNombre().lower():
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
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j4"), "imagenes"), self.nivel), "palabras")
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


        return pal2

    def randomPlayers(self, dic_letras):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de imagenes"""
        game_folder = os.path.dirname(__file__)
        players_folder = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j4"), "imagenes"), self.nivel), "palabras")
        lista_players = os.listdir(players_folder)



        # Creo una lista de numeros aleatorios.
        con = []
        while len(con) < 3:
            valor = random.randrange(len(lista_players)-1)
            if valor not in con:
                con.append(valor)

        lista = []
        num = 0
        letras =[]
        while len(lista) < 4:
            if lista_players[num].upper() in dic_letras:
                # si esta en el diccionario de palabras
                lista.append(lista_players[num])
                letras.append(lista_players[num][0])
            num = num +1


            #buscar mas con I y con O
        for palabra in lista_players:
            if lista[random.randrange(2)][0] == palabra[0] and lista[random.randrange(2)] != palabra:
                lista.append(palabra)
                break

        pal2 = {}
        for palabras in lista:
            pal2[palabras.replace('\n', '')] = os.path.join(os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j4"), "imagenes"),
                             self.nivel),"imagenes"), palabras).replace('\n', '')
        return pal2



    def win(self, image):
        """Imprime una patalla de felicitaciones si se gano la partida."""
        bool = False
        if self.hits == 4:
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

        self.dificultyLevels(facil, intermedio, dificil)

        # Setea pantalla de ganador
        image = Premio.Cartel_Premio('ganaste.png', 700, 300)
        cartel = Imagen('cartel', os.path.join(IMAGE_FOLDER, "cartel_ayuda_J4.png"), 1100, 300, 317, 100)

        # Setea iconos
        iconos = [Icono('quit', os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J4.png"), 1300, 50),
                  Icono('music', os.path.join(IMAGE_FOLDER, "musica_ON_J4.png"), 1300, 135),
                  Icono('help', os.path.join(IMAGE_FOLDER, "ayuda_J4.png"), 1300, 220)]


        # Setea enemigos
        dic_letras = self.randomEnemigos()
        letras_x = 160
        letras_y= 320
        letras = []
        for key, value in dic_letras.items():
            letras.append(Imagen(key, value, letras_x, letras_y, HEIGHT, WEIGHT))
            letras_x = letras_x + 345

        # Setea las fichas del jugador
        dic_jugadores = self.randomPlayers(dic_letras)
        jugadores = []
        PALABRAS_X = 200
        PALABRAS_Y = 570
        for nombre, ruta in dic_jugadores.items():
            jugadores.append(Palabras(ruta, nombre, PALABRAS_X, PALABRAS_Y))
            PALABRAS_X = PALABRAS_X + 320
            if len(jugadores) == 4:
                break



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

            if not self.help:
                cartel.update(self.screen)

            # Draw / Render
            if self.win(image):
                break



            # update la pantalla
            pygame.display.update()

        # self.clean_up()

        if self.hits == 4:
            j5 = Game()
            j5.execute()
        else:
            mainMenu = MainMenu.MainMenu()
            mainMenu.execute()

if __name__ == "__main__":
    game = JuegoCuatro()
    game.execute()
