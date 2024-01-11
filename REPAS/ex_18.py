user_input = input("Introdueix dues paraules: ")
paraules = tuple(user_input.split())
print(f"Paraules: {paraules}")
for paraula in paraules:
    char_dict = {}
    chars = []
    for char in paraula:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(f"Freqüència de caràcters de la paraula \"{paraula}\": {char_dict}")