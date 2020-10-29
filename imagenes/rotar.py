from PIL import Image


if __name__ == "__main__":
    try:
        image = Image.open('img/jojo.jpg')
        new_image= image.rotate(180,expand=True)
        #new_image= image.transpose(Image.ROTATE_90)
        new_image.show()
    except FileNotFoundError as error:
        print("No es posible encontrar la imagen")