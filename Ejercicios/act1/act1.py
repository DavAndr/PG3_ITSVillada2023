def creaListas():
    return ["cinco", "seis", "siete", "ocho"]

def Buscar(X):
    Z = 0
    for Y in X:
        Z = Z + 1
        if Y == "seis":
            print ("posicion:" + str(Z))
        

X = creaListas()
Buscar(X)