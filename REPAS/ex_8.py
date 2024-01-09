input = input("Introdueix de 1 a 3 paraules: ")
words = input.split()
for word in words:
    print(f"Paraula: {word} \n\tNúmero de caràcters: {len(word)} \n\tPrimer caràcter: {word[0]} \n\tÚltim caràcter: {word[-1]}")