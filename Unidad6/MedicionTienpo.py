import time
from reader import feed

def main():
    """Imprime el último tutorial de Python"""
    tic = time.perf_counter()
    tutorial = feed.get_article(0)
    toc = time.perf_counter()
    print(f"El tutorial ha sido descargado en {toc - tic:0.4f} segundos")

    print(tutorial)

if __name__ == "__main__":
    main()