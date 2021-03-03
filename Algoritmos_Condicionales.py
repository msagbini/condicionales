# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 20:41:53 2021

@author: RYZEN
"""
# Ejercicio 1
cantidad_camisas = int(input('Digite cuántas camisas va adquirir: '))
valor_compra = cantidad_camisas * 50000
if cantidad_camisas <= 0:
    print('No es un valor válido')
elif cantidad_camisas >= 3:
    valor_compra = valor_compra*0.7
    print(f'El valor a pagar con el 30% de descuento es de: {valor_compra}')
else:
    valor_compra = valor_compra*0.9
    print(f'El valor a pagar con el 10% de descuento es de: {valor_compra}')

# Ejercicio 2

valor_compra = float(input('Digite el valor de su compra: '))
valor_numero = float(input('Escoja un número: '))

if valor_numero < 74:
    valor_compra = valor_compra*0.15
    print(f'Descuento Aplicado del 15% por un valor de {valor_compra}')
else:
    valor_compra = valor_compra*0.20
    print(f'Descuento Aplicado del 20% por un valor de de {valor_compra}')

# Ejercicio 3

valor_fianza = float(input('Digite el valor de la fianza: '))

if valor_fianza > 0 and valor_fianza < 50000:
    valor_pagar = valor_fianza * 0.03
    print(f'El valor de la cuota es de: {valor_pagar}')
elif valor_fianza > 50000:
    valor_pagar = valor_fianza * 0.02
    print(f'El valor de la cuota es de: {valor_pagar}')
else:
    print("Digite un valor válido")
    
# ejercicio 4
dia1 = int(input("Digite los puntos emitidos el día 1: "))
dia2 = int(input("Digite los puntos emitidos el día 2: "))
dia3 = int(input("Digite los puntos emitidos el día 3: "))
dia4 = int(input("Digite los puntos emitidos el día 4: "))
dia5 = int(input("Digite los puntos emitidos el día 5: "))

p_contaminacion = (dia1 + dia2 + dia3 + dia4 + dia5) / 5
if p_contaminacion > 170:
    v_ganado = int(input("Digite lo ganado en los últimos 5 días: "))
    v_multa = v_ganado * 0.5
    print(f"El valor de la multa es: {v_multa}")
else:
    print(f"No hay multa, ya que el promedio {p_contaminacion} no es mayor a 170")

# Ejercicio 5

d_carro = int(input("Qué devaluación tendrá el auto en los próximos 3 años: "))
i_terren = int(input("Qué incremento tendrá el terreno los próximos 3 años: "))
if d_carro < i_terren * 0.5:
    print("Compra el carro")
else:
    print("No compres el carro")
                          
# Ejercicio 6

n_computadoras = int(input("Digite las computadoras que va a comprar: "))

if n_computadoras < 5 and n_computadoras >0:
    v_pagar = (11.000 * n_computadoras) * 0.9
    print(f"El valor a pagar es de: {v_pagar} por las {n_computadoras} computadoras.")
elif n_computadoras >= 5 and n_computadoras < 10:
    v_pagar = (11.000 * n_computadoras) * 0.8
    print(f"El valor a pagar es de: {v_pagar} por las {n_computadoras} computadoras.")
elif n_computadoras >= 10:
    v_pagar = (11.000 * n_computadoras) * 0.6
    print(f"El valor a pagar es de: {v_pagar} por las {n_computadoras} computadoras.")
else: 
    print("Digite un valor válido")
    
# Ejercicio 7

valor_estereo = int(input("Digite el valor de su estéreo: "))
marca = str(input("Digite 1 si la marca es NOSY, de lo contrario, 0: "))
if valor_estereo >= 2000 and marca == '1':
    v_pagar = (valor_estereo*0.84*0.85) + (valor_estereo * 0.16)
print(f"El valor de su estéreo es de: {v_pagar}")
elif valor_estereo >= 2000 and marca == '0':
    v_pagar = (valor_estereo*0.84*0.90) + (valor_estereo * 0.16)

else:
    print("Digite otro valor.")
    
# Ejercicio 8

monto_total = float(input("Digite el monto total de la compra: "))
if monto_total > 500000:
    c_invertir = monto_total * 0.55
    v_prestamo = monto_total * 0.3
    credito_fabricante = monto_total * 0.15
    intereses_fabricante = credito_fabricante*0.2
    print(f"La cantidad a invertir es: {c_invertir}, el valor del préstamo es de: {v_prestamo}, el valor del crédito es de: {credito_fabricante} y los intereses son: {intereses_fabricante}")
elif monto_total <= 500000:
    c_invertir = monto_total * 0.7
    credito_fabricante = monto_total * 0.3 
print(f"La cantidad a invertir es: {c_invertir}, el valor del préstamo es 0, el valor del crédito es de: {credito_fabricante} y los intereses son: {intereses_fabricante}")
else: 
    print("Digita un valor válido.")
    
    # Ejercicio 9
n1 = float(input("Digite el número 1: "))
n2 = float(input("Digite el número 2: "))
if n1 == n2:
    mult = n1*n2
    print(f"Los números son iguales y el resultado es: {mult}")
elif n1 > n2:
    resta = n1-n2
    print(f"El número 1 es mayor y la resta es: {resta}")
else:
    suma = n1+n2
    print(f"El número 2 es mayor y la suma es: {suma}")
    
# Ejercicio 10
n1 = float(input("Digite el número 1: "))
n2 = float(input("Digite el número 2: "))
n3 = float(input("Digite el número 3: "))

if n1 > n2 and n1 > n3:
    print(f"El numero mayor es el {n1}")
elif n2 > n1 and n2 > n3:
    print(f"El numero mayor es el {n2}")
elif n3 > n2 and n3 > n1:
    print(f"El numero mayor es el {n3}")
else: 
    print("Uno o más números son iguales.")