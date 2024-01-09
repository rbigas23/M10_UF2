input = input("Introdueix dues paraules: ")
words = input.split()
first_chars = words[0][0:2]
second_chars = words[1][0:2]
words[0] = second_chars + words[0][2:]
words[1] = first_chars + words[1][2:]
res = words[0] + " " + words[1]
print(f"Resultat: {res}")
