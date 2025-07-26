#  Comparador de Seguidores de Instagram

Este proyecto en Python te permite comparar las cuentas que **sigues** en Instagram con las que **te siguen**, y te muestra cuáles **no te siguen de vuelta**.

---

##  ¿Cómo funciona?

1. Descarga tus datos desde Instagram (en formato HTML):
   - `following.html` → lista de cuentas que sigues.
   - `followers_1.html` → lista de tus seguidores.

2. El script analiza ambos archivos y genera una lista con las cuentas que **no te siguen**.

3. Además, guarda el resultado en un archivo llamado: `no_me_siguen.txt`.

---

##  Cómo usarlo

1. Asegúrate de tener **Python 3** instalado.
2. Instala la biblioteca **BeautifulSoup**:

```bash

pip install beautifulsoup4
Coloca los archivos following.html y followers_1.html en la misma carpeta que el script.

Ejecuta el script en la terminal:
python comparador.py

 Requisitos
Python 3.x

beautifulsoup4

 Resultado
Verás en la terminal la lista de cuentas que sigues pero no te siguen.
También se guardará esa lista en el archivo: no_me_siguen.txt

Privacidad
Este programa no accede a tu cuenta de Instagram.
Solo analiza archivos exportados por ti desde la plataforma.

 Autor
Pergondev