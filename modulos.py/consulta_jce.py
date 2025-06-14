import requests

def obtener_datos_cedula(cedula):
    url = f"https://api.cedulado.microslab.com.do/api/cedulado/{cedula}"
    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            print("\n---- Datos de la cedula ----")
            print(f"Nombre: {datos['nombre']}")
            print(f"Apellidos: {datos['apellidos']}")
            print(f"Edad: {datos['edad']}")
            print(f"Sexo: {datos['sexo']}")

        else:
            print("No se pudo obtener la informacion. Verifique la cedula")
    except Exception as e:
        print(f"Error en la aplicacion: {e}")


cedula = input("Introduzca su cedula sin guiones): ")   
obtener_datos_cedula(cedula)





