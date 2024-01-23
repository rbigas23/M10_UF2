def get_frase_dict(frase):
    frase_dict = {}
    for paraula in frase.split():
        frase_dict[paraula] = len(paraula)
    return frase_dict
