print("""Calculadora - Escolha um dos operadores matemáticos para calcular:

1 para Soma
2 para Subtração
3 para Multiplicação
4 para Divisão
""")

operacao_soma = 1
operacao_subt = 2
operacao_mult = 3
operacao_divs = 4

operacao_escolhida = int(input("Digite a opção desejada: "))

if(operacao_escolhida == 1):
  operacao = "Soma"
  print(f"{operacao:=^20}".upper())
  n1_soma = int(input("Digite o primeiro número:"))
  n2_soma = int(input("Digite o segundo número:"))
  soma = n1_soma + n2_soma
  print("O resultado da soma entre {} e {} é igual a: {} ".format(n1_soma, n2_soma, soma))
  fim = "fim"
  print(f"{fim:=^20}".upper())

elif(operacao_escolhida == 2):
  operacao = "Subtração"
  print(f"{operacao:=^20}".upper())
  n1_sub = int(input("Digite o primeiro número:"))
  n2_sub = int(input("Digite o segundo número:"))
  subtracao = n1_sub - n2_sub
  print("O resultado da subtração entre {} e {} é igual a: {} ".format(n1_sub, n2_sub, subtracao))
  fim = "fim"
  print(f"{fim:=^20}".upper())

elif(operacao_escolhida == 3):
  operacao = "Multiplicação"
  print(f"{operacao:=^20}".upper())
  n1_mult = int(input("Digite o primeiro número:"))
  n2_mult = int(input("Digite o segundo número:"))
  multiplicacao = n1_mult * n2_mult
  print("O resultado da multiplicação entre {} e {} é igual a: {} ".format(n1_mult, n2_mult, multiplicacao))
  fim = "fim"
  print(f"{fim:=^20}".upper())

elif(operacao_escolhida == 4):
  operacao = "Divisão"
  print(f"{operacao:=^20}".upper())
  n1_div = int(input("Digite o primeiro número:"))
  n2_div = int(input("Digite o segundo número:"))
  divisao = n1_div / n2_div
  print("O resultado da divisão entre {} e {} é igual a: {} ".format(n1_div, n2_div, divisao))
  fim = "fim"
  print(f"{fim:=^20}".upper())

else:
  print("""
  Você deve escolher uma das operações:
  1 para Soma (+)
  2 para Subtração (-)
  3 para Multiplicação (*)
  4 para Divisão (/)""")
