#!/usr/bin/env python
__author__      = "Alexandre Costa"
__copyright__   = "Copyright 2014, Projeto AED"
__credits__     = ["Alexandre Costa"]
__license__     = "GPL"
__version__     = "1.0"
__maintainer__  = "Alexandre Costa"
__email__       = "alexandre.costa@inf.ufpel.edu.br"
__status__      = "Desenvolvimento"

class No:
  def __init__(self, info=None, link=None):
    self.info = info
    self.link = link

class Fila:
    def __init__(self):
        self.tamanho = 0
        self.topo = None