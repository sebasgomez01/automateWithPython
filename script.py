import os 
import shutil

# Obtengo la ruta del directorio actual
directorio_actual = os.getcwd()

# Creo una lista con todos sus elementos
elementos = os.listdir(directorio_actual)


# Itero sobre la lista de elementos
for elemento in elementos:

    # Obtengo la ruta completa del elemento
    archivo = os.path.join(directorio_actual, elemento)
    # obtengo el formato del archivo
    formato = os.path.splitext(archivo)[1]
    print(formato)

    # Verifico si es un archivo
    if os.path.isfile(archivo) and not elemento.endswith('.exe'):

    	# Defino el nombre de la carpeta
        nombre_carpeta = os.path.join(directorio_actual, formato)
        print(archivo)
        print(nombre_carpeta, os.path.exists(nombre_carpeta))

        # Chequeo si la carpeta existe:
        if os.path.exists(nombre_carpeta) and os.path.isdir(nombre_carpeta) and formato != '.exe':
        	# En el caso de que la carpeta exista simplemente quiero mover el archivo:
        	print("Muevo elemento")
            if not archivo_pertenece_a_carpeta(nombre_carpeta, archivo):
        	   shutil.move(archivo, nombre_carpeta)
        else:
        	# Si la carpeta no existe tengo que crearla y mover el archivo:
        	print("Creo carpeta, muevo elemento")
        	os.makedirs(nombre_carpeta)
        	shutil.move(archivo, nombre_carpeta)



# Función auxiliar para saber si un archivo pertenece a una carpeta

def archivo_pertenece_a_carpeta(carpeta, archivo):
    # Obtiene las rutas absolutas para asegurar que se comparen correctamente
    #ruta_absoluta_carpeta = os.path.abspath(carpeta)
    #ruta_absoluta_archivo = os.path.abspath(archivo)

    # Utiliza commonpath para obtener la ruta común más larga
    common_path = os.path.commonpath([carpeta, archivo])

    # Compara si la ruta común es igual a la ruta absoluta de la carpeta
    return common_path == ruta_absoluta_carpeta

