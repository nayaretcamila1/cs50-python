#haremos un programa interactivo solicitando informacion al user
#utilizaremos otra funcion incorporada llamada input que permite obtener la entrada del teclado

#las funciones pueden retomar valores y esos valores los podemos gardar en la memoria del computador utilizando inicialmente variables

#asignando el valor de retorno de la funion input a una variable de nombre name
name = input("¿como te llamas?")

#luego saludaremos al user
#llamaremos a la funcion print con 2 arumentos : "hola" y el segundo argumento es la variable name. los argumentos al llamar a una funcion se separan con coma
print ("hola", name)

print (f"hola {name}")