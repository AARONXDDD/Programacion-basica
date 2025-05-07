from reader import feed

def main():
    """Descarga e imprime el último tutorial de python"""
    tutorial = feed.get_article(0)
    print(tutorial)

if __name__ == "__main__":
    main()