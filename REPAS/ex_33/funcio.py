def show_products(compra_dict, iva):
    for n_prod, preu in enumerate(compra_dict, 1):
        preu_descompte = preu - (preu * compra_dict[preu] / 100)
        total = preu_descompte + (preu_descompte * iva / 100)
        print(f"Producte {n_prod}: {total}€")