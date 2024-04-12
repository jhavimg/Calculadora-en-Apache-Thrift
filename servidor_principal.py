import glob
import sys

from calculadora import Calculadora
from calc_avanzada import OperacionesAvanzadas
from calc_vectores import CalculadoraVectores
from calc_matrices import CalculadoraMatrices

from thrift import Thrift

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging
logging.basicConfig (level=logging.DEBUG)

class CalculadoraHandler:
    def __init__(self):
        self.log = {}

    def ping (self):
        print ('Me han hecho ping()')

    def suma (self, n1, n2):
        print (str(n1) + ' + ' + str(n2))
        return n1 + n2
    
    def resta (self, n1, n2):
        print (str(n1) + ' - ' + str(n2))
        return n1 - n2
    
    def multiplicacion (self, n1, n2):
        print (str(n1) + ' x ' + str(n2))
        return n1 * n2
    
    def division(self, n1, n2):
        print (str(n1) + ' / ' + str(n2))
        return n1 / n2
    
    # Servidor de operaciones avanzadas        
    
    def seno(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.seno(num)
        print(str(resultado))
        
        transport.close()

        return resultado
    
    def aseno(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.aseno(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    def coseno(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.coseno(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    def acoseno(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.acoseno(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    def tangente(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.tangente(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    def atangente(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.atangente(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    def grados_a_radianes(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()

        resultado = cliente.grados_a_radianes(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    def radianes_a_grados(self, num):
        transport = TSocket.TSocket('localhost', 9091) 
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()

        resultado = cliente.radianes_a_grados(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    def potencia(self, base, exponente):
        transport = TSocket.TSocket('localhost', 9091)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.potencia(base, exponente)
        print(str(resultado))

        transport.close()

        return resultado
    
    def raizCuadrada(self, num):
        transport = TSocket.TSocket('localhost', 9091)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)

        cliente = OperacionesAvanzadas.Client (protocol)
        transport.open()
        
        resultado = cliente.raizCuadrada(num)
        print(str(resultado))

        transport.close()

        return resultado
    
    # SERVIDOR DE OPERACIONES CON VECTORES
    
    def sumav(self, v1, v2):
        transport = TSocket.TSocket('localhost', 9092)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraVectores.Client(protocol)
        transport.open()
        resultado = cliente.sumav(v1, v2) 
        transport.close()
        return resultado
    
    def restav(self, v1, v2):
        transport = TSocket.TSocket('localhost', 9092)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraVectores.Client(protocol)
        transport.open()
        resultado = cliente.restav(v1, v2) 
        transport.close()
        return resultado
    
    def producto_escalar(self, v1, v2):
        transport = TSocket.TSocket('localhost', 9092)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraVectores.Client(protocol)
        transport.open()
        resultado = cliente.producto_escalar(v1, v2) 
        transport.close()
        return resultado
    
    def producto_vectorial(self, v1, v2):
        transport = TSocket.TSocket('localhost', 9092)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraVectores.Client(protocol)
        transport.open()
        resultado = cliente.producto_vectorial(v1, v2) 
        transport.close()
        return resultado
    
    def vector_unitario(self, v):
        transport = TSocket.TSocket('localhost', 9092)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraVectores.Client(protocol)
        transport.open()
        resultado = cliente.vector_unitario(v) 
        transport.close()
        return resultado
    
    def multiplicacion_escalar(self, v1, num):
        transport = TSocket.TSocket('localhost', 9092)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraVectores.Client(protocol)
        transport.open()
        resultado = cliente.multiplicacion_escalar(v1, num) 
        transport.close()
        return resultado
    
    def modulo(self, v):
        transport = TSocket.TSocket('localhost', 9092)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraVectores.Client(protocol)
        transport.open()
        resultado = cliente.modulo(v) 
        transport.close()
        return resultado
    
    # SERVIDOR DE OPERACIONES CON MATRICES
    
    def sumaM(self, m1, m2):
        transport = TSocket.TSocket('localhost', 9093)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraMatrices.Client(protocol)
        transport.open()
        resultado = cliente.sumaM(m1, m2) 
        transport.close()
        return resultado
    
    def restaM(self, m1, m2):
        transport = TSocket.TSocket('localhost', 9093)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraMatrices.Client(protocol)
        transport.open()
        resultado = cliente.restaM(m1, m2) 
        transport.close()
        return resultado
    
    def productoM(self, m1, m2):
        transport = TSocket.TSocket('localhost', 9093)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        cliente = CalculadoraMatrices.Client(protocol)
        transport.open()
        resultado = cliente.productoM(m1, m2) 
        transport.close()
        return resultado

if __name__ == '__main__':
    handler = CalculadoraHandler()
    processor = Calculadora.Processor (handler)
    transport = TSocket.TServerSocket (host='127.0.0.1', port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print ('Iniciando servidor principal...')
    server.serve()
    print ('done.')