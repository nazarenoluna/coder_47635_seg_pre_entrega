class Cliente:
    
    def __init__(self,nombre,apellido,edad,email,busqueda):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.email = email 
        self.busqueda = busqueda


    def __str__(self):
        return f'Se ha creado el cliente {self.nombre} {self.apellido}'


    def comprar(self,articulo,vendedor):
        print(f'Hola {self.nombre}!! Has comprado tu {articulo} en la tienda {vendedor}!.\nTe enviaremos la fatura a tu email :{self.email}.\n Gracias por tu compra!. Saludos.')
        

    def consultar(self,articulo,vendedor):
        print(f'Hola {self.nombre}! Si tenemos {articulo} en Stock. Esperamos tu compra. Saludos atte {vendedor}')
       

