#SHA-256
import hashlib
m = hashlib.sha256(b'daniela123')
print(m.digest())
#b"]xb3xa6(x06x10!x8ax1cx0bxbfxd9x9fx19x82x1e{r$m'x11xc9xf0xc7x9cx1fx17xfdFxa09"

#----------------------------------
#si hacemos un cambio en la cadena "mensaje lo escribimos la m con mayuscula el resultado
#totalmente diferente asi 
m = hashlib.sha256(b"Daniela123")
print(m.digest())
#b'xd2xaf1q.xadx04x14hxc1xc6xfaLvV\\xe0xf9xb1x93x10x079xffQxb9x07xe4xe3x818'

#MD5
#la misma sistaxis pero diferente nombre/*
m = hashlib.md5(b"Daniela123")
print(m.digest())
#b'&Rxeexe0x1d& xe9xc5xe5_jxc9xd4xb43'

#update()  actualiza el objeto hash añadiendo una nueva cadena. Reiteradas llamadas son equivalentes a una sola con la concatenación de las cadenas/*
m = hashlib.sha256()
m.update(b"mensaje")
m.update(b"cifrado")
print(m.digest())
#Es lo mismo que 
m = hashlib.sha256(b"mensaje" + b"cifrado")
print(m.digest())