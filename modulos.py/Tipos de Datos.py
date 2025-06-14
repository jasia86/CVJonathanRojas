#Ejercicios Prácticos en Python

#Tipos de Datos


#	Identificación de Tipos de Datos

entero = int(42)
print(type(entero))

texto = str("Hola")
print(type("texto"))

decimal = float(3.14)
print(type(3.14))

A = bool(True)
print(type(A))

#Conversion de Tipos de datos

entero = 42
cadena = str(entero)
print("El valor entero convertido a cadena es:", cadena)



entero + 42
cadena = str(entero)
print("el valor entero convertido a cadena es:") , cadena

#Uso de Tipos de Datos:


nombre = "jonathan"
edad = 38
altura_pies = 5
altura_pulgadas = 4
es_estudiante = True


# Convertir la altura a metros (1 pie = 0.3048 metros, 1 pulgada = 0.0254 metros)
altura_metros = (altura_pies * 0.3048) + (altura_pulgadas * 0.0254)

print("Nombre:" , nombre)
print("Edad:" , edad)
print("Altura:" , altura_metros)
print("Eres estudiante de Programacion:" , es_estudiante)

#	Comparación de Tipos de Datos:

valor_entero = 10
valor_flotante = 10.0

print("El tipo de 10 es:" , type(valor_entero))
print("El tipo de 10.0 es:" , type(valor_flotante))


if type(valor_entero) == type(valor_flotante):
    print("Los tipos de 10 y 10.0 son iguales.")
else:
    print("Los tipo de 10 y 10.0 son difrentes.")



#	Operaciones con Diferentes Tipos de Datos:


numero_entero = 10
numero_flotante = 12.5
resultado_suma = numero_entero + numero_flotante

cadena1 = "Hola, "
cadena2 = "Jonathan"
resultado_concatenacion = cadena1+cadena2

print("el resultado de la suma es:" , resultado_suma)
print("el resultado de la concatenacion es:" , cadena1+cadena2)

#Variables

    #	Declaración de Variables:

nombre = "Jonathan"
print("Mi nombre es:" , nombre)

    #	Reasignación de Variables:

edad = 38
print("Mi edad actual es:" , edad)

edad = edad + 1

print("Mi edad el proxima año es:" , edad)


#	Uso de Variables:

carros_rojos = 10
carros_azules = 15

print("la suma es:" , carros_azules+carros_rojos)

# Intercambiar los valores de las variables
carros_rojos, carros_azules = carros_azules, carros_rojos

print("\nValores después del intercambio:")
print("Carros rojos =", carros_rojos)
print("Carros azules =", carros_azules)


print("la suma es:" , carros_azules+carros_rojos)

#	Concatenación de Variables:

saludo = "Hola"
nombre = "Jonathan Rojas"

#Frase Completa
frase_completa = saludo + nombre

#Imprimir Frase Completa

print (frase_completa)

#3. ¿Declaran y asignan valores a las variables?

ciudad = "Santo Domingo Norte"

print (ciudad)

numero = None

#valor 50

numero = 50


print (numero)

precio = 19.99

print("precio inicial:" , precio)

#cambia su valor a 24.99

precio = 24.99

print("precio actualizado:" , precio)

x, y, z = 1, 2, 3

print("x:" , x)
print("y:" , y)
print("z:" , z)

#Ejercicio 5:Cambio de Valor

estado = True
print("Estado inciial:" , True)

#Cambio de Valor a FALSE

estado = False
print("Estado actualizado:" , False)

#4. ¿Expresiones?

numero1 = 5
numero2 = 3

resultado = numero1 + numero2

print(resultado)

resultado = 5+3

print("El resultado de la suma es:" , resultado)

#Ejercicio 2: Expresión de Cadena

saludo = "Buenos" + " dias"

print(saludo)

#Ejercicio 3: Expresión Booleana

comparacion = 10 > 5

print("¿10 es mayor que 5?" , comparacion)

#Ejercicio 4: Expresión Matemática
#NO PUDE OBTENER EL RESULTADO


#Ejercicio 5: Expresión Compleja

Resultado_Final = (5 + 5) * 2 - 5

print("El resultado final es:" , Resultado_Final)

#5. Que son los operadores
#Son símbolos o palabras clave que realizan operaciones específicas 
#sobre uno o más valores (llamados operandos)

Igual = 20 / 4
print("El resultado de la division es:" , Igual)

#Ejercicio 3: Operador Lógico

evaluacion = (5 < 10) and (8 > 3)
print("El resultado de la evaluacion es:" , evaluacion)

#Ejercicio 4: Operador de Asignación

contador = 0
contador += 5

print ("El valor del resultado es:" , contador)

#Ejercicio 5: Operador de Concatenación

Mensaje = "Hola" + " Mundo"

print (Mensaje)



      









           
      
           


