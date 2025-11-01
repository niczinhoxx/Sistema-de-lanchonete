import time  # Importa o módulo para criar pequenas pausas no terminal

print("Olá! Seja muito bem-vindo(a) à nossa lanchonete! 🍔🥤\n")
print("Nossas opções de lanche são:\n")

# Valores dos lanches
hamburguer = 12.00                
churrasco = 10.00                        
pastel = 7.50                     
salgado = 5.00  

print("1️⃣ Hambúrguer -- R$ 12.00")
print("2️⃣ Churrasco  -- R$ 10.00")
print("3️⃣ Pastel     -- R$  7.50")
print("4️⃣ Salgado    -- R$  5.00")
print("===========================================================\n")

# Entrada de quantidades
quant_hamburguer = int(input("Digite a quantidade de Hambúrgueres 🍔: "))
quant_churrasco = int(input("Digite a quantidade de Churrascos 🥩: "))
quant_pastel = int(input("Digite a quantidade de Pastéis 🥟: "))
quant_salgado = int(input("Digite a quantidade de Salgados 🧆: "))

print("===========================================================\n")

# Bebidas
print("-- Nossas opções de bebidas são --\n")

refrigerante = 5.00 
suco = 4.00  
agua = 2.00 

print("1️⃣ Refrigerante -- R$ 5.00")
print("2️⃣ Suco         -- R$ 4.00")
print("3️⃣ Água         -- R$ 2.00")
print("===========================================================\n")

quant_bebida1 = int(input("Digite a quantidade de Refrigerantes 🥤: "))
quant_bebida2 = int(input("Digite a quantidade de Sucos 🍹: "))
quant_bebida3 = int(input("Digite a quantidade de Águas 💧: "))

# Cálculo dos totais
preco_total_comida = (quant_hamburguer * hamburguer) + (quant_churrasco * churrasco) + (quant_pastel * pastel) + (quant_salgado * salgado)
preco_total_bebida = (quant_bebida1 * refrigerante) + (quant_bebida2 * suco) + (quant_bebida3 * agua) 
preco_final = preco_total_bebida + preco_total_comida

# Variável global para guardar gorjeta
valor_gorjeta = 0.0

print("===========================================================\n")
print(f"💰 O total da sua compra foi de: R$ {preco_final:.2f}")
print("===========================================================\n")

# Função para gorjeta
def calcular_gorjeta(valor):
    global valor_gorjeta

    print("Gostaria de adicionar uma gorjeta ao pedido? 💵")
    print("1️⃣ Sim")
    print("2️⃣ Não\n")

    escolha = int(input("Digite o número da sua escolha: "))

    if escolha == 1:
        print("\nEscolha a forma de adicionar a gorjeta:")
        print("1️⃣ Porcentagem (5%, 10% ou 15%)")
        print("2️⃣ Valor personalizado em reais 💸\n")

        tipo = int(input("Digite o número da opção desejada: "))

        if tipo == 1:
            print("\nEscolha a porcentagem da gorjeta:")
            print("1️⃣ 5%")
            print("2️⃣ 10%")
            print("3️⃣ 15%\n")
            
            opcao_gorjeta = int(input("Digite o número da opção desejada: "))

            match opcao_gorjeta:
                case 1:
                    valor_gorjeta = valor * 0.05
                case 2:
                    valor_gorjeta = valor * 0.10
                case 3:
                    valor_gorjeta = valor * 0.15
                case _:
                    print("❌ Opção inválida. Nenhuma gorjeta será adicionada.")
                    valor_gorjeta = 0.0

        elif tipo == 2:
            valor_gorjeta = float(input("\nDigite o valor da gorjeta em reais (ex: 5.00): R$ "))
        else:
            print("❌ Opção inválida. Nenhuma gorjeta será adicionada.")
            valor_gorjeta = 0.0

        valor_total = valor + valor_gorjeta
        print(f"\n💸 Gorjeta adicionada: R$ {valor_gorjeta:.2f}")
        print(f"💰 Total com gorjeta: R$ {valor_total:.2f}\n")
        return valor_total
    else:
        print("\nSem problemas! Nenhuma gorjeta foi adicionada. 👍")
        valor_gorjeta = 0.0
        return valor

# Atualiza o valor final com a gorjeta, se houver
preco_final = calcular_gorjeta(preco_final)

# Exibir resumo do pedido
def resumo_pedido():
    print("===========================================================")
    print("🧾 RESUMO DO SEU PEDIDO:")
    print("-----------------------------------------------------------")
    print(f"Hambúrguer x{quant_hamburguer} .......... R$ {quant_hamburguer * hamburguer:.2f}")
    print(f"Churrasco x{quant_churrasco} ........... R$ {quant_churrasco * churrasco:.2f}")
    print(f"Pastel x{quant_pastel} ................ R$ {quant_pastel * pastel:.2f}")
    print(f"Salgado x{quant_salgado} .............. R$ {quant_salgado * salgado:.2f}")
    print(f"Refrigerante x{quant_bebida1} ......... R$ {quant_bebida1 * refrigerante:.2f}")
    print(f"Suco x{quant_bebida2} ................. R$ {quant_bebida2 * suco:.2f}")
    print(f"Água x{quant_bebida3} ................. R$ {quant_bebida3 * agua:.2f}")
    print("-----------------------------------------------------------")
    print(f"Subtotal (sem gorjeta): R$ {preco_final - valor_gorjeta:.2f}")
    print(f"Gorjeta: ............... R$ {valor_gorjeta:.2f}")
    print("-----------------------------------------------------------")
    print(f"💰 TOTAL A PAGAR: R$ {preco_final:.2f}")
    print("===========================================================\n")

# Chama o resumo antes do pagamento
resumo_pedido()

# Escolha de pagamento
print("Qual forma de pagamento você deseja utilizar?\n")
print("1️⃣ Cartão de crédito")
print("2️⃣ Cartão de débito")
print("3️⃣ Pix\n")

opcao = int(input("Digite o número da opção desejada: "))

# Função de pagamento com animação
def forma_pagamento(opcao):
    print("\n💳 Processando pagamento", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.8)
    print("\n")

    match opcao:
        case 1:
            print("✅ Pagamento com cartão de crédito realizado com sucesso!")
        case 2:
            print("✅ Pagamento com cartão de débito realizado com sucesso!")
        case 3:
            print("✅ Pagamento via Pix realizado com sucesso!")
        case _:
            print("❌ Opção inválida. Tente novamente.")

    time.sleep(1)
    print("\n🧾 Gerando comprovante", end="")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.7)
    print("\n")

    print("🍔 Obrigado pela preferência! Volte sempre! 😄")

# Chamando a função de pagamento
forma_pagamento(opcao)
