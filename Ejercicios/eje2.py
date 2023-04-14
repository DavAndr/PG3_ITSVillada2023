## ACT 1 ##
print ("## ACT 1 ## \n")

class Alumno_act1:

    def __init__(self,nombre) -> None:
        self.nombre = nombre
    
    def muestraNombre(self):
        print(self.nombre)

alumno1 = Alumno_act1("Jose")
alumno1.muestraNombre()
print("\n")
alumno2 = Alumno_act1("Pablo")
alumno2.muestraNombre()

## ACT 2 ##
print ("\n## ACT 2 ##")

class Alumno_act2:

    def __init__(self,nombre,nota) -> None:
        self.nombre = nombre
        self.nota = nota
    
    def muestraVar(self):
        print("nombre: " + self.nombre)
        print("nota: " + str(self.nota))

        if self.nota >= 6:
            print("esta aprobado")
        else:
            print("esta desaprobado")

alumno1 = Alumno_act2("Jose",10)
alumno1.muestraVar()
print("\n")
alumno2 = Alumno_act2("Pablo",2)
alumno2.muestraVar()

## ACT 3 ##
print ("\n## ACT 3 ##")

class Triangulo:
    def __init__(self,angulo_A,angulo_B,cara_A,cara_B) -> None:
        self.angulo_A = angulo_A
        self.angulo_B = angulo_B
        self.angulo_C = 180-(cara_A + cara_B)
        self.cara_A = cara_A
        self.cara_B = cara_B
        self.cara_C = ((cara_A*cara_A) + (cara_B*cara_B)) ** 0.5
        self.equilatero_var = (self.cara_A==self.cara_B) and (self.cara_B == self.cara_C)
    
    def mostrarLadoMayor(self):
        if self.cara_A < self.cara_B:
            y = self.cara_A
            self.cara_A = self.cara_B
            self.cara_B = y
        
        if self.cara_A < self.cara_C:
            y = self.cara_A
            self.cara_A = self.cara_C
            self.cara_C = y
        
        print("El lado mas grande del triangulo mide:" + str(self.cara_A) + "cm")
    
    def equilatero(self):
        if self.equilatero_var:
            print("Es equilatero")
        else:
            print("No es equilatero")

print("\nTriangulo 1")
triangulo_1 = Triangulo(90,10,50,40)
triangulo_1.mostrarLadoMayor()
triangulo_1.equilatero()

print("\n Triangulo 2")
triangulo_2 = Triangulo(45,45,100,100)
triangulo_2.mostrarLadoMayor()
triangulo_2.equilatero()

## ACT 4 ##
print ("\n## ACT 4 ##")

class Calculadora:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()
    
    def suma(self):
        print(str(self.x + self.y))
    
    def resta(self):
        print(str(self.x - self.y))
    
    def multiplicacion(self):
        print(str(self.x * self.y))
    
    def division(self):
        print(str(self.x / self.y))
    
calculadora = Calculadora(1,2)

## ACT 5 ##
print ("\n## ACT 5 ##")

class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def escribir(self):
        print("Nombre: " + self.nombre)
        print("Edad: "+ self.edad)

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo) -> None:
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    
    def tax(self):
        if int(self.sueldo) > 3000:
            print ("debe pagar impuestos")
        else:
            print ("no debe pagar impuestos")

persona = Persona("Juan","5 años")
persona.escribir()

print ("\n")

empleado = Empleado("Jose","30","1000")
empleado.escribir()
empleado.tax()

## ACT 6 ##
print ("\n## ACT 5 ##")

class Familia:
    def __init__(self,padre,madre,hijos) -> None:
        self.padre = padre
        self.madre = madre
        self.hijos = hijos
    
    def __str__(self) -> str:
        print(" Padre: " + self.padre + "\n Madre: " + self.madre)

        print("Hijos:")

        for x in self.hijos:
            print(x)

familia = Familia("Juan","Juana",["Paco","Martin","Juanito"])

familia.__str__()