# En el mercado, podemos encontrar que el precio del producto 
# **Pernil Iberic D'Engreix Llen. Azuaga** en porción de 100 gramos cuesta 5,95€ 
# y el vendedor nos muestra que el precio por kilo cuesta 29,75€. ¿Crees que es correcto el precio?

# En este reto tienes que hacer un programa que calcule correctamente el precio por kilo del producto.
from copyreg import constructor
from importlib.metadata import packages_distributions


ciengramos = (5.95)
unkilo = ciengramos*10
print('Un kilo de Pernil Iberik DEngreix Llen vale :', unkilo, 'Euros')
#-----------------------------------------------------------------------------------------------------------
# ## Ejercicio 3: ¿Cuántos peces hay en el acuario?
# El agua de las granjas de Minnesota, Iowa, Illinois, Wisconsin,
# Missouri, Tennesse, Arkansas, Misssissipi y Louisiana desemboca en el 
# Océano Atlántico produciendo un fenómeno llamado zona muerta. 
# Debido a los altos niveles de nitrógeno y fósforo que traen estas aguas
# los peces mueren en grandes cantidades.

# Para evitar que mueran cientos y cientos de peces, la ONG Salvemos 
# los peces de colores ha decidido poner en cuarentena a 284 peces rojos y 163 
# peces azules en un gigantesco acuario, para devolverlos al mar cuando estén curados.
# ¿Cuántos peces hay en total dentro del acuario?

# ### Análisis del problema

# **¿Qué me pide el problema?**  
# Sumar los peces rojos y azules  

# **¿Qué datos necesito?**
# * Nº de peces rojos: 284  
# * Nº de peces azules: 163

# **¿Cómo debo responder?**  
# Imprimir en pantalla el total de peces

pecesrojos = 284
pecesazules = 163
totalpeces = pecesrojos + pecesazules
print("Total de peces :", totalpeces)
#-----------------------------------------------------------------------------------------------------------
## Ejercicio 4: ¿Cuánto se ha gastado Carmen?
# La posibilidad de ir al cine entre semana pagando un precio reducido es una tradición
# en las salas de cine españolas, lo que se conoce como El día del espectador.
# En algunos cines, el día del espectador suele ser los miércoles y las entradas se reducen hasta en un 70%. 
# La única pega es que suele ir mucha más gente...

# Para aprovechar el día del espectador, Carmen decide ir al cine con sus amigos y sale de su casa con 23€.
# Al regresar se da cuenta que le quedan 12.75€ ¿Sabrías programar cuánto se ha gastado?

# ### Análisis del problema

# **¿Qué me pide el problema?**  
# Restar el dinero sobrante por el restante
# **¿Qué datos necesito?**
#Dinero total
#Dinero restante
# **¿Cómo debo responder?**  
#Imprimir em pantalla cuanto dinero ha gastado
dinero_total = 23
dinero_restante = 12.75
dinero_gastado = dinero_total - dinero_restante
print('Carmen se ha gastado ', dinero_gastado, 'Euros en ir al cine')
## Ejercicio 5: ¿Cuánto te ha costado el ordenador?
# El videojuego en el ordenador está viviendo una nueva época de oro con un montón de juegos exclusivos. 
# Para comprarte un PC Gamer deberás fijarte principalmente en el procesador, la tarjeta gráfica,
# la memoria RAM... pero sobre todo en los accesorios como el teclado y ratón.

# Estás interesado en comprarte un nuevo PC y en la tienda de tu barrio cuesta 660€ 
# con todos los accesorios incluidos. Sin embargo, el vendedor te descuenta el 10% 
# por pronto pago ¿Cuánto tienes que pagar en total por el ordenador con todos los accesorios?

# ### Análisis del problema

# **¿Qué me pide el problema?**  
# Restar el total por el 10%
# **¿Qué datos necesito?**
# total costo 
# porcentaje descuento

# **¿Cómo debo responder?** 
#Imprimir el costo del pc despues del descuento
costo_pc = 660
descuento = 10
costopccondescuento = costo_pc - (costo_pc * descuento)/100 
print('El costo de la pc es de ', int(costopccondescuento), 'euros')
## Ejercicio 6: ¿Qué precio tenían antes del descuento?

En España, las rebajas de invierno suelen comenzar entre los días 1 y 7 de enero y finalizan a final de marzo. 
Por otro lado, las rebajas de verano empiezan durante la primera semana del mes de julio
y finalizan durante el mes de septiembre.

Para aprovechar la temporada de rebajas he salido de compras. He pagado 34€ por unos
pantalones que tenían un descuento del 15%. ¿Qué precio tenían antes de aplicar el descuento?


### Análisis del problema

## Ejercicio 6: ¿Qué precio tenían antes del descuento?

# En España, las rebajas de invierno suelen comenzar entre los días 1 y 7 de enero y finalizan a final de marzo. Por otro lado, las rebajas de verano empiezan durante la primera semana del mes de julio y finalizan durante el mes de septiembre.

# Para aprovechar la temporada de rebajas he salido de compras. He pagado 34€ por unos pantalones que tenían un descuento del 15%. ¿Qué precio tenían antes de aplicar el descuento?


# ### Análisis del problema

# **¿Qué me pide el problema?**  
#Calcular el valor del producto sin descuento

# **¿Qué datos necesito?**
#precio del producto
#porcentaje descuento

# **¿Cómo debo responder?**  




