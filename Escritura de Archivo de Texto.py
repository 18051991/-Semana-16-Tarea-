# Escritura de Archivo de Texto

# Especificamos el nombre del archivo que vamos a crear/abrir para escritura
nombre_archivo_escritura = "my_notes.txt"

# Abrimos el archivo en modo escritura ('w'). Si el archivo no existe, se crea.
# Si existe, su contenido anterior se sobrescribe.
try:
    with open(nombre_archivo_escritura, 'w') as archivo_escritura:
        # Escribimos tres líneas de notas personales en el archivo
        archivo_escritura.write("Recordatorio: Llamar al dentista para la cita.\n")
        archivo_escritura.write("Lista de compras: leche, huevos, pan, frutas.\n")
        archivo_escritura.write("Idea para el proyecto: Investigar sobre energías renovables.\n")
    print(f"Se han escrito las notas en el archivo '{nombre_archivo_escritura}'.")
except Exception as e:
    print(f"Ocurrió un error al escribir en el archivo: {e}")

# Lectura de Archivo de Texto

# Especificamos el nombre del archivo que vamos a abrir para lectura
nombre_archivo_lectura = "my_notes.txt"

# Abrimos el archivo en modo lectura ('r'). Si el archivo no existe, ocurrirá un error.
try:
    with open(nombre_archivo_lectura, 'r') as archivo_lectura:
        print(f"\nContenido del archivo '{nombre_archivo_lectura}':")
        # Leemos el archivo línea por línea utilizando readline()
        while True:
            linea = archivo_lectura.readline()
            # readline() devuelve una cadena vacía al llegar al final del archivo
            if not linea:
                break
            # Imprimimos cada línea leída (la línea ya incluye el carácter de nueva línea al final)
            print(linea, end='')  # Usamos end='' para evitar una doble línea en la consola
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo_lectura}' no fue encontrado.")
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")

# Cierre de Archivos
# El uso de 'with open(...)' asegura que el archivo se cierre automáticamente
# al salir del bloque 'with', incluso si ocurren errores.
# Por lo tanto, no necesitamos una instrucción de cierre explícita aquí.

print("\nOperaciones de lectura y escritura completadas.")
