import funcio as f

compra_dict =  {100:10, 250:5, 1500:30, 420:20, 3:0, 8000:13}
iva = int(input("Introdueix el valor de l'IVA: "))
f.show_products(compra_dict, iva)