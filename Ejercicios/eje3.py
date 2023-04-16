## ACT 1 ##
print ("## ACT 1 ## \n")
def eje1():
    check1 = True
    
    while check1 == True:
        check2 = True
        check3 = True
        check4 = True
        
        while check2 == True:
            X = input("introducir un numero: ")
            try:
                X = int(X)

                check2= False
            except ValueError:
                print("valor introducido invalido")
        
        while check3 == True:
            Y = input("introducir otro numero: ")
            try:
                Y = int(Y)

                check3= False
            except ValueError:
                print("valor introducido invalido")
        print("suma:" + str(X + Y))

        while check4 ==True:
            print("Quiere seguir sumando? \n (1) SI \n (2) NO")
            X = input()

            if X == "1":
                check4 = False
            elif X == "2":
                check4 = False
                check1 = False
            else:
                print("porfavor solo responda con 1 o 2")


eje1()

## ACT 2 ##
print ("## ACT 2 ## \n")

def eje2():
    check1 = True
    
    while check1 == True:
        check2 = True
        check3 = True
        check4 = True
        
        while check2 == True:
            X = input("introducir un numero: ")
            try:
                X = int(X)

                check2= False
            except ValueError:
                print("valor introducido invalido")
        
        while check3 == True:
            Y = input("introducir otro numero: ")
            try:
                Y = int(Y)

                check3= False
            except:
                print("valor introducido invalido")
        
        
        try:
            print(str(X) + "/"+ str(Y) + "=" + str(X / Y))
        except ZeroDivisionError:
            print("No se puede dividir por cero")

        while check4 ==True:
            print("Quiere seguir dividiendo? \n (1) SI \n (2) NO")
            X = input()

            if X == "1":
                check4 = False
            elif X == "2":
                check4 = False
                check1 = False
            else:
                print("porfavor solo responda con 1 o 2")

eje2()

## ACT 3 ##
print ("## ACT 3 ## \n")

meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

print("ingrese un numero de mes para saber cual es su nombre")

check1 = True
check3= True

while check1 == True:

    check2= True

    while check2 == True:
        X = input()
        try:
            X = int(X)

            check2= False
        except ValueError:
            print("valor introducido invalido")
    
    try:
        print(str(meses[X-1]))
    except IndexError:
        print("no existe ese numero de mes")
    
    while check3 ==True:
        print("Quiere seguir viendo meses? \n (1) SI \n (2) NO")
        X = input()

        if X == "1":
            check3 = False
        elif X == "2":
            check3 = False
            check1 = False
        else:
            print("porfavor solo responda con 1 o 2")

## ACT 4 ##
print ("## ACT 4 ## \n")

cosa_a_escribir = 123

txt = open("act4.txt","w+")
txt.write("abc")
txt.close()

txt = open("act4.txt","w+")
try:
    txt.write(cosa_a_escribir)
except TypeError:
    txt.write(str(cosa_a_escribir))
txt.close()

txt = open("act4.txt","r")
print(txt.read())
txt.close()