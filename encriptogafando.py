import hashlib

def encriptografar(CPF,Senha):
    sha_signature = hashlib.sha256(CPF.encode()).hexdigest()
    teste=(sha_signature+Senha)
    sha_signature = hashlib.sha256(teste.encode()).hexdigest()
    print(sha_signature)


encriptografar('123.456.789-11','6706QZXQFF5P')