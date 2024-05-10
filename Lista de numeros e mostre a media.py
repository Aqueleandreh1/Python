'''Crie um programa que leia as temperaturas médias de cada mês do ano e as armazene em uma lista; use outro vetor para guardar e exibir,
quando necessário, o nome dos meses do ano;
calcule a média anual de temperatura e informe quais meses ficaram acima da média anual.'''

temperatura=[]
acima=[]
mes=['jan', 'fev', 'mar', 'abr', 'maio', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for m in mes:
    temp=float(input("Digite a temperatura media do mês de " + m +": "))
    temperatura.append(temp)

media=sum(temperatura)/len(temperatura)
print("\nMédia = ", media)

print(f"\nMeses com temperatura acima da média de {media:.1f} graus:")
for i in range(12):
        if temperatura[i] > media:

            print(f"{mes[i]}: {temperatura[i]:.1f} graus")
