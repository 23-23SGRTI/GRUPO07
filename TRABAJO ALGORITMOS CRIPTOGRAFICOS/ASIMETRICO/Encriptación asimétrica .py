#GENERAR UNA CLAVE PÚBLICA Y PRIVADA
import time
from Crylpto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

start2=time.time()
#UTILIZAR LIBRERÍA PYCRIPTODOME
key = RSA.generate(2048)
private_key = key.export_key() #FUNCION PARA CREAR LA CLAVE PRIVADA

#CREACION DEL ARCHIVO
file_out = open("private.pem", "wb") #PRIVATE.PEM ES ARCHIVO DE CLAVE PRIVADA
file_out.write(private_key)
file_out.close()

#print("CLAVE PRIVADA")#IMPRIMIMOS LA CLAVE PRIVADA
#print(private_key)

#CREACION DEL ARCHIVO DE LA CLAVE PUBLICA
public_key = key.publickey().export_key()   #FUNCION PARA CREAR LA CLAVE PUBLICA
file_out = open("receiver.pem", "wb")       #RECEIVER.PEM ES EL NOMBRE DEL ARCHIVO DE CLAVE PUBLICA
file_out.write(public_key)                  #SE ESCRIBE LA CLAVE PUBLICA EN EL ARCHIVO
file_out.close()

end2=time.time()

#print("CLAVE PUBLICA") #IMPRIMIMOS LA CLAVE PÚBLICA
#print(public_key)
#print("Presione Enter")
#input()



#ENCRIPTACIÓN
print("ENCRIPTACIÓN DEL TEXTO")
start1=time.time()
data = open("texto.txt", "rb").read()#LECTURA DEL ARCHIVO texto.txt
end1=time.time()
print("LECTURA DEL ARCHIVO texto.txt")#IMPRIMIR CONTENIDO DEL ARCHIVO
print(data)
#print("Presione Enter")
#input()

start3=time.time()
file_out = open("encrypted_data.txt", "wb")

recipient_key = RSA.import_key(open("receiver.pem").read()) #LECTURA DE LA CLAVE DEL ARCHIVO RECEIVER PEM PONIENDOLO EN LA CLAVE DE RECIPIENTE
session_key = get_random_bytes(16)                          #SESSION KEY DE RANDOM BYTE

# ENCRIPTACION DE LA SESION CON LA CLAVE PUBLICA
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# ENCRIPTANDO LOS DATOS CON LA LLAVE DE SESION AES
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]

file_out.close()
end3=time.time()
#print("ENCRIPTACIÓN EXITOSA. PRESIONE ENTER")
#input()


#DESENCRIPTAR
print("DESENCRIPTACIÓN DEL TEXTO")
start4=time.time()
file_in = open("encrypted_data.txt", "rb")
print(file_in)

private_key = RSA.import_key(open("private.pem").read())


enc_session_key, nonce, tag, ciphertext = \
   [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]


# Decrypt the session key with the private RSA key
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)


# Decrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))
end4=time.time()
#print("DESENCRIPTACIÓN EXITOSA. PRESIONE ENTER")
#input()
print('T-E1' + " " + str(end1-start1))
print('T-E1' + " " + str(end2-start2))
print('T-E3' + " " + str(end3-start3))
print('T-E4' + " " + str(end4-start4))