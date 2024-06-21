import os
import time
from tqdm import tqdm

# Función para eliminar líneas duplicadas
def eliminar_lineas_duplicadas(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Eliminar duplicados preservando el orden
    seen = set()
    unique_lines = []
    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)

    # Escribir las líneas únicas en el archivo de salida
    with open(output_file, 'w') as file:
        for line in tqdm(unique_lines, desc="Eliminando duplicados", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}"):
            file.write(line)
            time.sleep(0.01)  # Simulación de procesamiento para la barra de progreso

# Main
if __name__ == "__main__":
    input_file = 'read.txt'
    output_file = 'mnemoncios.txt'
    
    if os.path.exists(input_file):
        eliminar_lineas_duplicadas(input_file, output_file)
        print("\033[92mLimpieza terminada\033[0m")
        print("Hecho Por May")
    else:
        print(f"El archivo {input_file} no existe.")
