import random

def lanzar_dado(tipo_dado,num_dado,dados_lanzados,cantidad_lanzamientos):
    pos = 0
    print(f'Cantidad de lanzamientos {cantidad_lanzamientos}')
    cantidad_lanzamientos = cantidad_lanzamientos +1
    for i in range(num_dados):
        pos +=1
        print(f'Lanzando dado de {tipo_dado} caras')
        num_cara =int(random.random()*tipo_dado)
        dados_lanzados.append(num_cara)
        print(f'Dado {pos}: {num_cara}')
        if len(dados_lanzados)>1:
            if dados_lanzados[i-1]==dados_lanzados[i] and cantidad_lanzamientos<3:
                lanzar_dado(tipo_dado,num_dado,dados_lanzados, cantidad_lanzamientos)

if __name__ == "__main__":
    tipo_dado = int(input("Ingrese el tipo de dado a lanzar: "))
    num_dados = int(input("Ingrese la cantidad de dados a lanzas: "))
    dados_lanzados = []
    cantidad_lanzamientos = 1
    lanzar_dado(tipo_dado,num_dados,dados_lanzados,cantidad_lanzamientos)

    
