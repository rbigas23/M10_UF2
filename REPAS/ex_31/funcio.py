def calcular_factura(preu, iva):
    iva = 21 if iva not in [4, 10, 21] else iva
    print(f"Valor sense IVA: {preu}€\nIVA: {iva}%\nTotal: {preu + (preu * iva / 100)}€")
