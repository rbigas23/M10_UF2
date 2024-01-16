contact_dict = {}
while (user_input := input("Introdueix un contacte, per acabar introdueix \"fi\": ")) != 'fi':
    data = user_input.split()
    key = data[0]
    if key in contact_dict:
        print("La persona ja s'ha afegit als contactes.")
    else:
        contact_dict[key] = data[1]
        print("Contacte afegit.")
print(f"Contactes: {contact_dict}")
