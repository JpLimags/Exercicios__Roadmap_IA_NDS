#preenchendo vetor
nums = 0
soma = 0

i = 1
while True:

    
    nums = int(input(f"Digite o {i}º numero (Caso deseje encerrar digite 0 !): "))
    soma +=nums

    if(nums != 0):
        i+=1
    elif(nums == 0):
        break

media = soma/(i-1)
print(f"A média aritmética obtida para n valores, é igual a: {media}")
