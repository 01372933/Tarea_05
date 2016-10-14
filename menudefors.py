# Enconding: UTF-8
#Blanca Flor Calderón Vázquez
#Ciclos for
from Graphics import*
from math import*


def dibujarCirculosYCuadrados():
    v=Window("Ciclos For",800,800)
    for espacio in range (0,400,10):
        circulo=Circle((400,400),espacio)
        rectangulo=Rectangle((390-espacio,390-espacio),(410+espacio,410+espacio))

def dibujarEstrella(angulo, longitud):
    v=Window("Ciclos For",800,800)
    t=Arrow((400,400),90)
    t.penDown()
    t.draw(v)
    t.forward(longitud)
    while t.x!=400 and t.y!=400:
    t.rotate(180-angulo)
    t.forward(longitud)
    

def dibujarEspiralDeCuadrados(espacio):
    v=Window("Ciclos For",800,800)
    t=Arrow((400,400),90)
    t.penDown()
    t.draw(v)
    for tramo in range (0,400,espacio)
        t.forward(tramo)
        t.rotate(90)

def dibujarCirculosEncirculos ():
    v=Window("Ciclos For",800,800)
    radio=300
    for i in range (0,360,longitud):
        x1Cor=400+radio*cos(i*pi/180)
        y1Cor=300-radio*sin(i*pi/180)
        for j in range (0,360,longitud):
            x2Cor=400+radio*cos(i*pi/180)
            y2Cor=300-radio*sin(i*pi/180)
        circulos=Circle((x1Cor,y1Cor),(x2Cor,y2Cor))
        circulos.draw(v)

def calcularValorAproximadoDePi ():
    for numero in range (1,100,1)
    numerote += (1/numero**2) 
    
    Pi=6*(numerote**.5)

def calcularCadenaDeOperacionesDeNumerosConsecutivos():# ESTOY HARTA DE VERDAD CON ESTA FUNCIÓN
    
    for clavedelaclave in range (2,9,1)
        clave=1
        clave =clave*10+clavedelaclave
        for numerosconsecutivos in range(1,123456789,clave):
            for numerosnaturales in range(1,9)
                operación=   numerosconsecutivos*8+numerosnaturales
        return operación 

def calcularCadenaDeOperacionesDeNumerosUnos ():
    clave=1
    clave =clave *10+1
    for termino in range (1,111111111,clave)
        palindrome= termino*termino
        print(palindrome)
#PODRÉ PENSAR CORRECTA Y LÓGICAMENTE MUY BIEN, PERO PASARLO A ESTA COSA DE PROGRAMACION ES AAAAGHHHHHHHHH CUANDO DEBES IR PASO POR PASO Y ESTA COSA NO TE COMPRENDE

def main ():
    eleccion=int(input("1.- Ilusión óptica. \2.- Símbolo satanista. \3.-Laberinto. \4.-Mandalalita. \5.-Valor aproximado de Pi. \6.- Cuenta regresiva. \7.-Palidromes numéricos. \8.-Nada ¿ Qué deseas ver? "
    
    if eleccion==8:
        reproduciendo="Pues cierra los ojos, si no quieres ver nada"
    
    else:
        while eleccion>0 and eleccion<9:
            if eleccion==1:
                dibujarCirculosYCuadrados()
            elif eleccion==2:
                dibujarEstrella()
            elif eleccion==3:
                dibujarEspiralDeCuadrados()
            elif eleccion==4:
                dibujarCirculosEncirculos()
            elif eleccion==5:
                reproduciendo=calcularValorAproximadoDePi ()
            elif eleccion==6:
                reproduciendo=calcularCadenaDeOperacionesDeNumerosConsecutivos()
            else:
                reproduciendo=calcularCadenaDeOperacionesDeNumerosUnos ()
    print (reproduciendo)
            
           
  

main()