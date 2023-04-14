#### eje 1 ####


print("#### eje 1 ####")

X =["dos", "uno","cinco"]

def encontrar(X,J):
    Y = 0
    for Z in X:
        Y = Y+1
        if Z == J:
            print("la posicion es:" + str(Y))

encontrar(X,"dos")

#### eje 2 ####
print("\n #### eje 2 ####\n")

check = False
while check == False:
    año = input("introducir año en numeros:  ")
    
    try:
        año = int(año)
        check = True
    except:
        print("valor introducido invalido")

def bisiesto(año):
    if (año % 4) == 0:
        print("El año introducido es bisiesto")
    else:
        print("El año introducido no es bisiesto")

bisiesto(año)

#### eje 3 ####
print("\n #### eje 3 #### \n")

check = False
while check == False:
    altura = input("introducir altura de un cuadrado a pintar en numeros:  ")
    
    try:
        altura = int(altura)
        check = True
    except:
        print("valor introducido invalido")

print("\n")

check = False
while check == False:
    ancho = input("introducir ancho de un cuadrado a pintar en numeros:  ")
    
    try:
        ancho = int(ancho)
        check = True
    except:
        print("valor introducido invalido")

caracter = input("Introducir caracter que conforma el cuadrado:  ")

def hacerCuadrado(altura,ancho,caracter):
    for N in range(int(altura)):
        print(caracter * ancho)

hacerCuadrado(altura,ancho,caracter)

#### eje 4 ####
print("\n #### eje 4 #### \n")

n_desorden = [1,4,2,7,43,10,5,3]
print(n_desorden)

def ordenar(lista):
    for a in range(len(lista)):
        for b in range(len(lista)-1):
            if lista[b] > lista[b+1]:
                hold = lista[b+1]
                lista[b+1] = lista[b]
                lista[b] = hold
    return lista

n_desorden = ordenar(n_desorden)

print(n_desorden)

#### eje 5 ####
print("\n #### eje 5 #### \n")

palindromo = input("Introducir una palabra para saber si es un palindromo:")

def darVuelta(palindromo):
    b = 0
    for v in range(len(palindromo)):
        
        if palindromo[-abs(v+1)] == palindromo[v]:
            b = b+1
        else:
            print("no es palindromo")
            break

    if b == len(palindromo):
            print("es palindromo")

darVuelta(palindromo)

#### eje 6 ####
print("\n #### eje 6 #### \n")

palabra= input("Introducir frase para contar sus vocales:  ")

def encontrarLetra(palabra):

    letra_a = 0
    letra_e = 0
    letra_i = 0
    letra_o = 0
    letra_u = 0

    for f in palabra:
        if f == "a":
            letra_a = letra_a +1
        elif f == "e":
            letra_e = letra_e +1
        elif f == "i":
            letra_i = letra_i +1
        elif f == "o":
            letra_o = letra_o +1
        elif f == "u":
            letra_u = letra_u +1
    
    print("La cantidad de vocales son:\n A= " + str(letra_a) + "\n E= " + str(letra_e) + "\n I= " + str(letra_i) + "\n O= " + str(letra_o) + "\n U= " + str(letra_u))

encontrarLetra(palabra)

#### eje 7 ####
print("\n #### eje 7 #### \n")



def step(numero):
    h = True
    for b in range(len(str(numero))-1):
        if (int(str(numero)[b+1])+1) != int(str(numero)[b]):
            if (int(str(numero)[b+1])-1) != int(str(numero)[b]):
                print("no es step")
                h = False
                break
    if h == True:
        print("si es step")

numero = 123234348
print("numero")
step(numero)

numero = 123234345
print("numero")
step(numero)