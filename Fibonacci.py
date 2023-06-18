#Sequência de fibonacci
def fib(n):                           #Declaração da função fib com parâmetro n
  a, b = 0, 1                         #a e b recebem, respectivamente, os valores de 0 e 1
  while a < n:                        #Cria um laço de repetição while que executa as linhas 5 e 6 enquanto a for menor que n
      print(a, end = ' ')             #Imprime o valor de a e usa o parâmetro 'end' para estabelecer um espaço (' ') como último caracter ao invés da quebra de linha (\n)
      a, b = b, a + b                 #a recebe o valor de b, e b recebe o valor da soma entre b e o valor antigo de a.

  
  fib(100)                            #Chamando a função fib, em que o parâmetro n = 100 
  
 
