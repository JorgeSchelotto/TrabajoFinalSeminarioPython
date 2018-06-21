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


class Jugador:
    def __init__(self, nombre, *args):
        self.nombre = nombre
        self.listPuntajes = args

    def nivelMaximo(self):
        max = -1
        for puntajes in self.listPuntajes:
            if puntajes.nivel < max:
                max = puntajes.nivel
        return max

    def cantidadTotalPuntajes(self):
        return len(self.listPuntajes)

    def puntajeMAximo(self, nivel):
        for puntaje in self.listPuntajes:
            if puntaje.nivel == nivel:
                max = -1
                if max < puntaje.puntos:
                    max = puntaje.puntos
        return max

    def menorTiempo(self, nivel):
        for puntaje in self.listPuntajes:
            if puntaje.nivel == nivel:
                min = 9999
                if min < puntaje.tiempo:
                    min = puntaje.tiempo
        return min