print("\nBEM VINDO A COPIADORA")
print('\nDigite o serviço desejado: ')
print('DIG - Digitalização')
print('ICO -Impressão Colorida')
print('IPB - Impressão Petro e Branco')
print('FOT - Fotocópia')

#escolhaserviço
def escolha_servico():
    while True:
        servico = input(">> ").upper()
        if servico == "DIG":
            return 1.10
        elif servico == "ICO":
            return 1.00
        elif servico == "IPB":
            return 0.40
        elif servico == "FOT":
            return 0.20
        else:
            print("Opção inválida. Escolha o tipo de serviço novamente.")

#num de paginas com desconto
def num_pagina():
    while True:
        try:
            paginas = float(input("Digite o número de páginas: "))
            if paginas >= 20000:
                print("Número de páginas acima do limite.")
                print("Por favor, entre com um número de páginas diferente.")
                continue
            elif paginas >= 2000:
                return paginas * 0.75 , paginas  #25%
            elif paginas >= 200:
                return paginas * 0.80 , paginas  # 20%
            elif paginas >= 20:
                return paginas * 0.85 , paginas  # 15%
            else:
                return paginas, paginas  #nenhum desconto
        except ValueError:
            print("Entrada inválida. Digite um número.")

#serviçoextra
def servico_extra():
    print('\nDeseja adicionar algum serviço extra?')
    print('1 - Encadernação simples - R$ 15.00')
    print('2 - Encadernação capa dura - R$ 40.00')
    print('0 - Não desejo mais nada.')
    while True:
        extra = input(">> ")
        if extra == "1":
            return 15.00  #simples
        elif extra == "2":
            return 40.00  #capadura
        elif extra == "0":
            return 0.00  #nada
        else:
            print("Opção inválida. Tente novamente.")

#código principal
servico_valor = escolha_servico()
paginas_com_desconto, paginas_original = num_pagina()
extra_valor = servico_extra()
total = (servico_valor * paginas_com_desconto) + extra_valor


print(f"\nTotal a pagar: R$ {total} (serviço:{servico_valor} * páginas: {paginas_original} + extra: {extra_valor})")
