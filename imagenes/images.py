from PIL import Image


if __name__ == "__main__":
    try:
        image = Image.open('img/jojo.jpg')
        print(image.size)
        print(image.mode)
        print(image.format)
        image.show()
    except FileNotFoundError as error:
        print("No es posible encontrar la imagen")