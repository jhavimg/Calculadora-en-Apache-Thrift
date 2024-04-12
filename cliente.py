from calculadora import Calculadora
from calculadora.ttypes import EVector

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import math

transport = TSocket.TSocket ('localhost', 9090)
transport = TTransport.TBufferedTransport (transport)
protocol = TBinaryProtocol.TBinaryProtocol (transport)

client = Calculadora.Client (protocol)

transport.open()

def introducir_matriz():
    print ("Introduce el tamaño de la matriz a continuación")
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))

    matriz = []

    print("Introduce los elementos de la matriz fila por fila, separando los números con espacios:")

    for i in range(filas):
        fila = list(map(float, input(f"Fila {i+1}: ").split()))
        
        if len(fila) != columnas:
            print("Error: número incorrecto de elementos en la fila. Por favor, reintroduce la fila.")
            return introducir_matriz()
        
        matriz.append(fila)

    return matriz

print ("Hacemos ping al server")
client.ping()

print ("Se pueden realizar distintos tipos de operaciones:\n")
print ("-b: Para hacer operaciones básicas")
print ("-a: Para operaciones avanzadas")
print ("-v: Para operaciones con vectores")
print ("-m: Para operaciones con matrices")

comando = input ("Introduce el tipo de operación: ")

if(comando == '-b'):
    print("-b seleccionado. Operaciones básicas")
    num1 = input ("Introduce el primer número: ")
    op = input ("Introduce la operación (+,-,x,/): ")
    num2 = input ("Introduce el segundo número: ")

    num1 = float(num1)
    num2 = float(num2)

    if(op == '+'):
        resultado = client.suma (num1, num2)
        print (str(num1) + "+" + str(num2) + "="  + str(resultado))
    elif(op == '-'):
        resultado = client.resta (num1, num2)
        print (str(num1) + "-" + str(num2) + "="  + str(resultado))
    elif (op == 'x'):
        resultado = client.multiplicacion (num1, num2)
        print (str(num1) + "x" + str(num2) + "="  + str(resultado))
    elif (op == '/'):
        resultado = client.division (num1, num2)
        if (num2 == 0):
            print ("No se puede dividir entre 0")
        else:
            print (str(num1) + "/" + str(num2) + "="  + str(resultado))

elif (comando == '-a'):
    print ("Escoge una de los siguientes tipos de operaciones:")
    print ("sin: seno de un número")
    print ("asin: arcoseno de un número (numero entre -1 y 1)")
    print ("cos: coseno de un número")
    print ("acos: arcocoseno de un número  (numero entre -1 y 1)")
    print ("tan: tangente de un número")
    print ("atan: arcotangente de un número")
    print ("pow: Potencia de un número")
    print ("rt: Raíz cuadrada de un número")
    print ("g_r: Pasar de grados a radianes")
    print ("r_g: Pasar de radianes a grados")

    op = input("Introduce una operación: ")

    if (op == 'sin' or op == 'cos' or op == 'tan' or op == 'asin' or op == 'acos' or op == 'atan'):
        num = input("Introduce el ángulo en grados: ")
        num = float(num)
        angulo_radianes = client.grados_a_radianes(num)
        if (op == 'sin'):
            resultado = client.seno (angulo_radianes)
            print ("sin(" + str(num) + ")=" + str(resultado))
        elif (op == 'cos'):
            resultado = client.coseno (angulo_radianes)
            print ("cos(" + str(num) + ")=" + str(resultado))
        elif (op == 'tan'):
            resultado = client.tangente (angulo_radianes)
            print ("tan(" + str(num) + ")=" + str(resultado))
        elif (op == 'asin'):
            resultado = client.aseno (num)
            print ("asin(" + str(num) + ")=" + str(resultado))
        elif (op == 'acos'):
            resultado = client.acoseno (num)
            print ("acos(" + str(num) + ")=" + str(resultado))
        elif (op == 'atan'):
            resultado = client.atangente (num)
            print ("atan(" + str(num) + ")=" + str(resultado))

    elif (op == 'pow'):
        base = input ("Introduce la base de la potencia: ")
        exp = input ("Introduce el exponente de la potencia: ")
        base = float(base)
        exp = float(exp)
        resultado = client.potencia(base, exp)
        print ("potencia " + str(base) + "^" + str(exp) + "=" + str(resultado))
    elif (op == 'rt'):
        raiz = input ("Introduce el número para calcular raíz cuadrada: ")
        raiz = float(raiz)
        resultado = client.raizCuadrada(raiz)
        print ("Raíz cuadrada de " + str(raiz) + "=" + str(resultado))
    elif (op == 'g_r'):
        grados = input ("Introduce los grados: ")
        grados = float(grados)
        radianes = client.grados_a_radianes(grados)
        print (str(grados) + " grados son: " + str(radianes) + " radianes")
    elif (op == 'r_g'):
        radianes = input ("Introduce los radianes")
        radianes = float(radianes)
        grados = client.radianes_a_grados(radianes)
        print (str(radianes) + " radianes son: " + str(grados) + " grados")

elif (comando == '-v'):
    print ("Tipos de operaciones a realizar:")
    print ("+: Suma de vectores")
    print ("-: Resta de vectores")
    print ("p: Producto vectorial (vectores de 3 dimensiones)")
    print ("e: Producto escalar")
    print ("m: Modulo de un vector")
    print ("s: Multiplicacion escalar")
    print ("u: Vector unitario")

    op = input ("Introduce la operación: ")

    elementos_v1 = []
    elementos_v2 = []

    if (op == '+' or op == '-' or op == 'e'):
        tam = int(input("Introduce el tamaño de los vectores: "))

        print("Introduce los elementos del primer vector:")
        for i in range(tam):
            elemento = float(input(f"Elemento {i + 1}: "))
            elementos_v1.append(elemento)

        print("Introduce los elementos del segundo vector:")
        for i in range(tam):
            elemento = float(input(f"Elemento {i + 1}: "))
            elementos_v2.append(elemento)  

        v1 = EVector(elementos=elementos_v1, longitud=tam)
        v2 = EVector(elementos=elementos_v2, longitud=tam)

    elif (op == 'p'):
        tam = 3

        print("Introduce los elementos del primer vector:")
        for i in range(tam):
            elemento = float(input(f"Elemento {i + 1}: "))
            elementos_v1.append(elemento)

        print("Introduce los elementos del segundo vector:")
        for i in range(tam):
            elemento = float(input(f"Elemento {i + 1}: "))
            elementos_v2.append(elemento)  

        v1 = EVector(elementos=elementos_v1, longitud=tam)
        v2 = EVector(elementos=elementos_v2, longitud=tam)

    elif (op == 'm' or op == 'u'):
        tam = int(input("Introduce el tamaño del vector: "))

        print("Introduce el vector:")
        for i in range(tam):
            elemento = float(input(f"Elemento {i + 1}: "))
            elementos_v1.append(elemento)

        v1 = EVector(elementos=elementos_v1, longitud=tam)
    elif (op == 's'):
        tam = int(input("Introduce el tamaño del vector: "))

        print("Introduce el vector:")
        for i in range(tam):
            elemento = float(input(f"Elemento {i + 1}: "))
            elementos_v1.append(elemento)
        
        v1 = EVector(elementos=elementos_v1, longitud=tam)

        num = int(input("Introduce el número por el que multiplicas: "))
    else:
        print ("Opción no válida")

    if (op == '+'):
        resultado = client.sumav(v1, v2)
        print(f"Resultado de la suma: {resultado.elementos}")
    elif (op == '-'):
        resultado = client.restav(v1, v2)
        print(f"Resultado de la reta: {resultado.elementos}")  
    elif (op == 'e'):
        resultado = client.producto_escalar(v1, v2)
        print(f"Resultado del producto escalar: {resultado}") 
    elif (op == 'p'):
        resultado = client.producto_vectorial(v1, v2)
        print(f"Resultado del producto vectorial: {resultado.elementos}")
    elif (op == 'm'):
        resultado = client.modulo(v1)
        print(f"Resultado del modulo: {resultado}")
    elif (op == 's'):
        resultado = client.multiplicacion_escalar(v1, num)
        print(f"Resultado de la multiplicación escalar: {resultado.elementos}")
    elif (op == 'u'):
        resultado = client.vector_unitario(v1)
        print(f"Resultado del vector unitario: {resultado.elementos}")

elif (comando == '-m'):
    print ("Tipos de operaciones a realizar:")
    print ("+: Suma de matrices")
    print ("-: Resta de matrices")
    print ("x: Producto de matrices")
    
    op = input ("Introduce la operación: ")

    m1 = introducir_matriz()
    m2 = introducir_matriz()

    if (op == '+'):
        resultado = client.sumaM(m1, m2)
        print("Matriz resultado:")
        for fila in resultado:
            print(fila)
    elif (op == '-'):
        resultado = client.restaM(m1, m2)
        print("Matriz resultado:")
        for fila in resultado:
            print(fila)
    elif (op == 'x'):
        resultado = client.productoM(m1, m2)
        print("Matriz resultado:")
        for fila in resultado:
            print(fila)

transport.close()