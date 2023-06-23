# TrabalhoIntroPython
Trabalho sobre Python e Github da disciplina de Introdução à Ciência da Computação.

## GRAYSCALE
Primeiramente, são importadas as bibliotecas cv2 (OpenCV), numpy (“np”), matplotlib.pyplot (“ptl”) e a cv2_imshow, oriunda do google.colab.patches. Segundamente, foi utilizado o código cv2.imread(), que tem a função de ler a imagem e armazená-la em uma variável (“img”). Posteriormente, a função `cv2_imshow(img)` permite que a imagem seja exibida no ambiente Colab. Já o código comentado possui uma função que permite exibir uma imagem na tela por meio de uma janela, mas agora possibilitando dar nome a janela. O `cv2.waitKey(0)` exibido tem a função de esperar o usuário pressionar qualquer tecla e, após a execução desse código, a função `cv2.destroyAllWindows()` é acionada. Ela é usada apenas para fechar de forma eficiente todas as janelas abertas pelo `cv2.imshow()`. Com a função `cv2.split(img)`, a imagem colorida é dividida em 3 canais de cores (RGB). Em seguida é feita a conversão das cores em tons de cinza (por ponderação padrão), representando a luminosidade da imagem. O trecho de código seguinte é o de conversão da matriz img_grayscale_pondered em um tipo de dado ‘np.uint8’. O código relacionado ao Grayscale termina com `cv2_imshow(img_grayscale_pondered)`, que permite que a imagem em escala de cinza seja exibida no Google Colab.

## TRANSFORMAÇÕES

### Negativo
A primeira parte desse código, que está comentado, calcula o valor negativo dos canais de cores azul, vermelho e verde. Em seguida, a variável “colorida” recebe o valor 1, que servirá de parâmetro no trecho de código seguinte para definir a escala de cores da imagem. Assim, img_in recebe o valor da imagem original (em cores). Em seguida, em `img_out = 255 - img_in`, é realizada a inversão de cores subtraindo o valor de cada pixel por 255. Por fim, é exibida a imagem colorida através da função `cv2_imshow(img_in)` e com alterações através da função `cv2_imshow(img_out)`.

### Contraste e brilho 
Iniciando o código, é carregado a imagem em escala de cinza. Posteriormente, são definidos os valores das variáveis ‘a’ e ‘b’, que servirão de parâmetro para controlar o contraste. Em seguida, é realizado o ajuste de contraste da imagem, fazendo com que cada pixel seja multiplicado por “a” e somado com “b”, e convertendo a imagem resultante para o tipo de dado ‘np.uint8’. Por fim, é exibida a imagem original e a imagem alterada logo seguida.


## FILTRO ESPACIAL

### Suavização
Primeiramente, é carregada uma imagem definida dentro do código em escalas de cinza. Logo em seguida é criada uma “kernel”, que é uma matriz especial para ser usada na operação de suavização da imagem. Posteriormente, é aplicada a suavização de imagem com a mesma profundidade de bits que a de entrada. Por fim, é exibida a imagem antes da suavização e depois de ter recebido a operação de suavização de imagem.
