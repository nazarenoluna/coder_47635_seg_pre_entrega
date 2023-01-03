import json

def ingresar(datos):                                
    usuario = input('ingrese el usuario:')
    clave = input('ingrese la clave:') 
    datos[usuario]= clave
    return datos 
    

def mostrar(datos):    
    print('La info almacenada en la base de datos es :')    
    for key,value in datos.items():
        print(key,value)


def guardar(datos):
    ruta = r"C:/Users/Facha/Desktop/seg_pre_entrega" 
    with open(ruta+r"/lista_clientes.json","w") as file:
        json.dump(datos,file,indent=4)


def verificar(datos):           
    usuario = input('ingrese el usuario :')
    if usuario in datos:
        passw = input('ingrese la clave :')
        if datos[usuario] == passw:
            print('Has iniciado sesión')                
        else:
            print("contraseña incorrecta")
    else:
        print("no se ha encontrado el usuario")

