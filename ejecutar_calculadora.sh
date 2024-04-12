#!/bin/bash

# Navega a la carpeta donde se encuentra este script
#cd "$(dirname "$0")"

# Ejecuta servidor.py desde su carpeta en una nueva terminal
gnome-terminal -- bash -c "cd gen-py; python3 servidor_principal.py; exec bash"

# Ejecuta servidor_avanzado.py desde su carpeta en una nueva terminal
gnome-terminal -- bash -c "cd gen-py; python3 servidor_avanzado.py; exec bash"

# Ejecuta servidor_vectores desde su carpeta en una nueva terminal
gnome-terminal -- bash -c "cd gen-cpp; ./servidor_vectores; exec bash"

# Ejecuta CalcMatricesHandler.jar en una nueva terminal
gnome-terminal -- bash -c "java -jar CalcMatricesHandler.jar; exec bash"

# Ejecuta cliente.py desde su carpeta en una nueva terminal
gnome-terminal -- bash -c "cd gen-py; python3 cliente.py; exec bash"

