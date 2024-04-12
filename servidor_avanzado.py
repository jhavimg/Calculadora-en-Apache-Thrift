import glob
import sys

from calc_avanzada import OperacionesAvanzadas

import math

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging
logging.basicConfig (level=logging.DEBUG)

class OperacionesAvanzadasHandler:
    def __init__(self):
        self.log = {}

    def ping (self):
        print ("Me han hecho ping()")

    def seno(self, num):
        print("Calculando seno de " + str(num))
        return math.sin(num)
    
    def aseno(self, num):
        print("Calculando arcoseno de " + str(num))
        return math.degrees(math.asin(num))
    
    def coseno(self, num):
        print("Calculando coseno de " + str(num))
        return math.cos(num)
    
    def acoseno(self, num):
        print("Calculando arcocoseno de " + str(num))
        return math.degrees(math.acos(num))

    def tangente(self, num):
        print("Calculando tangente de " + str(num))
        return math.tan(num)
    
    def atangente(self, num):
        print("Calculando arcotangente de " + str(num))
        return math.degrees(math.atan(num))
    
    def grados_a_radianes(self, n1):
        print("Pasar a radianes " + str(n1))
        return math.radians(n1)
    
    def radianes_a_grados(self, n):
        print ("Pasar a grados " + str(n))
        return math.degrees(n)

    def potencia(self, base, exponente):
        return math.pow(base, exponente)

    def raizCuadrada(self, numero):
        return math.sqrt(numero)
    
if __name__ == '__main__':
    handler = OperacionesAvanzadasHandler()
    processor = OperacionesAvanzadas.Processor (handler)
    transport = TSocket.TServerSocket (host='127.0.0.1', port=9091)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer (processor, transport, tfactory, pfactory)

    print ("Iniciando servidor avanzado...")
    server.serve()
    print ('done')