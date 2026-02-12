[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/oiBnaWzg)
# Introducción a ambientes virtuales con Conda

## Autor
Luis Fernando Borrero Perales - 11/02/2026

## Descripción
Este repositorio contiene una tarea práctica para aprender a crear y gestionar ambientes virtuales en Conda. Los estudiantes aprenderán a configurar un entorno de desarrollo aislado, instalar paquetes específicos y crear código Python funcional.

## Contenido del repositorio
- `Instrucciones.md` - Guía paso a paso para crear y usar ambientes virtuales
- `requirements.txt` - Lista de paquetes Python necesarios
- `main.py` - Archivo Python de ejemplo
- `ejercicio.ipynb` - Cuaderno Jupyter de ejemplo
- `.gitignore` - Archivo para ignorar archivos innecesarios en Git
- `README.md` - Este archivo de documentación

## Cómo usar el código

### 1. Configurar el ambiente virtual
Sigue las instrucciones detalladas en `Instrucciones.md` para:
- Crear el ambiente virtual "vision"
- Instalar los paquetes requeridos
- Activar el ambiente

### 2. Ejecutar el código de ejemplo
Una vez configurado el ambiente:

```bash
# Ejecutar el archivo Python
python main.py

# Ejecutar Jupyter Notebook
jupyter notebook
```

### 3. Explorar y modificar
- Abre `ejercicio.ipynb` en Jupyter para experimentar con el código
- Modifica `main.py` para agregar nuevas funcionalidades
- Agrega nuevos paquetes al `requirements.txt` según tus necesidades

## Funcionalidades del código
- **Análisis de datos**: Uso de NumPy y Pandas para manipulación de datos
- **Visualización**: Gráficos con Matplotlib
- **Procesamiento de imágenes**: Funcionalidades básicas con OpenCV y Pillow
- **Notebooks interactivos**: Desarrollo y experimentación con Jupyter

## Nivel de uso de herramientas de inteligencia artificial

- **Medio**: Uso moderado de herramientas de IA para asistencia en el desarrollo.


### Herramientas utilizadas (si aplica)
En el desarrollo de este trabajo se utilizó un asistente de IA (Perplexity, powered by GPT‑5.1) como apoyo para tareas específicas de documentación y ejemplo de código.

#### Prompts utilizados:
```
Eres un ingeniero de software con doctorado de Python con amplios conocimientos en Análisis de datos y Procesamiento de imágenes.
```

**Generación de código:**
```
Prompt: "Crea un archivo Python que demuestre el uso de:
Análisis de datos: Uso de NumPy y Pandas para manipulación de datos.
Visualización: Gráficos con Matplotlib.
Procesamiento de imágenes: Funcionalidades básicas con OpenCV y Pillow."
```
## ¿Para qué se utilizó la IA?
- **La IA se utilizó principalmente para:**

   - Proponer estructuras y ejemplos de: Script de demostración con NumPy, Pandas, Matplotlib, OpenCV y Pillow.
   - Redactar y mejorar secciones explicativas del **README.md**



## Archivo `.gitignore` en este proyecto

### ¿Qué es un archivo `.gitignore`?

Un archivo `.gitignore` es un archivo de texto que le indica a Git qué archivos y carpetas debe **ignorar** dentro de un repositorio. [web:66][web:69]  
Es decir, aunque existan en tu directorio de trabajo, Git no los tendrá en cuenta cuando hagas `git status`, `git add` o `git commit`. [web:67][web:76]

### ¿Para qué sirve?

Sirve para excluir del control de versiones archivos que no aportan valor al código fuente, por ejemplo: [web:68][web:70]

- Archivos temporales generados por el sistema operativo (`.DS_Store`, `Thumbs.db`). [web:68]  
- Archivos de compilación o build (`build/`, `dist/`). [web:68]  
- Entornos virtuales (`venv/`, `.env/`). [web:71][web:77]  
- Archivos de configuración local de editores (`.vscode/`, `.idea/`). [web:70][web:71]  

Esto mantiene el repositorio más limpio y enfocado solo en los archivos relevantes del proyecto. [web:70][web:72]

### ¿Cómo funciona?

El archivo `.gitignore` funciona mediante **patrones de texto**, uno por línea, que le dicen a Git qué rutas debe excluir. [web:68][web:76]

Algunas reglas básicas:

- `nombre_archivo.ext` ignora un archivo concreto.  
- `carpeta/` ignora todo el contenido de una carpeta.  
- `*.log` ignora todos los archivos con extensión `.log`. [web:68]  
- El signo de exclamación `!` sirve para “des‑ignorar” algo que antes estaba ignorado. [web:68]  

Ejemplos:

```gitignore
# Ignora todos los archivos .log
*.log

# Ignora la carpeta del entorno virtual
venv/

# Ignora todos los .txt excepto README.txt
*.txt
!README.txt

