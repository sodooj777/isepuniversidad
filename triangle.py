import re # importamos el modulo re

# creamos la clase triangulo
class triangulo(): 
     
     #funcion de Constructror de clase  
    def __init__(self,a,b):
         self.a = a
         self.b = b
         self.c = a
         
            
    def __areat__(self):
        # validamos con un condiciona los datos a introducir solo pueden se r numero
        # y rango de busqueda a-z con el modulo re validamos los espacios en blanco   
        if re.search('[a-z ]' ,self.a) or re.search('[a-z]' ,self.b):
                   return("estos datos no son correctos intente nuevamente") 
                 
        if re.search('' ,self.a) and re.search('' ,self.b):
                   return("estos datos no son correctos intente nuevamente") 
    
        # reasignamos la variables self.a y b en un float dentro de a y b
        a=float(self.a) 
        b=float(self.b)
        
        # retorna el resultado por area =b *a /2 
        return("el resultado es  :", a * b / 2)

          

t = triangulo((input("Escriba la altura del triangulo lado a: ")) , (input("Escriba la altura del triangulo lado b : ")))

# heradamos de la clase triangulo
print(t.__areat__())
