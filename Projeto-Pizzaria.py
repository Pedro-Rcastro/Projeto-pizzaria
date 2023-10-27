
print('Bem-vindo a pizzaria do Pedro Rogério')
print('-------------------CARDÁPIO----------------------')
print('CÓDIGO|DESCRIÇÃO |PIZZA MÉDIA(M)|PIZZA GRANDE(G)|')
print('    21|Napolitana|       R$20,00|        R$26,00|')
print('    22|Magaherita|       R$20,00|        R$26,00|')
print('    23|Calabresa |       R$25,00|        R$32,50|')
print('    24|Toscana   |       R$30,00|        R$39,00|')
print('    25|Portuguesa|       R$30,00|        R$39,00|')
print('-------------------------------------------------')
acumulador = 0
while True:
  tamanho = input('Entre com o tamanho de pizza desejada(M/G):')
  tamanho = tamanho.upper()
  if tamanho != 'M'and tamanho != 'm'and tamanho != 'G'and tamanho != 'g':
    print('Opção Inválida. Pare de digitar tamanhos que não existem!')
    continue# Se usuário digitar algo errado voltar para o começo do while

  codigo = input('Entre com o codigo de pizza desejado(21/22/23/24/25):')
  if codigo != '21'and codigo != '22'and codigo != '23'and codigo != '24'and codigo != '25':
    print('Opção Inválida. Pare de digitar codigos que não existem!')
    continue# Se usuário digitar algo errado voltar para o começo do while

  if codigo == '21' and tamanho == 'M':
    print('Você escolheu a pizza napolitana tamanho M')
    acumulador = acumulador + 20# Pague o valor que tinha no acumulador e some com 20

  if codigo == '21' and tamanho == 'G':
    print('Você escolheu a pizza napolitana tamanho G')
    acumulador = acumulador + 26# Pague o valor que tinha no acumulador e some com 26

  if codigo == '22' and tamanho == 'M':
    print('Você escolheu a pizza Margherita tamanho M')
    acumulador = acumulador + 20# Pague o valor que tinha no acumulador e some com 20

  if codigo == '22' and tamanho == 'G':
    print('Você escolheu a pizza napolitana tamanho G')
    acumulador = acumulador + 26# Pague o valor que tinha no acumulador e some com 26

  if codigo == '23' and tamanho == 'M':
    print('Você escolheu a pizza Calabresa tamanho M')
    acumulador = acumulador + 25# Pague o valor que tinha no acumulador e some com 25

  if codigo == '23' and tamanho == 'G':
    print('Você escolheu a pizza Calabresa tamanho G')
    acumulador = acumulador + 32,50# Pague o valor que tinha no acumulador e some com 32,50

  if codigo == '24' and tamanho == 'M':
    print('Você escolheu a pizza toscana tamanho M')
    acumulador = acumulador + 30# Pague o valor que tinha no acumulador e some com 30

  if codigo == '24' and tamanho == 'G':
    print('Você escolheu a pizza Toscana tamanho G')
    acumulador = acumulador + 39# Pgue o valor que tinha noacumulador e some com 39

  if codigo == '25' and tamanho == 'M':
    print('Você escolheu a pizza Portuguesa tamanho M')
    acumulador = acumulador + 30# Pgue o valor que tinha noacumulador e some com 30

  if codigo == '25' and tamanho == 'G':
    print('Você escolheu a pizza napolitana tamanho G')
    acumulador = acumulador + 39# Pgue o valor que tinha noacumulador e some com 39

  pedir_mais =input('Deseja pedir mais alguma pizza(S/Digite outra tecla?:)')
  pedir_mais = pedir_mais.upper()#resolvendo o problema de digitar "m"ou "M"
  if pedir_mais =='S':
    continue
  else:
      print('O valor total a ser é pago:R${:.2f}'.format(acumulador))
      break