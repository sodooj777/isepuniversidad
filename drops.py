#  lista y se convierte el numero en una cadena dentro de la lista con la funcion string
variable = [(str(39)),str(45),str(546),str(11)]

# se crea un diccionario para las gotas de agua
p1={1:'Plic',2:'Plac',3:'Ploc'} 

# imprimimos por pantalla la lista con el numero de la posicion  concatenada con el dicionario que queremos mostrar   
print(variable[0],"tiene 3 como factor pero no 7,5 el resultado seria :"+ p1[1] + "\n")
    
print(variable[1],"tiene 3,5 como factor pero no 7 el resultado seria :"+ p1[2],p1[1] + "\n")

print(variable[2],"tiene 3,7 como factor pero no 5 el resultado seria :"+ p1[2],p1[1] + "\n")

print(variable[3],"no tiene 3,5 y 7 como factor ")