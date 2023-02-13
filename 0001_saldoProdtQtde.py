'''-------------------------------------------------------------
FATEC - SCS
Curso de CST em Segurança da Informação
1° Semestre - Aula de Programação I
Professor: Vinicius Heltai
Aluno: Rafael Sena
Data: 11/02/2023
Enunciado:Um produto custa R$ 1.50. O cliente tem R$ 10.00.
Quantos produtos esse cliente pode comprar?
----------------------------------------------------------------'''

# declarações de variáveis
saldo = float(input('Quanto você pode gastar?\nR$ '))
valorProduto = float(input('Quanto custa o produto?\nR$ '))
qtde = 0

# processamento
while (saldo >= valorProduto):
    qtde += 1
    saldo = saldo - valorProduto

# saída do resultado
print(qtde)
