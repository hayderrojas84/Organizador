import os
import shutil

# Cambia esta ruta por la ruta que quieres organizar
ruta_objetivo ='C:/Users/User/Downloads'

tipos_archivos = {
    'Imágenes': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt'],
    'Hojas de cálculo': ['.xls', '.xlsx'],
    'Videos': ['.mp4', '.avi'],
    'Otros': []
}

def crear_carpeta(nombre):
    carpeta = os.path.join(ruta_objetivo, nombre)
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    return carpeta

def organizar_archivos():
    for archivo in os.listdir(ruta_objetivo):
        ruta_archivo = os.path.join(ruta_objetivo, archivo)
        if os.path.isfile(ruta_archivo):
            extension = os.path.splitext(archivo)[1].lower()
            encontrado = False
            for categoria, extensiones in tipos_archivos.items():
                if extension in extensiones:
                    destino = crear_carpeta(categoria)
                    shutil.move(ruta_archivo, os.path.join(destino, archivo))
                    encontrado = True
                    break
            if not encontrado:
                destino = crear_carpeta('Otros')
                shutil.move(ruta_archivo, os.path.join(destino, archivo))

organizar_archivos()
print("¡Organización completada!")
