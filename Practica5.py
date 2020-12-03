print ("Coste de la comida ordenada en el restaurante?.")
preu= input ("¿Cuanto os costó la comida en el restaurante? ")

a= float (preu)

iva= a*0.1
b= (iva)
print("El IVA es de: " +str (b)+"€")

propina= a*0.1
c= (propina)
print("La propina es de: " +str (c)+ "€")

preu_total= a+b+c
print("El precio total es de: "+str(precio_total)+"€")
