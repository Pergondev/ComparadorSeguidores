from bs4 import BeautifulSoup

def cargar_cuentas_desde_html(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        sopa = BeautifulSoup(contenido, "html.parser")
        enlaces = sopa.find_all("a")
        cuentas = [enlace.text.strip() for enlace in enlaces if enlace.text.strip()]
        return cuentas

def comparar_listas(lista_seguidos, lista_seguidores):
    cuentas_no_me_siguen = [cuenta for cuenta in lista_seguidos if cuenta not in lista_seguidores]
    return cuentas_no_me_siguen

def main():
    archivo_seguidos = "following.html"
    archivo_seguidores = "followers_1.html"

    print(" Cargando archivos...")
    lista_seguidos = cargar_cuentas_desde_html(archivo_seguidos)
    lista_seguidores = cargar_cuentas_desde_html(archivo_seguidores)

    print(f" Seguidos: {len(lista_seguidos)} cuentas")
    print(f" Seguidores: {len(lista_seguidores)} cuentas")

    cuentas_que_no_me_siguen = comparar_listas(lista_seguidos, lista_seguidores)

    print("\n Cuentas que sigues y no te siguen:")
    for cuenta in cuentas_que_no_me_siguen:
        print(f" {cuenta}")

    # (Opcional) Guardar resultados en un archivo
    with open("no_me_siguen.txt", "w", encoding="utf-8") as salida:
        for cuenta in cuentas_que_no_me_siguen:
            salida.write(f"{cuenta}\n")

    print("\n Resultado guardado en 'no_me_siguen.txt'")

if __name__ == "__main__":
    main()
