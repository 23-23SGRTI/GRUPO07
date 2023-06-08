from cryptography.fernet import Fernet

# Cargar la clave
def cargar_clave():
    return open("clave.key", "rb").read()

# Desencriptar un mensaje
def desencript(nom_archivo, clave):
    f = Fernet(clave)
    with open(nom_archivo, "rb") as file:
        archivo_info = file.read()
    decrypted_data = f.decrypt(archivo_info)
    with open(nom_archivo, "wb") as file:
        file.write(decrypted_data)

# Cargar la clave
clave = cargar_clave()

nom_archivo = "text.txt"

# Desencriptar el archivo
desencript(nom_archivo, clave)
