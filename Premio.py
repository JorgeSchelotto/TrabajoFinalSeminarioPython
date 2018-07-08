__author__ = 'Burgos, Agustin - Schelotto, Jorge'
# -*- coding: utf-8 -*-

import pygame
#from os import path

clock = pygame.time.Clock()
ancho = 800
alto = 800
tamaño = (ancho, alto)
screen = pygame.display.set_mode(tamaño)
cartel_premio = image.pygame.load('Imagenes/ganaste.png').convert() 

class Cartel_Premio():
	'''instancia el objeto de la clase cargando la imagen'''
	def __init__(self, dx, dy, cartel_premio):
		self.image = pygame.image.load(cartel_premio).convert() 
		self.rect = self.image.get_rect(x = dx, y = dy)
		
	def imprime(self, screen):
		'''imprime la imagen'''
		screen.blit(self.imagen, self.rect)
