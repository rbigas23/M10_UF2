areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]
print(f"Segon element: {areas_pis[1]}\n"+
      f"Últim element: {areas_pis[-1]}\n"+
      f"Àrea terrassa: {areas_pis[7]}\n"+
      f"Del primer al tercer: {areas_pis[0:3]}\n"+
      f"Del tercer a l'últim: {areas_pis[2:]}\n"+
      f"Total àrea habitacions: {areas_pis[5] + areas_pis[-1]}"+
      f"")
areas_pis[9] = 9.16
print(f"Modificació lavabo: {areas_pis}")
areas_pis.extend(["Pati interior", 2.78])
print(f"Modificació pati interior: {areas_pis}")
print(f"Area total: {sum([i for x,i in enumerate(areas_pis) if not x % 2 == 0])}")