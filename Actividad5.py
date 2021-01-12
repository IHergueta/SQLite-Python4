import csvfile as csvfile

f = open("ventas.txt","r")
import sqlite3
from sqlite3 import Error

from main import *

import csv

try:
    con = sqlite3.connect("mi_erp.db")
    print("Conectandose a mi_erp.db")
    cur = con.cursor()
except Error:
    print(Error)
    con = sqlite3.connect("mi_erp.db")

try:

    for line in f:

        cur.execute("Insert into ventas(id,cdgproducto,cantidad,ciudad,importe,precio) Values(?, ?, ?, ?, ?, ?)", line)

    con.commit()


    print("Ventas insertadas correctamente")

except sqlite3.DatabaseError:

    print("No se ha isertado correctamente")


try:

    cur.execute("SELECT (cantidad*precio) from ventas")

    importe = cur.fetchall()




except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos")

try:

    cur.execute("update ventas set importe=(?)",importe)

    con.commit()

    print("Importe actualizado correctamente")

except sqlite3.DatabaseError:

    print("No se ha actualizado correctamente")


try:

    cur.execute("Select (cantidad*precio),ciudad from ventas ciudad='Sevilla'")

    datosS = cur.fetchall()

    con.commit()

    print("Datos Sevilla -> ",datosS)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos 2")

try:

    cur.execute("Select (cantidad*precio),ciudad from ventas ciudad='Huelva'")

    datosH = cur.fetchall()

    con.commit()

    print("Datos Huelva -> ",datosH)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos 2")

try:

    cur.execute("Select (cantidad*precio),ciudad from ventas ciudad='Cordoba'")

    datosC = cur.fetchall()

    con.commit()

    print("Datos Cordoba -> ",datosC)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos 2")

try:

    cur.execute("Select (cantidad*precio),ciudad from ventas ciudad='Almeria'")

    datosA = cur.fetchall()

    con.commit()

    print("Datos Almeria -> ",datosA)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos 2")

try:

    cur.execute("Select (cantidad*precio),ciudad from ventas ciudad='Cadiz'")

    datosCA = cur.fetchall()

    con.commit()

    print("Datos Sevilla -> ",datosCA)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos 2")


datos = datosCA + datosS + datosC + datosA + datosH
print(datos)

try:



    rows = [datos]

    fields = ["ventas","ciudad"]


    file = open("Acum_Ventas.csv", "w")

    with file as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)

        csvwriter.writerows(rows)


except sqlite3.DatabaseError:

     print("Algo ha ido mal")



try:

    cur.execute("Select productos.nombre,ventas.precio,ventas.cantidad,(ventas.cantidad*ventas.precio) from ventas join productos on ventas.cdgproducto=productos.id")

    prod = cur.fetchall()

    con.commit()

    print("Productos -> ",prod)

except sqlite3.DatabaseError:

    print("Algo ha ido mal en los datos 2")


try:



    rows = [prod]

    fields = ["Productos","precio","cantidad","importe"]


    file = open("Acum_Productos.csv", "w")

    with file as csvfile:

        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)

        csvwriter.writerows(rows)


except sqlite3.DatabaseError:

     print("Algo ha ido mal")



