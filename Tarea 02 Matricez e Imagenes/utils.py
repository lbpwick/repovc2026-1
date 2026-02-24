# utils.py
"""
De texto a imagen
─────────────────
Módulo principal con toda la lógica del proyecto:
  - Alfabeto de matrices binarias 7 filas × ancho variable
  - Normalización de texto
  - Composición de palabras
  - Escalado nearest-neighbor
  - Renderizado y guardado con colores configurables
"""

import os
import numpy as np
from PIL import Image
import matplotlib.colors as mcolors

# ──────────────────────────────────────────────
# 1. ALFABETO  (7 filas × ancho variable)
# ──────────────────────────────────────────────

ALTO_LETRA = 7

def _m(rows):
    """Convierte lista de cadenas '01...' a ndarray uint8."""
    return np.array([[int(c) for c in r] for r in rows], dtype=np.uint8)

ALFABETO = {
    # ── minúsculas ────────────────────────────────────────────
    "a": _m(["0110","1001","1001","1111","1001","1001","1001"]),
    "b": _m(["1110","1001","1001","1110","1001","1001","1110"]),
    "c": _m(["0110","1001","1000","1000","1000","1001","0110"]),
    "d": _m(["1110","1001","1001","1001","1001","1001","1110"]),
    "e": _m(["1111","1000","1000","1110","1000","1000","1111"]),
    "f": _m(["1111","1000","1000","1110","1000","1000","1000"]),
    "g": _m(["0110","1001","1000","1011","1001","1001","0110"]),
    "h": _m(["1001","1001","1001","1111","1001","1001","1001"]),
    "i": _m(["010","010","010","010","010","010","010"]),
    "j": _m(["0001","0001","0001","0001","0001","1001","0110"]),
    "k": _m(["1001","1010","1100","1000","1100","1010","1001"]),
    "l": _m(["10","10","10","10","10","10","11"]),
    "m": _m(["10001","11011","10101","10101","10001","10001","10001"]),
    "n": _m(["1001","1101","1101","1011","1011","1001","1001"]),
    "o": _m(["0110","1001","1001","1001","1001","1001","0110"]),
    "p": _m(["1110","1001","1001","1110","1000","1000","1000"]),
    "q": _m(["0110","1001","1001","1001","1101","0110","0001"]),
    "r": _m(["1110","1001","1001","1110","1010","1001","1001"]),
    "s": _m(["0110","1001","1000","0110","0001","1001","0110"]),
    "t": _m(["111","010","010","010","010","010","010"]),
    "u": _m(["1001","1001","1001","1001","1001","1001","0110"]),
    "v": _m(["1001","1001","1001","1001","1010","1010","0100"]),
    "w": _m(["10001","10001","10001","10101","10101","11011","10001"]),
    "x": _m(["1001","1001","0110","0110","0110","1001","1001"]),
    "y": _m(["1001","1001","0110","0110","0100","0100","0100"]),
    "z": _m(["1111","0001","0010","0100","1000","1000","1111"]),

    # ── mayúsculas (idénticas a minúsculas para simplificar) ──
    "A": _m(["0110","1001","1001","1111","1001","1001","1001"]),
    "B": _m(["1110","1001","1001","1110","1001","1001","1110"]),
    "C": _m(["0110","1001","1000","1000","1000","1001","0110"]),
    "D": _m(["1110","1001","1001","1001","1001","1001","1110"]),
    "E": _m(["1111","1000","1000","1110","1000","1000","1111"]),
    "F": _m(["1111","1000","1000","1110","1000","1000","1000"]),
    "G": _m(["0110","1001","1000","1011","1001","1001","0110"]),
    "H": _m(["1001","1001","1001","1111","1001","1001","1001"]),
    "I": _m(["010","010","010","010","010","010","010"]),
    "J": _m(["0001","0001","0001","0001","0001","1001","0110"]),
    "K": _m(["1001","1010","1100","1000","1100","1010","1001"]),
    "L": _m(["10","10","10","10","10","10","11"]),
    "M": _m(["10001","11011","10101","10101","10001","10001","10001"]),
    "N": _m(["1001","1101","1101","1011","1011","1001","1001"]),
    "O": _m(["0110","1001","1001","1001","1001","1001","0110"]),
    "P": _m(["1110","1001","1001","1110","1000","1000","1000"]),
    "Q": _m(["0110","1001","1001","1001","1101","0110","0001"]),
    "R": _m(["1110","1001","1001","1110","1010","1001","1001"]),
    "S": _m(["0110","1001","1000","0110","0001","1001","0110"]),
    "T": _m(["111","010","010","010","010","010","010"]),
    "U": _m(["1001","1001","1001","1001","1001","1001","0110"]),
    "V": _m(["1001","1001","1001","1001","1010","1010","0100"]),
    "W": _m(["10001","10001","10001","10101","10101","11011","10001"]),
    "X": _m(["1001","1001","0110","0110","0110","1001","1001"]),
    "Y": _m(["1001","1001","0110","0110","0100","0100","0100"]),
    "Z": _m(["1111","0001","0010","0100","1000","1000","1111"]),

    # ── dígitos ───────────────────────────────────────────────
    "0": _m(["0110","1001","1011","1101","1001","1001","0110"]),
    "1": _m(["010","110","010","010","010","010","111"]),
    "2": _m(["0110","1001","0001","0010","0100","1000","1111"]),
    "3": _m(["0110","1001","0001","0110","0001","1001","0110"]),
    "4": _m(["0010","0110","1010","1010","1111","0010","0010"]),
    "5": _m(["1111","1000","1000","1110","0001","1001","0110"]),
    "6": _m(["0110","1001","1000","1110","1001","1001","0110"]),
    "7": _m(["1111","0001","0010","0010","0100","0100","0100"]),
    "8": _m(["0110","1001","1001","0110","1001","1001","0110"]),
    "9": _m(["0110","1001","1001","0111","0001","1001","0110"]),

    # ── especiales ────────────────────────────────────────────
    " ": np.zeros((ALTO_LETRA, 3), dtype=np.uint8),
    ".": _m(["00","00","00","00","00","11","11"]),
    "?": _m(["0110","1001","0001","0010","0100","0000","0100"]),
}

# ──────────────────────────────────────────────
# 2. NORMALIZAR TEXTO
# ──────────────────────────────────────────────

def normalizar_texto(texto: str) -> list:
    """
    Devuelve lista de caracteres soportados.
    Los caracteres no soportados se sustituyen por '?'.
    Maneja equivalencias simples de acentos y ñ.
    """
    equivalencias = {
        "á":"a","é":"e","í":"i","ó":"o","ú":"u",
        "Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U",
        "ñ":"n","Ñ":"N","ü":"u","Ü":"U",
    }
    resultado = []
    for ch in texto:
        ch2 = equivalencias.get(ch, ch)
        resultado.append(ch2 if ch2 in ALFABETO else "?")
    return resultado

# ──────────────────────────────────────────────
# 3. COMPOSICIÓN DE PALABRA
# ──────────────────────────────────────────────

def texto_a_matriz(
    texto: str,
    espacio_letras: int = 1,
    espacio_palabras: int = 3,
    margen_sup: int = 0,
    margen_inf: int = 0,
    margen_izq: int = 0,
    margen_der: int = 0,
) -> np.ndarray:
    """
    Convierte un texto en una matriz binaria 2-D.
    Parámetros
    ----------
    texto          : cadena de caracteres
    espacio_letras : columnas de fondo entre letras consecutivas
    espacio_palabras: columnas extra después de un espacio
    margen_*       : filas/columnas de fondo añadidas al borde
    """
    chars = normalizar_texto(texto)
    if not chars:
        return np.zeros((ALTO_LETRA, 1), dtype=np.uint8)

    columnas = []
    sep_letra = np.zeros((ALTO_LETRA, espacio_letras), dtype=np.uint8)
    sep_palabra = np.zeros((ALTO_LETRA, espacio_palabras), dtype=np.uint8)

    for i, ch in enumerate(chars):
        mat = ALFABETO[ch]
        columnas.append(mat)
        if i < len(chars) - 1:
            columnas.append(sep_palabra if ch == " " else sep_letra)

    imagen = np.concatenate(columnas, axis=1)

    # Añadir márgenes
    alto = margen_sup + ALTO_LETRA + margen_inf
    ancho = margen_izq + imagen.shape[1] + margen_der
    resultado = np.zeros((alto, ancho), dtype=np.uint8)
    resultado[margen_sup:margen_sup + ALTO_LETRA,
              margen_izq:margen_izq + imagen.shape[1]] = imagen
    return resultado

# ──────────────────────────────────────────────
# 4. ESCALADO (nearest-neighbor)
# ──────────────────────────────────────────────

def escalar_matriz(matriz: np.ndarray, factor: int = 1) -> np.ndarray:
    """
    Escala la matriz por un factor entero usando np.kron
    (equivalente a nearest-neighbor).
    """
    if factor < 1:
        raise ValueError(f"El factor de escala debe ser >= 1, se recibió {factor}.")
    if factor == 1:
        return matriz.copy()
    bloque = np.ones((factor, factor), dtype=np.uint8)
    return np.kron(matriz, bloque)

# ──────────────────────────────────────────────
# 5. RENDERIZADO Y GUARDADO
# ──────────────────────────────────────────────

def _color_a_rgb(color) -> tuple:
    """
    Acepta:
      - Tupla/lista RGB int 0-255  → (R, G, B)
      - Nombre de color matplotlib → (R, G, B)
      - Hex '#RRGGBB'              → (R, G, B)
    Lanza ValueError con mensaje claro si el formato es inválido.
    """
    if isinstance(color, (tuple, list)):
        if len(color) != 3:
            raise ValueError(f"La tupla RGB debe tener exactamente 3 elementos: {color}")
        for v in color:
            if not (isinstance(v, int) and 0 <= v <= 255):
                raise ValueError(
                    f"Cada componente RGB debe ser un entero entre 0 y 255. "
                    f"Valor inválido: {v} en {color}"
                )
        return tuple(color)

    if isinstance(color, str):
        try:
            r, g, b, _ = mcolors.to_rgba(color)
            return (int(r * 255), int(g * 255), int(b * 255))
        except ValueError:
            raise ValueError(
                f"Color no reconocido: '{color}'. "
                f"Usa un nombre de matplotlib, hex '#RRGGBB' o tupla (R,G,B)."
            )

    raise ValueError(
        f"Tipo de color no soportado: {type(color)}. "
        f"Usa str (nombre o hex) o tupla (R,G,B)."
    )


def matriz_a_imagen(
    matriz: np.ndarray,
    color_letra,
    color_fondo,
) -> Image.Image:
    """
    Convierte una matriz binaria en una imagen PIL RGB.
    Los píxeles con valor 1 toman color_letra; los 0, color_fondo.
    """
    rgb_letra = _color_a_rgb(color_letra)
    rgb_fondo = _color_a_rgb(color_fondo)

    alto, ancho = matriz.shape
    lienzo = np.full((alto, ancho, 3), rgb_fondo, dtype=np.uint8)
    lienzo[matriz == 1] = rgb_letra
    return Image.fromarray(lienzo, mode="RGB")


def guardar_imagen(
    texto: str,
    ruta: str,
    color_letra=(0, 0, 0),
    color_fondo=(255, 255, 255),
    espacio_letras: int = 1,
    espacio_palabras: int = 3,
    margen_sup: int = 2,
    margen_inf: int = 2,
    margen_izq: int = 2,
    margen_der: int = 2,
    escala: int = 1,
) -> None:
    """
    Pipeline completo: texto → matriz → escala → color → guardado.

    Parámetros
    ----------
    texto         : texto a renderizar
    ruta          : ruta del archivo de salida (ej. 'outputs/hola.png')
    color_letra   : color de los píxeles encendidos
    color_fondo   : color del fondo
    espacio_letras: píxeles entre letras
    espacio_palabras: píxeles extra entre palabras
    margen_*      : margen en píxeles (antes de escalar)
    escala        : factor de agrandamiento (nearest-neighbor)
    """
    os.makedirs(os.path.dirname(ruta) if os.path.dirname(ruta) else ".", exist_ok=True)
    mat = texto_a_matriz(
        texto,
        espacio_letras=espacio_letras,
        espacio_palabras=espacio_palabras,
        margen_sup=margen_sup,
        margen_inf=margen_inf,
        margen_izq=margen_izq,
        margen_der=margen_der,
    )
    mat_esc = escalar_matriz(mat, factor=escala)
    img = matriz_a_imagen(mat_esc, color_letra, color_fondo)
    img.save(ruta)
    print(f"Imagen guardada → {ruta}  ({img.size[0]}×{img.size[1]} px)")
