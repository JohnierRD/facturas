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
nombre_cliente = input("Ingrese su Nombre y Apellido: ")
id_cliente = input("Ingrese su numero de identificacion: ")

formato_mensaje = (f"<h1> --- Factura No. {numero_factura} --- Fecha: {fecha} --- Cliente: {nombre_cliente} --- ID Cliente: {id_cliente} </h1>")

# Datos del producto (1-2-3-4-5)
# Datos a solicitar y evaluar - valor unitario - cantidad - subtotal - iva
"""
def usuarios():

"""
PORCENTAJE_IVA = 19

conteo_productos = 1                 # Saber en cuál producto vamos
precio_total = 0                     # Acumulador del total de productos
# Mientras que el conteo del productos sea menor o igual a 5
while conteo_productos <= 5:
    nombre_producto = input("Ingrese producto : ")
    precio_u = float(input("Ingresa el precio del producto número : "))
    cantidad = float(input("Ingrese la cantidad en unidades : "))
    precio_p = precio_u * cantidad
    
    # Convertir a flotante
    precio = float(precio_p)
    # Agregarlo al precio total
    precio_total += precio
    # Ya leímos un producto, le sumamos al conteo
    conteo_productos += 1

    formato_producto = "<h1>Producto: {} --- Precio: ${} --- Cantidad {} --- Subtotal ${} </h1>".format(nombre_producto, precio_u, cantidad, precio_p)
    #print(formato_producto)
# Cuando el ciclo termine calculamos el IVA
iva_producto = precio_total * (PORCENTAJE_IVA / 100)  # Dividir entre 100 porque es un porcentaje
# Sumar el iva_producto
precio_con_iva = precio_total + iva_producto
# Imprimir totales
#print(formato_producto)

print(f"Total: ${precio_total}")
print(f"IVA: ${iva_producto}")
print(f"Total con IVA: ${precio_con_iva}")







"""
for i in range(3):
    usuarios()"""


# Scrib para envio de correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


 #credenciales
proveedor_correo = 'smtp.live.com: 587'
remitente = 'jhyghhb@hotmail.com'
password = 'claves'
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
msg['To'] = 'jjjjjj@gmail.com'
msg['Subject'] = 'Prueba cliente correo ADSI RAPPI'
servidor.sendmail(msg['From'] , msg['To'], msg.as_string())

# Confirmacion de envio de factura al correo
print("******Se ha enviado la factura a su correo registrado******")
print("------------------ 2021 --------------------------------")

"""

#hoooooooooooo
#miiiiiiiii
