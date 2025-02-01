# Esse programa realiza a implementação em Python para transformar uma 
# imagem colorida para níveis de cinza (0 a 255) e para binarizada (0 e 255), preto e branco.

# Data: 25/01/2025
# Programador: Vinícius Werneck

# Etapa 1: carregar a imagem
from PIL import Image

# Caminho da imagem
path = r"C:\Users\Werneck\OneDrive\Documentos\Cursos\Projeto Baires-ML-DIO\Lena.png"

# Abrindo a imagem
img = Image.open(path)
# Exibindo a imagem
img.show()

def converter_para_cinza(imagem):
    #Verifica o modo da imagem (RBG ou outro)
    if imagem.mode != 'RGB':
        imagem = imagem.convert('RGB')

    largura, altura =imagem.size
    imagem_cinza = Image.new("L", (largura, altura))  #Escala de cinza

    for y in range(altura):
        for x in range (largura):
            r,g,b = imagem.getpixel((x,y))
            valor_cinza = int(0.299*r+0.587*g+0.114*b)
            imagem_cinza.putpixel((x,y), valor_cinza)

    return imagem_cinza

# Converter a imagem para cinza
imagem_cinza = converter_para_cinza(img)
imagem_cinza.show()

def binarizar_imagem(imagem_cinza, limiar=127):
    largura, altura = imagem_cinza.size
    imagem_binaria = Image.new ("1", (largura, altura)) #Binária

    for y in range(altura):
        for x in range (largura):
            valor_cinza = imagem_cinza.getpixel((x,y))
            valor_binario = 1 if valor_cinza > limiar else 0
            imagem_binaria.putpixel((x,y), valor_binario)
    
    return imagem_binaria

# Converter a imagem para preto e branco
imagem_binaria = binarizar_imagem(imagem_cinza)
imagem_binaria.show()
