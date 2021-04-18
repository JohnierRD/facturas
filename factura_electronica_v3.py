#factura Electronica
# Mensaje de bienvenida
tienda = "ADSI TOP - SU TIENDA DE ROPA"
print("ADSI TOP - SU TIENDA DE ROPA")

# Se llama la funcion fecha
from datetime import datetime

# Se determina el encabezado de la factura
numero_factura = 10001
fecha = datetime.now()
formato_tienda = "<h1> ------------- {} -------------- </h1>".format(tienda)

# Datos del cliente
nombre_cliente = input("\nIngrese su Nombre y Apellido: ")
id_cliente = input("Ingrese su numero de identificacion: ")

formato_mensaje = "<h1> --- Factura No. {} --- Fecha: {}\n --- Cliente: {} --- ID Cliente: {} </h1>".format(numero_factura, fecha, nombre_cliente, id_cliente)

# Datos del producto (1-2-3-4-5)
# Datos a solicitar y evaluar - valor unitario - cantidad - subtotal - iva

nombre_producto1 = input("Ingrese producto 1: ")
valor_unitario_producto1 = int(input("Ingrese precio producto 1: $"))
cantidad_producto1 = int(input("Ingrese la cantidad en unidades: "))
precio_producto1= valor_unitario_producto1 * cantidad_producto1
# precio_final_producto1 = int(precio_producto1) * 0.19 + int(precio_producto1)
iva_producto1 = int(precio_producto1) * 0.19
formato_producto1 = "<h1>Producto: {} --- Precio: ${} --- Cantidad {} --- Subtotal ${} </h1>".format(nombre_producto1, valor_unitario_producto1, cantidad_producto1, precio_producto1)

nombre_producto2 = input("Ingrese producto 2: ")
valor_unitario_producto2 = int(input("Ingrese precio producto 2: $"))
cantidad_producto2 = int(input("Ingrese la cantidad en unidades: "))
precio_producto2 = valor_unitario_producto2 * cantidad_producto2
#precio_final_producto2 = int(precio_producto2) * 0.19 + int(precio_producto2)
iva_producto2 = int(precio_producto2) * 0.19
formato_producto2 = "<h1>Producto: {} --- Precio: ${} --- Cantidad {} --- Subtotal ${} </h1>".format(nombre_producto2, valor_unitario_producto2, cantidad_producto2, precio_producto2)

nombre_producto3 = input("Ingrese producto 3: ")
valor_unitario_producto3 = int(input("Ingrese precio producto 3: $"))
cantidad_producto3 = int(input("Ingrese la cantidad en unidades: "))
precio_producto3= valor_unitario_producto3 * cantidad_producto3
#precio_final_producto3 = int(precio_producto3) * 0.19 + int(precio_producto3)
iva_producto3 = int(precio_producto3) * 0.19
formato_producto3 = "<h1>Producto: {} --- Precio: ${} --- Cantidad {} --- Subtotal ${} </h1>".format(nombre_producto3, valor_unitario_producto3, cantidad_producto3, precio_producto3)

nombre_producto4 = input("Ingrese producto 4: ")
valor_unitario_producto4 = int(input("Ingrese precio producto 4: $"))
cantidad_producto4 = int(input("Ingrese la cantidad en unidades: "))
precio_producto4= valor_unitario_producto4 * cantidad_producto4
#precio_final_producto4 = int(precio_producto1) * 0.19 + int(precio_producto4)
iva_producto4 = int(precio_producto4) * 0.19
formato_producto4 = "<h1>Producto: {} --- Precio: ${} --- Cantidad {} --- Subtotal ${} </h1>".format(nombre_producto4, valor_unitario_producto4, cantidad_producto4, precio_producto4)

nombre_producto5 = input("Ingrese producto 5: ")
valor_unitario_producto5 = int(input("Ingrese precio producto 5: $"))
cantidad_producto5 = int(input("Ingrese la cantidad en unidades: "))
precio_producto5= valor_unitario_producto5 * cantidad_producto5
#precio_final_producto5 = int(precio_producto5) * 0.19 + int(precio_producto5)
iva_producto5 = int(precio_producto5) * 0.19
formato_producto5 = "<h1>Producto: {} --- Precio: ${} --- Cantidad {} --- Subtotal ${} </h1>".format(nombre_producto5, valor_unitario_producto5, cantidad_producto5, precio_producto5)

# Resumen de valores Calculados
subtotal = precio_producto1 + precio_producto2 + precio_producto3 + precio_producto4 + precio_producto5
iva = iva_producto1 + iva_producto2 + iva_producto3 + iva_producto4 + iva_producto5

total_pagar = subtotal + iva
formato_total_pagar = "<h1> Subtotal: ${} --- Iva: ${} ***** TOTAL A PAGAR: ${}\n***** !!!!!! GRACIAS POR SU COMPRA!!!!! </h1>".format(subtotal,iva, total_pagar)

# Elaborado por quien
elaborado = "L3J - 2021"
formato_elaborado = "<h1> ------------------------- {} ---------------------------------- </h1>".format(elaborado)

# Salida en pantalla de los valores y subvalores - confirmacion visual de la factura

print("\nPREVISUALIZACIÓN")
print(formato_tienda)
print(formato_mensaje)
print(formato_producto1)
print(formato_producto2)
print(formato_producto3)
print(formato_producto4)
print(formato_producto5)
print(formato_total_pagar)

# Scrib para envio de correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#credenciales
proveedor_correo = 'smtp.live.com: 587'
remitente = 'jhonier1608@hotmail.com'
password = '5466437,.'
#conexion a servidor
servidor = smtplib.SMTP(proveedor_correo)
servidor.starttls()
servidor.ehlo()
#autenticacion
servidor.login(remitente, password)
#mensaje 
mensaje = "<h1> {} {} {} {} {} {} {} {} {} </h1>".format(formato_tienda, formato_mensaje, formato_producto1, formato_producto2, formato_producto3, formato_producto4, formato_producto5, formato_total_pagar, formato_elaborado) 

msg = MIMEMultipart()
msg.attach(MIMEText(mensaje, 'html'))
msg['From'] = remitente
msg['To'] = 'jjrodu@gmail.com'
msg['Subject'] = 'Prueba cliente correo ADSI RAPPI'
servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

# Confirmacion de envio de factura al correo
print("******Se ha enviado la factura a su correo registrado******")
print("------------------ 2021 --------------------------------")

#hola