def normalizar_lista(valores, modo):
    if modo not in ("minmax", "zscore", "unit"):
        raise ValueError("Modo inválido. Usa 'minmax', 'zscore' o 'unit'.")

    datos = list(valores)

    if modo == "minmax":
        minimo = min(datos)
        maximo = max(datos)
        rango = maximo - minimo

        if rango == 0:
            return [0.0 for _ in datos]

        resultado = []
        for x in datos:
            nuevo = (x - minimo) / rango
            resultado.append(nuevo)
        return resultado

    elif modo == "zscore":
        n = len(datos)
        media = sum(datos) / n

        suma_cuadrados = 0.0
        for x in datos:
            suma_cuadrados += (x - media) ** 2
        varianza = suma_cuadrados / n
        desviacion = varianza ** 0.5

        if desviacion == 0:
            return [0.0 for _ in datos]

        resultado = []
        for x in datos:
            nuevo = (x - media) / desviacion
            resultado.append(nuevo)
        return resultado

    elif modo == "unit":
        suma_cuadrados = 0.0
        for x in datos:
            suma_cuadrados += x ** 2
        norma = suma_cuadrados ** 0.5

        if norma == 0:
            return [0.0 for _ in datos]

        resultado = []
        for x in datos:
            nuevo = x / norma
            resultado.append(nuevo)
        return resultado
