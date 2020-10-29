from PIL import Image


if __name__ == "__main__":
    try:
        image = Image.open('img/jojo.jpg')
        new_image = image.crop(
            (300,0,700,150) #4 int (left<right, upper<lower, right, lower)
        )
        #image.show()
        new_image.save('img/letras.jpg')
        new_image.show()
    except FileNotFoundError as error:
        print("No es posible encontrar la imagen")