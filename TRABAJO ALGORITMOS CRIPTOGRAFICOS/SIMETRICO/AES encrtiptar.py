from cryptography.fernet import Fernet

# Generar clave
def cargar_clave():
    return open("clave.key", "rb").read()

# escribir y guardar la clave

def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Encriptar un mensaje

def encript(nom_archivo, clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb") as file:
        archivo_info = file.read()
    encrypted_data = f.encrypt(archivo_info)
    with open(nom_archivo, "wb") as file:
        file.write(encrypted_data)

#generar clave
generar_clave()
#carga la clave
clave = cargar_clave()

#encriptar
nom_archivo = "text.txt"
encript(nom_archivo, clave)
