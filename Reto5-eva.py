Productos = [
    ["Manzana","Fruta",3000],
    ["Queso","Lacteo",40000],
    ["Carne","Carnico",12000],
    ["leche","Lacteo",22000],
    ["Yogurt","Lacteo",6000],
    ["Jabon","Limpieza",23000]
]

for item in Productos:

    if item[1] == "Lacteo" and item[2] > 20000:
        descuento = "Descuento aplicado: ",item[2]-(item[2]*0.15)
    else:
        descuento = " "

    print (f"Nombre del producto: {item[0]}\n Categoria del producto {item[1]}\n valor base del producto {item[2]} \n {descuento}")
    print (f"\n")
