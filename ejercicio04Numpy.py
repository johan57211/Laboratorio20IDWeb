import numpy as np

def normalizar_lista_np(valores, modo):
    if modo not in ("minmax", "zscore", "unit"):
        raise ValueError("Modo inválido. Usa 'minmax', 'zscore' o 'unit'.")

    datos = np.array(valores, dtype=float)

    if modo == "minmax":
        minimo = np.min(datos)
        maximo = np.max(datos)
        rango = maximo - minimo

        if rango == 0:
            return np.zeros_like(datos).tolist()

        resultado = (datos - minimo) / rango
        return resultado.tolist()

    elif modo == "zscore":
        media = np.mean(datos)
        desviacion = np.std(datos)

        if desviacion == 0:
            return np.zeros_like(datos).tolist()

        resultado = (datos - media) / desviacion
        return resultado.tolist()

    elif modo == "unit":
        norma = np.linalg.norm(datos)

        if norma == 0:
            return np.zeros_like(datos).tolist()

        resultado = datos / norma
        return resultado.tolist()

valores = [10, 20, 30]

print(normalizar_lista_np(valores, "minmax"))
print(normalizar_lista_np(valores, "zscore"))
print(normalizar_lista_np(valores, "unit"))
print("Original:", valores)

