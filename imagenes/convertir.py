from PIL import Image


if __name__ == "__main__":
    try:
        #https://pillow.readthedocs.io/en/stable/handbook/concepts.html
        image = Image.open('img/jojo.jpg')
        new_image= image.convert('L')
        new_image.show()
    except FileNotFoundError as error:
        print("No es posible encontrar la imagen")