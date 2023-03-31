from re import X

from sqlalchemy import false, true


def año():
    x = false

    while x == false:
        resultado = input("porfavor introducir un año en numeros")

        try:
            resultado = int(resultado)
            x = true
        except:
            print("valor introducido invalido")

    return resultado

año = año()

if (año % 4) == 0:
    print("a")
else:
    print("b")