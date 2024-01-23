def get_result(min, max):
    print(f"\nResultat de la suma: {str(min + max)}")
    print("\nValors entre els dos números: " + "".join([str(x) + " " for x in range(min + 1, max)]))
