
print('\nBEM VINDO A LOJA DE GELADOS')
print('-' * 20 + 'MENU' + '-'* 20)
print('   | Tamanho | Cupuaçu (CP) | Açaí (AC) |')
print('   |---------|--------------|-----------|')
print('   |    P    |   R$  9.00   |  R$ 11.00 |')
print('   |    M    |   R$ 14.00   |  R$ 16.00 |')
print('   |    G    |   R$ 18.00   |  R$ 20.00 |')
print('-' * 44)


total_pedido = 0

while True:
    while True:
        sabor = input("\nDigite o sabor (CP para Cupuaçu, AC para Açaí): ").upper()
        if sabor in ["CP", "AC"]:
            break
        else:
            print("Sabor inválido. Tente novamente")
            continue


    while True:
        tamanho = input("Digite o tamanho (P, M, G): ").upper()
        if tamanho in ["P", "M", "G"]:
            break  # Sai do loop se o tamanho for válido
        else:
            print("Tamanho inválido. Tente novamente")
            continue


    if sabor == "CP":
        if tamanho == "P":
            preco = 9.0
        elif tamanho == "M":
            preco = 14.0
        else:
            preco = 18.0
    else:
        if tamanho == "P":
            preco = 11.0
        elif tamanho == "M":
            preco = 16.0
        else:
            preco = 20.0


    total_pedido += preco


    print(f"Pedido: {sabor} tamanho {tamanho} - R$ {preco:}")
    print(f"Total acumulado: R$ {total_pedido:}")


    while True:
        continuar = input("\nDeseja pedir mais alguma coisa? (S/N): ").upper()
        if continuar in ["S", "N"]:
            break
        print("Resposta inválida. Digite S ou N.")

    if continuar == "N":
        break

print(f"\nTotal do pedido: R$ {total_pedido}")
print("Obrigado pela sua compra!")
