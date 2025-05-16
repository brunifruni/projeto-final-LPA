print('BEM-VINDO A STORE!')

valorunit = float(input('Digite o valor unitário do produto: R$ '))
qtd = int(input('Quantidade do produto: '))

#calculo do valor total sem desconto
valortot = valorunit * qtd

#definição do desconto com base no valor total 
if valortot < 2500:
    desc = 0
elif valortot >=2500 and valortot < 6000:
    desc = 4
elif valortot >= 6000 and valortot < 10000:
    desc = 7
else:
    desc = 11

#calculo do valor do desconto
valordesc = (valortot * desc) / 100
#calculo do total com o desconto
totalcomdesc = valortot - valordesc

print(f'\nResumo da compra:')
print(f'Valor da compra sem desconto: R$ {valortot}')
print(f'Desconto aplicado: {desc}% (R${valordesc})')
print(f'Valor total com desconto: R$ {totalcomdesc}')
