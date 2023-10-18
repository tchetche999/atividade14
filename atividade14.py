# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input("insira seu salário:"))
if sal > float("1250.00"):
 print("seu novo salário é", sal+(sal/100))
else:
 print("seu novo salário é", sal+(sal/150))