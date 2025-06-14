Palaba_buscada = input("Ingresa la palaba a buscar ")

with open("archivo.txt", "r") as archivo:
    continido = archivo.read()
    if palabra_busqueda in contenido:
        print("La palabra se encuentra en el archivo.")
    
    else:
        print("La palabra no esta en el archivo.")


