#Conversão de imagem RGB em imagem Grayscale
import cv2                                                              # Importa a bibliotéca do OpenCV (é uma bibliotéca de precessamento de imagens e videos).
import numpy as np                                                      # Importa a bibliotéca do NumPy (uma bibliotéca de computação numérica, com arrays multidimencionais e funções matemáticas de alto desempenho, usada em conjunto com OpenCV).
import matplotlib.pyplot as plt                                         # Importa uma bibliotéca de visualização de dados em python (usado aqui para exibir imagens)
from google.colab.patches import cv2_imshow                             # é uma função do colab que chama a função cv_imshow (que será utilizada para exibir imagens)

img = cv2.imread('t1.jpg',1)                              # Tem como função abrir a imagem com o nome citado e o parametro indica se a imagem ira ser carregada em corres(1), preto e branco(0) ou se mantem a configuração original(-1)
cv2_imshow(img)                                           # Função expecifica do Colab, possibilita mostrar imagens diretamente do notebook/PC

#mostrando a imagem colorida - caso você use Python no seu computador
#reutilize para exibir as imagens em outros códigos
#Voce pode descomentar o código apagando as aspas simples

cv2.imshow('in', img)                                     
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imshow('in', img)    é utilizada para mostrar a imagem e o primeiro parâmetro 'in' é o nome da janela que a imagem irá ser mostrada, pode ser utilizado qualquer palavra como primeiro parâmetro.
#cv2.waitKey(0)           essa função faz o código esperar o usuário pressionar alguma tecla antes de continuar, já o parametro indica que se ele irá esperar indefinidamente com o parâmetro (0) ou (-1) que tem a mesma função
#já com um parâmetro definido por exemplo (500) será definido 500 milissegundos de espera.
#cv2.destroyAllwindows()  é usada apenas para fechar todas as janelas abertas de forma eficiente "todas as janelas abertas pelo cv2.imshow"    

#aplicando conversão ponderada - converte imagem colorida para escalas de cinza
#img_grayscale_basic = 0.299*img[ : , : ,0] + 0.587*img[ : , : ,1] + 0.114*img[ : , : ,2]

#cv2
B, G, R = cv2.split(img)                            # a sua função é dividir a imagem em 3 canais de cores nesse caso B "canal Blue//Azul", G "Green//Verde" e R "Red//Vermelho"
img_grayscale_pondered = 0.299*B+0.587*G+0.114*R    # converge as cores em tons de cinza representando a luminosidade da imagem, a formula ao lado calcula cada cor R, G, B. mostrando a luminosidade baseada na formula e depois é armazenada na variável

img_grayscale_pondered = np.array(img_grayscale_pondered, dtype=np.uint8)    #converte a imagem em escala cinza em dados apropiádos para exibila

cv2_imshow(img_grayscale_pondered)                  # esta função apenas exibe a imagem em escala de cinza ponderada no google colab
