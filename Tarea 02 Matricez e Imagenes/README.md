# 📘 De texto a imagen

Convierte cadenas de texto en imágenes PNG usando **matrices binarias de píxeles** como representación interna de cada carácter.

## 📂 Estructura del repositorio

```
├── utils.py      # toda la lógica del proyecto
├── demo.ipynb    # notebook de demostración
├── README.md     # esta documentación
└── .gitignore    # excluye imágenes generadas
```

> Las imágenes generadas se guardan en `outputs/` localmente pero **no se suben al repositorio** (ver `.gitignore`).

---

## ⚙️ Configuración del ambiente virtual

## Paso 1: Abrir Anaconda Prompt
**IMPORTANTE**: Usa siempre **Anaconda Prompt** en lugar de la terminal normal de Windows para trabajar con conda.

1. Busca "Anaconda Prompt" en el menú de inicio de Windows
2. Haz clic derecho y selecciona "Ejecutar como administrador" si es necesario
3. Se abrirá una ventana de terminal con el entorno de Anaconda configurado

## Paso 2: Crear el ambiente virtual
En Anaconda Prompt, ejecuta el siguiente comando para crear un ambiente virtual llamado "vision":

```bash
conda create --name vision python=3.9
```

- `--name vision`: Define el nombre del ambiente
- `python=3.9`: Especifica la versión de Python (puedes usar 3.8, 3.10, 3.11 según prefieras)

Cuando te pregunte si proceder, escribe `y` y presiona Enter.

## Paso 3: Activar el ambiente virtual
Una vez creado, activa el ambiente:

```bash
conda activate vision
```

Deberías ver `(vision)` al inicio de la línea de comandos, indicando que el ambiente está activo.

---

## ▶️ Ejecutar el notebook

```bash
jupyter notebook demo.ipynb
```

---

## 🚀 Uso rápido desde Python

```python
from utils import guardar_imagen

# Nombres de color (matplotlib)
guardar_imagen("hola", "outputs/hola.png",
               color_letra="blue", color_fondo="yellow",
               escala=10, margen_sup=2, margen_inf=2,
               margen_izq=2, margen_der=2)

# Tupla RGB
guardar_imagen("hola", "outputs/hola_rgb.png",
               color_letra=(0, 0, 0), color_fondo=(255, 255, 255),
               escala=10)

# Hex #RRGGBB
guardar_imagen("hola", "outputs/hola_hex.png",
               color_letra="#1E90FF", color_fondo="#F5F5F5",
               escala=10)
```

---

## 🎨 Formatos de color soportados

| Formato | Ejemplo | Descripción |
|---------|---------|-------------|
| Nombre matplotlib | `"blue"`, `"yellow"` | Cualquier nombre de `matplotlib.colors` |
| Tupla RGB | `(0, 0, 0)`, `(255, 255, 255)` | Enteros 0–255 por canal |
| Hex `#RRGGBB` | `"#1E90FF"`, `"#F5F5F5"` | Notación hexadecimal estándar |

---

## 🔧 Funciones principales en `utils.py`

| Función | Descripción |
|---------|-------------|
| `normalizar_texto(texto)` | Convierte el texto a caracteres soportados; reemplaza no soportados por `?` |
| `texto_a_matriz(texto, ...)` | Concatena matrices de letras con espaciado y márgenes |
| `escalar_matriz(matriz, factor)` | Escala la imagen ×N con nearest-neighbor (`np.kron`) |
| `matriz_a_imagen(matriz, color_letra, color_fondo)` | Convierte la matriz binaria en imagen PIL RGB |
| `guardar_imagen(texto, ruta, ...)` | Pipeline completo: texto → matriz → escala → color → PNG |

---

## 🔡 Decisiones de diseño

### Tamaño de matrices
- Todas las letras tienen **7 filas** de alto.
- El **ancho varía** por carácter para que cada letra tenga proporciones naturales:
  - `i`, `l` → 2–3 columnas
  - `m`, `w` → 5 columnas
  - Resto → 3–4 columnas

### Acentos y caracteres especiales
Se usa un diccionario de equivalencias dentro de `normalizar_texto`:

```python
equivalencias = {
    "á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u",
    "Á":"A", "É":"E", "Í":"I", "Ó":"O", "Ú":"U",
    "ñ":"n", "Ñ":"N",
}
```

Los caracteres sin equivalencia se reemplazan por `?`.  
Para soporte completo de `ñ` o vocales con tilde, basta agregar su propia matriz en `ALFABETO`.

### Escalado
Se utiliza `np.kron(matriz, np.ones((N, N)))` que replica cada píxel en un bloque N×N, equivalente a interpolación nearest-neighbor sin dependencias externas.

---

## 📑 `.gitignore`

Las imágenes generadas (`*.png`, `*.jpg`, etc.) y la carpeta `outputs/` están excluidas del repositorio para no versionar archivos binarios generados automáticamente.

---

## Uso de Inteligencia Artificial

En el desarrollo de este proyecto se utilizó un asistente de IA (Perplexity) como apoyo para:
- Generar borradores de las matrices del alfabeto.
- Estructurar el módulo `utils.py`

Todo el código y la documentación fueron revisados, adaptados y validados manualmente para ajustarse a los requisitos de la tarea.
