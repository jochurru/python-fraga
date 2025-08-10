"""
Tipos de datos primitivos

"""
#Numeros.
Num= 1
print (Num)
print (type (Num))
Num2=1.2
print (Num2)
print (type (Num2))
#Los numeros pueden ser Int (enteros) y Float (con decimales)
#-----------------------------------------------------
#Cadenas de textos
cadena="hola mundo" #string con " "
cadena2='hola mundo2' #String con ' '
cadena3="""hola mundo con saltos de linea
en la parte de abajo
""" #String con cadena de texto usando """ """

print(cadena)
print (cadena2)
print(cadena3)
print(type (cadena))
print(type (cadena2))
print(type (cadena3))

#----------------------------------------------------------------------------------------------------

#Booleans

variable1=True
Variable2=False

if variable1 is True:
    print ("Es verdadero")
else:
    print ("Es falso")

if Variable2 is False:
    print("Es Falso")
else:
    print("Es verdadero")

print(type(variable1))
print(type(Variable2))
#Representan valores logicos que pueden ser verdaderos o falsos.
#----------------------------------------------------------------------------------------------------

"""
Listas, Tuplas y Diccionarios.

"""
#-----------------------------------------------------------------------------------------------------
#Listas (Se representan con corchetes y los elementos se separan con comas; las mismas son mutables )

lista1=[1,2,"hola",True,1.2,]

print (lista1)

print (type(lista1))

#------------------------------------------------------------------------------------------------------

#Tuplas (Se representan con parentesis y los elemenentos se separan con comas, las mismas son inmutables)

tupla1=(1,2,"Hola",False,1.3)

print (tupla1)

print (type (tupla1))

#-------------------------------------------------------------------------------------------------------

#Diccionarios (Se representan con llaves y los elementos estan representados con clave:valor y estan separados por dos puntos, estos son mutables.)

Diccionario1={"Nombre":"Jonatan","Apellido":"Churruarin","Edad":39}
print(Diccionario1)

print (type(Diccionario1))

#-------------------------------------------------------------------------------------------------------

#Slicing de Cadenas de textos y subcadenas.

Slicing= "Python es muy divertido"

print (Slicing[2:])

print(Slicing[:2])

print(Slicing [-1])

print (Slicing [0])

#----------------------------------------------------------------------------------------------------------


