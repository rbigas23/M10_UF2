user_input = input("Introdueix una frase: ")
frase = user_input.split()
for i, word in enumerate(frase):
    repeated_chars = []
    final_word = ""
    for char in word:
        if char not in repeated_chars:
            repeated_chars.append(char)
            final_word += char
    frase[i] = final_word
print(tuple(frase))