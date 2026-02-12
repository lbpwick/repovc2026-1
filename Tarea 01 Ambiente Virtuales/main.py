"""
Demostración integrada de:
- Análisis de datos con NumPy y Pandas
- Visualización con Matplotlib
- Procesamiento de imágenes con OpenCV y Pillow

Requisitos:
    pip install numpy pandas matplotlib opencv-python pillow
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageFilter

# ==========================
# 1. ANÁLISIS DE DATOS
# ==========================
def demo_numpy_pandas():
    print("=== DEMO NUMPY + PANDAS ===")

    # Crear un array NumPy con datos simulados
    np.random.seed(42)
    edades = np.random.randint(18, 60, size=10)        # enteros 18–59
    salarios = np.random.randint(1_000_000, 5_000_000, size=10)  # salarios en pesos
    deptos = np.random.choice(["Sistemas", "Finanzas", "RRHH"], size=10)

    # Estadísticas básicas con NumPy
    print("Edades:", edades)
    print("Edad media:", np.mean(edades))
    print("Salario medio:", np.mean(salarios))

    # Crear DataFrame con Pandas
    data = pd.DataFrame({
        "edad": edades,
        "salario": salarios,
        "departamento": deptos
    })

    print("\nDataFrame completo:")
    print(data)

    # Operaciones típicas de Pandas
    print("\nSalario medio por departamento:")
    print(data.groupby("departamento")["salario"].mean())

    print("\nFiltrar empleados con salario > 3 millones:")
    print(data[data["salario"] > 3_000_000])


# ==========================
# 2. VISUALIZACIÓN CON MATPLOTLIB
# ==========================
def demo_matplotlib():
    print("\n=== DEMO MATPLOTLIB ===")

    # Datos de ejemplo
    x = np.linspace(0, 2 * np.pi, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # Figura con dos subplots
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    ax[0].plot(x, y_sin, color="blue", label="sin(x)")
    ax[0].set_title("Función seno")
    ax[0].set_xlabel("x")
    ax[0].set_ylabel("sin(x)")
    ax[0].legend()
    ax[0].grid(True)

    ax[1].plot(x, y_cos, color="red", label="cos(x)")
    ax[1].set_title("Función coseno")
    ax[1].set_xlabel("x")
    ax[1].set_ylabel("cos(x)")
    ax[1].legend()
    ax[1].grid(True)

    plt.tight_layout()
    plt.show()


# ==========================
# 3. PROCESAMIENTO DE IMÁGENES
#    OpenCV + Pillow
# ==========================
def crear_imagen_sintetica(path="imagen_demo.png"):
    """
    Crea una imagen sintética simple (gradiente + círculo)
    y la guarda en disco para usarla tanto con OpenCV como con Pillow.
    """
    # Crear una imagen RGB 256x256 como array NumPy
    h, w = 256, 256
    img = np.zeros((h, w, 3), dtype=np.uint8)

    # Gradiente en el canal rojo y verde
    for i in range(h):
        for j in range(w):
            img[i, j, 0] = i       # rojo
            img[i, j, 1] = j       # verde
            img[i, j, 2] = 128     # azul constante

    # Dibujar un círculo usando OpenCV
    centro = (w // 2, h // 2)
    radio = 60
    cv2.circle(img, centro, radio, (255, 255, 255), thickness=3)

    cv2.imwrite(path, img)
    print(f"Imagen sintética guardada en: {path}")
    return path


def demo_opencv(path="imagen_demo.png"):
    print("\n=== DEMO OPENCV ===")
    # Leer imagen (BGR)
    img_bgr = cv2.imread(path)
    if img_bgr is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {path}")

    print("Dimensiones de la imagen (alto, ancho, canales):", img_bgr.shape)

    # Convertir a escala de grises
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque gaussiano
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)

    # Mostrar usando Matplotlib (convertir BGR -> RGB)
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax[0].imshow(img_rgb)
    ax[0].set_title("Color (OpenCV)")
    ax[0].axis("off")

    ax[1].imshow(img_gray, cmap="gray")
    ax[1].set_title("Grises")
    ax[1].axis("off")

    ax[2].imshow(img_blur, cmap="gray")
    ax[2].set_title("Desenfoque Gaussiano")
    ax[2].axis("off")

    plt.tight_layout()
    plt.show()


def demo_pillow(path="imagen_demo.png"):
    print("\n=== DEMO PILLOW ===")
    # Abrir imagen con Pillow
    img = Image.open(path)
    print("Tamaño (ancho, alto):", img.size)
    print("Modo:", img.mode)

    # Convertir a blanco y negro
    img_bw = img.convert("L")

    # Aplicar filtro de borde
    img_edges = img_bw.filter(ImageFilter.FIND_EDGES)

    # Mostrar imágenes
    fig, ax = plt.subplots(1, 3, figsize=(12, 4))
    ax[0].imshow(img)
    ax[0].set_title("Original (Pillow)")
    ax[0].axis("off")

    ax[1].imshow(img_bw, cmap="gray")
    ax[1].set_title("Blanco y negro")
    ax[1].axis("off")

    ax[2].imshow(img_edges, cmap="gray")
    ax[2].set_title("Detección de bordes")
    ax[2].axis("off")

    plt.tight_layout()
    plt.show()


# ==========================
# MAIN
# ==========================
if __name__ == "__main__":
    # 1) NumPy + Pandas
    demo_numpy_pandas()

    # 2) Visualización con Matplotlib
    demo_matplotlib()

    # 3) Procesamiento de imágenes (OpenCV + Pillow)
    ruta_imagen = crear_imagen_sintetica()
    demo_opencv(ruta_imagen)
    demo_pillow(ruta_imagen)
