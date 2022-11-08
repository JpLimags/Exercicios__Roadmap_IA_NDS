salario = float(input("Digite o valor do salário: "))
aumento = int(input("Digite a porcetagem do aumento: "))

novo_salario = salario + (salario * aumento/100)

print(f"O valor do aumento foi de R${novo_salario - salario}")
print(f"O novo salário foi de {novo_salario}")