#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Implementación del juego numero 3. Al cerrarlo volvera al menu principal"""


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
    from J5 import *
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
IMG_FOLDER = os.path.join(FOLDER, "j3")
GARBAGE_FOLDER = os.path.join(os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j3"), "logo_J3b.png")
IMAGE_FOLDER = os.path.join(os.path.join(GAME_FOLDER, "Imagenes"), "j3")
MUSIC_FOLDER = None
SOUNDS_FOLDER = None
HEIGHT = 180
WEIGHT = 170



class JuegoTres:
    """Implementa el juego tres. El objetivo es llevar hacia el tacho la imagen cuyo nombre no comienza con la misma letra
    que las demas imagenes"""
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(IMG_FOLDER, "fondo-03.png")).convert_alpha()
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
        pygame.mixer.music.load(os.path.join(os.path.join(GAME_FOLDER, 'Musica'), 'JuegoTres.mp3'))
        pygame.mixer.music.play(loops=-1)

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
                        self.nivel = 'difíciles'
            print(self.nivel)
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

    def check_events(self, iconos, player, Enemigo):
        """Verifica los eventos dentro del loop"""
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
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_ON_J3.png")), (73, 73))
                            else:
                                pygame.mixer.music.pause()
                                icono.image = pygame.transform.scale(
                                    pygame.image.load(os.path.join(IMAGE_FOLDER, "musica_OFF_J3.png")), (73, 73))
                        elif icono.name == 'credits':
                            pass
                        elif icono.name == 'help':
                            self.help = not self.help
                        if not self.help:
                            icono.image = pygame.transform.scale(
                                pygame.image.load(os.path.join(IMAGE_FOLDER, "cerrar_ayuda_J3.png")), (73, 73))
                        else:
                            icono.image = pygame.transform.scale(
                                pygame.image.load(os.path.join(IMAGE_FOLDER, "ayuda_J3.png")), (73, 73))
                for Player in player:
                    if Player.getRect().collidepoint(event.pos):
                        Player.setClick(True)
            elif event.type == MOUSEBUTTONUP:
                for Player in player:
                    Player.setClick(False)
                    if pygame.sprite.collide_rect(Player, Enemigo):
                        if Player.getPalabra()[0].lower() == Enemigo.getNombre()[0].lower():
                            self.beepLose()
                        if Player.getPalabra()[0].lower() != Enemigo.getNombre()[0].lower():
                            self.beepWin()
                            Player.rect.center = Enemigo.rect.center
                            Player.image = pygame.transform.scale(Player.image, (0, 0))
                            Player.collide = True
                            self.crash = True
                if self.crash:
                    self.hits = self.hits + 1
                    self.crash = False


    def randomEnemigos(self):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de letras"""
        game_folder = os.path.dirname(__file__)
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "imagenes"), self.nivel)
        lista_enemigos = os.listdir(enemies_folder)

        # Genero un diccionario cuya clave y valor son un elemento de lista_enemigos elegido en forma aleatoria.
        num = random.randrange(len(lista_enemigos)-1)
        pal = [lista_enemigos[num].replace('\n', ''), os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"),"imagenes"), self.nivel), lista_enemigos[num]).replace('\n', '')))]
        return pal


    def randomPlayers(self, dic_letras):
        """Genera un diccionario aleatorio con los nombres y las direcciones de los archivos de imagenes"""

        # Creo lista con los nombres de las imagenes de la carpeta indicada
        game_folder = os.path.dirname(__file__)
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "imagenes"), self.nivel)
        lista_enemigos = os.listdir(enemies_folder)

        # Cargo una lista con palabras que empiesen con la misma letra que la imagen elegida en la funcion randomEnemigos()
        imagenes = []
        for imagen in lista_enemigos:
            if len(imagenes) == 5:
                break
            if not(imagen in imagenes) and imagen[0] == dic_letras[0][0]:
                print(not(imagen in imagenes))
                imagenes.append(imagen)




        # Carga una imagen aleatoria cuyo nombre no comience con la primera letra de la imagen elegida
        num = random.randrange(len(lista_enemigos) - 1)
        while len(imagenes) < 6:
            if lista_enemigos[num][0] != dic_letras[0][0]:
                imagenes.append(lista_enemigos[num])
            else:
                num = random.randrange(len(lista_enemigos) - 1)



        # Desordeno la lista imagenes
        random.shuffle(imagenes)


        # Creo un diccionario que tiene como llave el nombre de la imagen y como valor su direccion en memoria secundaria
        pal2 = {}
        for palabras in imagenes:
            pal2[palabras.replace('\n', '')] = os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "Imagenes"),
                             self.nivel), palabras).replace('\n', '')


        return pal2

    def win(self, image):
        """Imprime una patalla de felicitaciones si se gano la partida."""
        bool = False
        if self.hits == 1:
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
        facil = Icono('faciles', os.path.join(IMAGE_FOLDER, "1.png"), 500, 400)
        intermedio = Icono('intermedio', os.path.join(IMAGE_FOLDER, "2.png"), 700, 400)
        dificil = Icono('dificil', os.path.join(IMAGE_FOLDER, "3.png"), 900, 400)

        self.dificultyLevels(facil, intermedio, dificil)

        # Setea pantalla de ganador
        image = Premio.Cartel_Premio('ganaste.png',700, 300)
        cartel = Imagen('cartel', os.path.join(IMAGE_FOLDER, "cartel_ayuda_J3.png"), 1100, 300, 317, 100)

        # Cargo iconos
        iconos = [Icono('quit', os.path.join(IMG_FOLDER, "cerrar_ayuda_J3.png"), 1300, 50),
                  Icono('music', os.path.join(IMG_FOLDER, "musica_ON_J3.png"), 1300, 155),
                  Icono('help', os.path.join(IMG_FOLDER, "ayuda_J3.png"), 1300, 255)]


        # Cargo imagen del tacho
        nombre = self.randomEnemigos()

        tacho = Imagen(nombre[0], GARBAGE_FOLDER, 160, 570, 169, 200)

        # Cargo imagen a comparar
        imagen = Imagen(nombre[0], nombre[1], 200, 350, HEIGHT, WEIGHT)

        # Cargo fichas
        dic_jugadores = self.randomPlayers(nombre).copy()
        jugadores = []

        PALABRAS_Y_ABAJO = 550
        PALABRAS_Y_ARRIVA = 260
        PALABRAS_X = 450
        PALABRAS_X_ARRIVA = 450
        cant = 0
        for nombre, ruta in dic_jugadores.items():
            if cant < 3:
                jugadores.append(Palabras(ruta, nombre.replace('.png', ''), PALABRAS_X, PALABRAS_Y_ABAJO))
                PALABRAS_X = PALABRAS_X + 320
                cant = cant + 1
                print(cant)
            elif cant >= 3:
                jugadores.append(Palabras(ruta, nombre.replace('.png', ''), PALABRAS_X_ARRIVA, PALABRAS_Y_ARRIVA))
                PALABRAS_X_ARRIVA = PALABRAS_X_ARRIVA + 320
                cant = cant + 1

        while self.running:
            """Loop principal del programa"""
            self.clock.tick(self.FPS)
            self.screen.blit(self.image, (0, 0))


            # Verifico eventos
            self.check_events(iconos, jugadores, tacho)

            # Render del tacho y la imagen
            imagen.update(self.screen)
            tacho.update(self.screen)



            # Render de los iconos
            for icono in iconos:
                icono.update(self.screen)
                if icono.rect.collidepoint(pygame.mouse.get_pos()):
                    icono.hover = True
                else:
                    icono.hover = False


            # Render de las fichas
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
        if self.hits >= 1 :
            j5 = JuegoCinco.Game()
            j5.execute()
        else:
            mainMenu = MainMenu.MainMenu()
            mainMenu.execute()

if __name__ == "__main__":
    game = JuegoTres()
    game.execute()
