from PIL import Image


if __name__ == "__main__":
    try:
        image = Image.open('img/jojo.jpg')
        width, height = image.size
        new_width = width//2
        new_height = height//2
        print(f'Ancho: {width}')
        print(f'Alto: {height}')
        print(f'Nuevo Ancho: {new_width}')
        print(f'Nuevo Alto: {new_height}')
        new_image = image.resize((new_width,new_height))
        image.show()
        new_image.show()
    except FileNotFoundError as error:
        print("No es posible encontrar la imagen")