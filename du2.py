import os
from tqdm import tqdm

# Función para leer las líneas eliminadas previamente
def leer_lineas_eliminadas(archivo_eliminadas):
    if os.path.exists(archivo_eliminadas):
        with open(archivo_eliminadas, 'r', encoding='utf-8') as file:
            return set(file.readlines())
    return set()

# Función para guardar las líneas eliminadas de manera única
def guardar_lineas_eliminadas(archivo_eliminadas, lineas_eliminadas):
    # Leer las líneas eliminadas previamente
    lineas_existentes = leer_lineas_eliminadas(archivo_eliminadas)
    
    # Actualizar el conjunto con las nuevas líneas eliminadas
    lineas_existentes.update(lineas_eliminadas)
    
    # Escribir el conjunto actualizado en el archivo eliminadas
    with open(archivo_eliminadas, 'w', encoding='utf-8') as file:
        file.writelines(lineas_existentes)

# Función para eliminar líneas duplicadas y actualizar las eliminadas
def eliminar_lineas_duplicadas(input_file, output_file, archivo_eliminadas):
    # Leer las líneas eliminadas previamente
    lineas_eliminadas_previas = leer_lineas_eliminadas(archivo_eliminadas)
    
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Leer las líneas únicas actuales
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as file:
            unique_lines = file.readlines()
    else:
        unique_lines = []

    # Convertir a conjunto para eliminar duplicados
    seen = set(unique_lines)
    nuevas_lineas_eliminadas = set()

    for line in tqdm(lines, desc="Procesando líneas", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}"):
        if line in seen or line in lineas_eliminadas_previas:
            nuevas_lineas_eliminadas.add(line)
        else:
            unique_lines.append(line)
            seen.add(line)

    # Escribir las líneas únicas en el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(unique_lines)

    # Guardar las nuevas líneas eliminadas
    guardar_lineas_eliminadas(archivo_eliminadas, nuevas_lineas_eliminadas)

# Main
if __name__ == "__main__":
    archivos_entrada = ['read1.txt', 'read2.txt', 'read3.txt']  # Lista de archivos a procesar
    output_file = 'mnemoncios.txt'
    archivo_eliminadas = 'eliminadas.txt'
    
    for input_file in archivos_entrada:
        if os.path.exists(input_file):
            eliminar_lineas_duplicadas(input_file, output_file, archivo_eliminadas)
            print(f"\033[92mLimpieza terminada para {input_file}\033[0m")
        else:
            print(f"El archivo {input_file} no existe.")

    print("Hecho Por May")
