def foo(valor):
    #tenta transformar expressao em v ou f None = falso
    if valor:
        print("Valor é verdadeiro")
    else:
        print("Valor é falso")

foo(" ")
foo("")
foo(None)
bool(" ") #true
bool("") #false
bool(None) #false