from PIL import Image


if __name__ == "__main__":
    try:
        panel = Image.open('img/oso.jpeg')
        letras = Image.open('img/kanjis.png')
        gorro = Image.open('img/gorro.png')
        gorro_width, gorro_height = gorro.size
        #paste
        gorro = gorro.resize((gorro_width//3,gorro_height//3))
        panel.paste(
            gorro,
            (200,190),
            mask = gorro
        )
        panel.show()

        panel.paste(
            letras,
            (250,50),
            mask = letras
        )
        panel.show()
        
        #panel.save('img/oso_jojo.jpg')
    except FileNotFoundError as error:
        print("No es posible encontrar la imagen")