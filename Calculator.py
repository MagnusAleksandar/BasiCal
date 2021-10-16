x=int(input("Ingrese el primer número: "))
y=int(input("Ingrese el segundo número: "))
z=str(input("Elija una operación:\n A. Suma\n B. Resta\n C. Multiplicación\n D. División.\n"))
def resultado (x,y,z):
    if z=="A" or z=="a" or z=="Suma" or z=="suma":
        print(x+y)
        return
    elif z=="B" or z=="b" or z=="Resta" or z=="resta":
        print(x-y)
        return
    elif z=="C" or z=="c" or z=="Multiplicación" or z=="Multiplicacion" or z=="multiplicacion" or z=="multiplicación":
        print(x*y)
        return
    elif z=="D" or z=="d" or z=="División"  or z=="división" or z=="Division" or z=="division":
        print(x/y)
        return
    else:
        print("Operación no válida")
        return

operacion=resultado(x,y,z)
print(operacion)