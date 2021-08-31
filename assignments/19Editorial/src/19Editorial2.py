def main():
    # escribe tu código abajo de esta línea
    import math
    numero_palabras = int(input("Dame el número de palabras: "))
    numero_paginas = math.ceil(numero_palabras / 475)
    total = (numero_paginas * 60)
    porcentaje = 90* total / 100 
    print("El costo de la publicación es:", porcentaje)

if __name__ == '__main__':
    main()
