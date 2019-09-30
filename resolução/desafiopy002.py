# Criar um programa que utilize o método 50-20-10-20: (PaginaSobreMetodos)
# 1. Leia o salário líquido informado pelo usuário.
# 2. Organize os valores de acordo com o método citado.
# 3. Informe ao usuário qual o valor que ele deve destinar para cada categoria.

print('='*60)

salario_liq = 0
despesas_fixas = 0
investimento_longo = 0
investimento_curto = 0
gastos = 0

print('Digite o valor do sálario líquido:'.format(' '*5 ))
salario_liq = float(input())
    

despesas_fixas = salario_liq * 0.5
print('{} 50% do sálario destinado a despesas fixas: {} R$ {:8.2f}'.format(' '*5,' '*25, despesas_fixas))

investimento_longo = salario_liq * 0.2
print('{} 20% do sálario destinado a investimentos de longo prazo {} R$ {:8.2f}'.format(' '*5,' '*12, investimento_longo))

investimento_curto = salario_liq * 0.1
print('{} 10% do sálario destinado a investimentos de curto prazo {} R$ {:8.2f}'.format(' '*5,' '*12, investimento_curto))

gastos = salario_liq * 0.2
print('{} 20% do sálario destinado a gastos livres e despesas váriaveis: {} R$ {:8.2f}'.format(' '*5,' '*5, gastos))

print('='*60)