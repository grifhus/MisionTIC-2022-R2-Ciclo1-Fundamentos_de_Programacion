# Taller Clase 4

# Este taller debe crear una biblioteca llamada **taller** y la solución de cada ejercicio se realizará en una función llamada _ejercicio_X_, donde _X_ es el número del ejercicio.  

# Adicionalmente, crear un archivo _prueba_ donde se escribirán los comandos para probar cada una de las funciones.

# **Nota**: si necesita crear funciones adicionales para resolver los ejercicios, debes crearlas en la biblioteca, en el archivo prueba no debes crear ninguna función. 

# ## Ejercicio 1
# Escribir una función a la que se le pase una cadena `<nombre>` y muestre por pantalla el saludo `¡hola <nombre>!`.

# def ejercicio_1(nombre):
#     return "Hola", nombre 
# print (ejercicio_1(input("Ingresa tu nombre: ")))

    


# ## Ejercicio 2
# Escribir una función que reciba un número entero positivo y devuelva su **factorial**.


# ## Ejercicio 3
# Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
# deberá aplicar un 19%.
# def calcular_iva(factura, iva):
    
#     if iva == None:
#         valorfactura = (0.19*factura) + factura
#         print("Total de la factura con IVA del 19% :", valorfactura)
#     else:
#         caliva = iva/100
#         valorfactura = (caliva*factura) + factura
#     print("Total de la factura con IVA del", iva,"% :", valorfactura)
    
# calcular_iva(20000)
#""PENDIENTE POR SOLUCIONAR""

# ## Ejercicio 4
# Escribir una función que calcule el área de un círculo 
# y otra que calcule el volumen de un cilindro usando la primera función.
#  import math
#  math.pi
#  def area_circulo(radio):
#      area = (radio*radio)* math.pi
#      print(area)
#      return area
# def volumen_cilindro(radio:int , altura:int):
#     import math
#     math.pi
#     def area_circulo(radio):
#         area = (radio*radio)* math.pi
#         print(area)
#         return area_circulo
#     volumen = (area_circulo(radio)* altura)
#     print(volumen)
    
# #     volumen =  * altura
# #     print(volumen)

# volumen_cilindro(5,7)
#falta llamr la fundion dentro de la toa funcion
    
# ## Ejercicio 5
# Escribir un programa que lea un entero positivo *n*, 
# introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta *n*. 
# La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:

# ![suma = \frac{n(n+1)}{2}](https://latex.codecogs.com/png.image?\dpi{140}\bg{white}suma=\frac{n(n&plus;1)}{2})

# ## Ejercicio 6
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase `Tu índice de masa corporal es <imc>` donde `<imc>`
# es el índice de masa corporal calculado redondeado con dos decimales.


# def masa(peso:int,estatura:int):
#     indice = peso/ ((estatura/100)**2)
#     return ('Tu índice de masa corporal es: ' "{0:.2f}".format(indice))  
# print (masa(int(input("Ingresa tu peso: ")),(int(input("Ingresa tu altura: ")))))
    
#Solucionado


# ## Ejercicio 7
# Una juguetería tiene mucho éxito en dos de sus productos:
# payasos y muñecas. Suele hacer venta por correo
# y la empresa de logística les cobra por peso de cada paquete
# así que deben calcular el peso de los payasos 
# y muñecas que saldrán en cada paquete a demanda.
# Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos 
# y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
# def jugueteria(payaso,muñeca):
#     pesopayaso = payaso * 112
#     pesomuñera = muñeca * 75
#     pesototal = pesopayaso + pesomuñera
#     print('Peso total del paquete es de: ', pesototal, 'Gramos' ) 
# print (jugueteria(int(input("Cantidad de Payasos: ")),(int(input("Cantidad de Muñecas: ")))))
#solucionado
    
# ## Ejercicio 8
# Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan,
# el descuento que se le hace por no ser fresca y el coste final total.
# def panaderia(panes):
#     panessindescuento = panes* 3.49
#     panescondescuento = (panes * 3.49)*0.6
#     descuento = panes-panescondescuento
#     print('Precio normal del pan es de:',"{0:.2f}".format(panessindescuento),"Euros." , 'El descuento por no estar fresco es de:', "{0:.2f}".format(descuento),"Euros." , 'Total a pagar:', "{0:.2f}".format(panescondescuento),"Euros." )
# print (panaderia(int(input("Cantidad de Panes Comprados: "))))
#Solucionado

# ## Ejercicio 9
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular 
# y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. 
# Redondear cada cantidad a dos decimales.
# def ahorros(cantidad):
#     primeraño = (cantidad*0.04)+ cantidad
#     segundoaño =(primeraño*0.04)+ primeraño
#     terceraño = (segundoaño*0.04)+ segundoaño
#     print("Cantidad de ahorros Primer año:", "{0:.2f}".format(primeraño),
#           "Cantidad de ahorros Segundo año:", "{0:.2f}".format(segundoaño),
#            "Cantidad de ahorros Tercer año:", "{0:.2f}".format(terceraño))
# print (ahorros(int(input("Ingresa cantidad dinero: "))))
#*Solucionado

# ## Ejercicio 10
# Crea un programa que dado un número entero que designa un periodo de tiempo expresado en segundos,
# imprima el equivalente en días, horas, minutos y segundos.  
# Por ejemplo: 
# * 300000 segundos serán 3 días, 11 horas, 20 minutos y 0 segundos.
# * 7400 segundos serán 0 días, 2 horas, 3 minutos y 20 segundos.
def tiempo(numero):
    dia = int(numero /86400)
    hora1 = numero % 86400
    minuto1 = hora1 % 3600
    segundos1 = minuto1 % 60
    #print(hora1)
    #print(minuto1)
    #print(segundos1)
    hora = int(hora1/3600)
    minuto = int(minuto1/60)
    segundos = int(segundos1/1)
    print(numero,"segundos serán",dia,"días,", hora, "horas,", minuto,"minutos y", segundos,"segundos.")  
# dia = 300000 % 86400
# horas = 40800 % 3600
# minutos= 1200 % 60
tiempo(300000)
tiempo(7400)
tiempo(12342567)