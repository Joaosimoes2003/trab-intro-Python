**#Conversão de imagem RGB em imagem Grayscale**
import cv2 # Importa a bibliotéca do OpenCV (é uma bibliotéca de precessamento de imagens e videos)
import numpy as np # Importa a bibliotéca do NumPy (uma bibliotéca de computação numérica, com arrays multidimencionais e funções matemáticas de alto desempenho, usada em conjunto com OpenCV)
import matplotlib.pyplot as plt # Importa uma bibliotéca de visualização de dados em python (usado aqui para exibir imagens)
#caso for usar o Google Colab com a OpenCV, usar a lib abaixo
from google.colab.patches import cv2_imshow # é uma função do colab que chama a função cv_imshow (que será utilizada para exibir imagens)

#abrir a imagem
img = cv2.imread('praia.jpg',0) # Tem como função abrir a imagem com o nome citado e o parametro indica se a imagem ira ser carregada em corres(1), preto e branco(0) ou se mantem a configuração original(-1)
#caso for usar o Google Colab com a OpenCV,
cv2_imshow(img) # Função expecifica do Colab, possibilita mostrar imagens diretamente do notebook/PC

#mostrando a imagem colorida - caso você use Python no seu computador
#reutilize para exibir as imagens em outros códigos
#Voce pode descomentar o código apagando as aspas simples

cv2.imshow('in', img) # É utilizada para mostrar a imagem e o primeiro parâmetro 'in' é o nome da janela que a imagem irá ser mostrada, pode ser utilizado qualquer palavra como primeiro parâmetro
cv2.waitKey(0) # Faz o código esperar o usuário pressionar alguma tecla antes de continuar. O parâmetro (0) ou (-1) indica que se ele irá esperar indefinidamente. Para um parâmetro definido, é determinado em milisseguntos Ex.: (500) = 500 milissegundos de espera
cv2.destroyAllWindows() # É usada apenas para fechar de forma eficiente todas as janelas abertas abertas pelo cv2.imshow

#aplicando conversão ponderada - converte imagem colorida para preto e branco
#img_grayscale_basic = 0.299*img[ : , : ,0] + 0.587*img[ : , : ,1] + 0.114*img[ : , : ,2]

#cv2
B, G, R = cv2.split(img) # A sua função é dividir a imagem em 3 canais de cores nesse caso B "canal Blue/Azul", G "Green/Verde" e R "Red/Vermelho"
img_grayscale_pondered = 0.299*B+0.587*G+0.114*R # Converte as cores em tons de cinza representando a luminosidade da imagem. Após “=” há uma fórmula que calcula cada cor dos canais R, G e B, armazenando na variável a luminosidade baseada na fórmula
img_grayscale_pondered = np.array(img_grayscale_pondered, dtype=np.uint8) # Converte a imagem em escala cinza em dados apropiados para exibí-la
cv2_imshow(img_grayscale_pondered) # Esta função apenas exibe a imagem em escala de cinza ponderada no Google Colab

#tranformações
#negativo

#img_negative[ : , : ,0] = 255 - img[ : , : ,0]
#img_negative[ : , : ,1] = 255 - img[ : , : ,1]      calcula o valor negativo dos canais de cores azul,vermelho e verde
#img_negative[ : , : ,2] = 255 - img[ : , : ,2]

colorida = 1   # pode ser escolhido entre escala de cinza (0) e colorido (1) a variável colorida pode ser mudada de acordo com a necessidade 

img_in = cv2.imread('t1.jpg',colorida)    # esta variável armazena a imagem original carregada

img_out = 255 - img_in  # realiza a inversão de cores (subtraindo o valor de cada pixel por 255 obtendo assim o valor invertido)

cv2_imshow(img_in)   # exibe a imagem original carregada
cv2_imshow(img_out)  # exibe a imagem invertida   

#contraste e brilho
img_in = cv2.imread('t1.jpg',0)  # carrega a imagem em escala cinza como especificado pelo parâmetro (0)

a = -1       # tanto “a” quanto “b” podem ser qualquer número
b = 1       # os números de “a” e de “b” representam parâmetros que controlam o contraste da imagem

img_out = a*img_in + b # realiza o ajuste de contraste da imagem fazendo com que cada pixel seja multiplicado por “a” e somado com “b”


img_out = np.array(img_out, dtype = np.uint8) # converte a imagem resultante para o tipo de dado ‘np.uint8’ representado por valores inteiros sem sinal de 8 bits

cv2_imshow(img_in)   # é exibida a imagem original.
cv2_imshow(img_out)  # é exibida a imagem com ajuste de contraste.

#suavização
img_in = cv2.imread('t1.jpg',0) # Carrega uma imagem e como o parâmetro é de (0) ela é carregada em escala de cinza

kernel = np.ones((5,5),np.float32)/25 # Criar um kernel que é uma matriz especial para ser usada na operação de suavização da imagem


img_out_1 = cv2.filter2D(img_in,-1,kernel) # aplica a operação de suavização de imagem de entrada usando o kernel definido na linha de cima o parâmetro nesse caso que a saída
 # terá a mesma profundidade de bits da imagem de entrada (-1) agora se o parâmetro fosse de (0) a  imagem de saída teria a profundidade de 8 bits por pixel (float) e se fosse (1)
 # a imagem de saída teria a profundidade de 32 bits por pixel.

cv2_imshow(img_in)   #exibe a imagem original (no caso antes da suavização)
cv2_imshow(img_out_1)  # é usada para exibir a imagem após o efeito de suavização.
