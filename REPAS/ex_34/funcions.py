
    
def get_quadrat_list(num_list, get_quadrat):
    quadrat_list = []
    for num in num_list:
        quadrat_list.append(get_quadrat(num))
    return quadrat_list