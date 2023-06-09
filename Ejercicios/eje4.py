import math
##act 1##
print("act 1")

def password():
    password_var = "Abc1____"

    return password_var

def test_password():
    tested = password()
    assert len(tested) >= 8

    letras_mayus = False
    letras_minus = False
    letras_num = False

    for x in tested:

        if x.isupper():
            letras_mayus = True
        if x.islower():
            letras_minus = True
        if x.isnumeric():
            letras_num = True
    
    assert letras_mayus == True
    assert letras_minus == True
    assert letras_num == True

##act 2##
print("act 2")

def roman_to_decimal(y: str):
    decimal = 0

    for h in y:
        if h == "i" or h == "I":
            decimal = decimal+1
        elif h == "v" or h == "V":
            decimal = decimal+5
        elif h == "l" or h == "L":
            decimal = decimal+50
        elif h == "c" or h == "C":
            decimal = decimal+100
        elif h == "d" or h == "D":
            decimal = decimal+500
        elif h == "m" or h == "M":
            decimal = decimal+1000
    
    return decimal

def test_roman_to_decimal():
    assert roman_to_decimal("ivlcdm") == 1656
    assert roman_to_decimal('V') == 5

##act 3##
print("act 3")

def is_anagram(x,y):
    x_sorted = "".join(sorted(x))
    y_sorted = "".join(sorted(y))
    return y_sorted == x_sorted

def test_is_anagram():
    assert is_anagram("abcd","cdab") == True
    assert is_anagram("abcd","j") == False

##act 4##
print("act 4")

def calculate_statistics(x: list):
    total = 0
    desviaciones_total = 0

    for y in x:
        total = total + y
    
    promedio = total/len(x)

    desviaciones = []

    for y in x:
        desviaciones.append(pow(y-promedio, 2))
    
    for y in desviaciones:
        desviaciones_total = desviaciones_total + y
    
    varianza = desviaciones_total / len(x)
    desviacion_estandar = math.sqrt(varianza)
    return "promedio:" + str(promedio) + " // desviacion_estandar:" + str(desviacion_estandar)

def test_calculate_statistics():
    assert calculate_statistics([0,1,2,3,4,5,6,7,8,9,10]) == "promedio:5.0 // desviacion_estandar:3.1622776601683795"
    assert calculate_statistics([0,1000]) == "promedio:500.0 // desviacion_estandar:500.0"

##act 5##
print("act 5")

def search_matrix(matrix,target):

    estado = False

    for x in matrix:
        if x == target:
            estado = True
    
    return estado

def test_search_matrix():
    assert search_matrix([1,2,3,4,5,6], 5) == True
    assert search_matrix([[1,2,3,4,5,6],[7,8,9],[10]],[10]) == True
    assert search_matrix([[1,2,3,4,5,6],[7,8,9],[10]],[11]) == False