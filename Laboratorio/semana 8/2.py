
import sys
print("Versión de Python:", sys.version)

import sys
print("Antes de la terminación")
sys.exit()  # El programa se detendrá aquí
print("Después de la terminación")  # Esto no se imprimirá

import sys
original_stdout = sys.stdout
with open('output.txt', 'w') as f:
    sys.stdout = f
    print("Este texto se escribirá en output.txt en lugar de la consola.")
sys.stdout = original_stdout  # Restaurar la salida estándar
