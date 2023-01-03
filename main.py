from paquete1.modulo2 import Cliente# importando la clase Cliente   
from paquete1.modulo1 import *# importando todos los metodos de la primer pre entrega



cliente1 = Cliente("Pedro","Santillan",30,"pedsan@hotmail.com",["elctrodomesticos"])# atributos de la clase Cliente(nombre,apellido,edad,email,busqueda)
print('*'*50)
print(cliente1)# se imprime por la funcion str creada en la clase Cliente
print('*'*50)
cliente1.consultar("Heladeras","Rodo")# metodo consultar ,se ingresa el argumento de lo que busca comprar y la tienda
print('*'*50)
cliente1.comprar("Heladeras","Rodo")# metodo comprar, se ingresa de lo que va a comprar y la tienda. 
print('*'*50)


'''
usuario_passw = {}# el dict creado para las funciones de la 
usuario_passw = ingresar(usuario_passw)# llamado de las funcion ingresar de la 1er pre entrega 
mostrar(usuario_passw)# llamado de la funcion mmostrar de la 1er pre entrega 
guardar(usuario_passw)# llamado de la funcion guardad de la 1er pre entrega 
verificar(usuario_passw)# llamado de la funcion verificar de la 1er pre entrega 
'''