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
from Imagenes import Imagen
import os
import random
from Palabras import Palabras


# Set Up el arte y sonido (assets)
game_folder = os.path.dirname(__file__)
folder = os.path.join(game_folder, "Imagenes")
img_folder = os.path.join(folder, "j3")
tacho_folder = os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "logo_J3b.png")
imagen_folder = os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "E.png")
H = 180
W = 170



class Main:
    """Menu principal del juego"""
    def __init__(self):
        self.running = True
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.load = pygame.image.load(os.path.join(img_folder, "fondo-03.png")).convert()
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

    def check_events(self, iconos, player, Enemigo):
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
                for Player in player:
                    if Player.getRect().collidepoint(event.pos):
                        Player.setClick(True)
            elif event.type == MOUSEBUTTONUP:
                for Player in player:
                    Player.setClick(False)
                    if pygame.sprite.collide_rect(Player, Enemigo):
                        print('Toque un enemigo!', Enemigo.getNombre())
                        if Player.getPalabra()[0] != Enemigo.getNombre()[0]:
                            print(Player.getPalabra()[0].upper(), Enemigo.getNombre() )
                            Player.rect.center = Enemigo.rect.center
                            print('Palabra {} toco a Imagen {}. Suma 10!'.format(Player.getPalabra(), Enemigo.getNombre()))
                            Player.collide = True


    def randomEnemigos(self):
        """Genera un diccionario aleatorio y sin repeticiones con los nombres y las direcciones de los archivos de letras"""
        game_folder = os.path.dirname(__file__)
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "imagenes"), "faciles")
        lista_enemigos = os.listdir(enemies_folder)

        # Genero un diccionario cuya clave y valor son un elemento de lista_enemigos elegido en forma aleatoria.
        num = random.randrange(len(lista_enemigos)-1)
        print(num)
        pal = [lista_enemigos[num].replace('\n', ''), os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"),"imagenes"), "faciles"), lista_enemigos[num]).replace('\n', '')))]
        print(pal)
        return pal


    def randomPlayers(self, dic_letras):
        """Genera un diccionario aleatorio con los nombres y las direcciones de los archivos de imagenes"""

        # Creo lista con los nombres de las imagenes de la carpeta indicada
        game_folder = os.path.dirname(__file__)
        enemies_folder = os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "imagenes"), "faciles")
        lista_enemigos = os.listdir(enemies_folder)

        # Cargo una lista con palabras que empiesen con la misma letra que la imagen elegida en la funcion randomEnemigos()
        imagenes = []
        for imagen in lista_enemigos:
            if imagen[0] == dic_letras[0][0]:
                imagenes.append(imagen)

        # Carga una imagen aleatoria cuyo nombre no comience con la primera letra de la imagen elegida
        num = random.randrange(len(lista_enemigos) - 1)
        while len(imagenes) < 6:
            if lista_enemigos[num][0] != dic_letras[0][0]:
                imagenes.append(lista_enemigos[num])
            else:
                num = random.randrange(len(lista_enemigos) - 1)
            print('No se cumple la condicion', lista_enemigos[num][0], dic_letras[0][0])


        # Desordeno la lista imagenes
        random.shuffle(imagenes)


        # Creo un diccionario que tiene como llave el nombre de la imagen y como valor su direccion en memoria secundaria
        pal2 = {}
        for palabras in imagenes:
            pal2[palabras.replace('\n', '')] = os.path.join(
                os.path.join(os.path.join(os.path.join(os.path.join(game_folder, "Imagenes"), "j3"), "Imagenes"),
                             'faciles'), palabras).replace('\n', '')

        print(pal2)

        return pal2



    def execute(self):
        """Loop del juego"""

        self.on_init()

        # Cargo iconos
        iconos = [Icono('quit', os.path.join(img_folder, "flecha3.png"), 1250, 100 )]



        # Cargo imagen del tacho
        nombre = self.randomEnemigos()
        print('nombre: ', nombre)
        print(nombre)
        tacho = Imagen(nombre[0],tacho_folder , 160, 570,  169, 200)

        # Cargo imagen a comparar
        print(nombre[1])
        imagen = Imagen(nombre[0], nombre[1], 200,350, H, W)

        # Cargo fichas
        dic_jugadores = self.randomPlayers(nombre).copy()
        jugadores = []

        PALABRAS_X_ABAJO = 520
        PALABRAS_X_ARRIVA = 220
        PALABRAS_Y = 570
        PALABRAS_X = 520
        for nombre, ruta in dic_jugadores.items():
            cant = 0
            if cant > 3:
                PALABRAS_Y = 220
                jugadores.append(Palabras(ruta, nombre.replace('.png', ''), PALABRAS_X, PALABRAS_Y))
                PALABRAS_X = PALABRAS_X + 320
                cant = cant + 1
            elif cant < 3:
                jugadores.append(Palabras(ruta, nombre, PALABRAS_X, PALABRAS_Y))
                PALABRAS_X = PALABRAS_X + 320




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



            # Draw / Render



            # update la pantalla
            pygame.display.update()

        self.clean_up()

if __name__ == "__main__":
    game = Main()
    game.execute()
