import hashlib

def encriptografar(Valor1,Valor2):
    sha_signature = hashlib.sha256(Valor1.encode()).hexdigest()
    teste=(sha_signature+Valor2)
    sha_signature = hashlib.sha256(teste.encode()).hexdigest()
    print(sha_signature)


encriptografar('123.456.789-11','6706QZXQFF5P')