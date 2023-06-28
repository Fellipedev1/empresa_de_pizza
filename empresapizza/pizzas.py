print("  🥰  Pizzaria do Fellipaão   🥰    ")
print("1 - A pizza de mussarela é R$ 23.90")
print("2 - A pizza de havaina é  R$ 20.90")
print("3 - A pizza de calabresa é  R$ 19.90")
print("4 - A pizza de margarida é  R$ 18.90")

escolha = input("Escolha qual pizza você quer: ")

while not escolha.isdigit() or int(escolha) not in range(1, 5):
    print("Seleção inválida. Por favor, escolha um número de item de menu válido.")
    escolha = input("Informe o número da pizza que deseja pedir: ")

tamanho = input("Informe a quantidade de pizzas que você quer: ")

while not tamanho.isdigit() or int(tamanho) <= 0:
    print("Quantidade inválida. Por favor, insira um número inteiro positivo.")
    tamanho = input("Informe a quantidade de pizzas que deseja pedir: ")

entrega = input("Você deseja entrega? (s/n): ")

while entrega != 's' and entrega != 'n':
    print("Resposta inválida. Por favor, responda 's' para Sim ou 'n' para Não.")
    entrega = input("Você deseja entrega? (s/n): ")

if entrega == 's':
    print("Pedido será entregue.")

preco_total = float(tamanho) * 0.0

if escolha == '1':
    preco_total = float(tamanho) * 23.90
elif escolha == '2':
    preco_total = float(tamanho) * 20.90
elif escolha == '3':
    preco_total = float(tamanho) * 19.90
elif escolha == '4':
    preco_total = float(tamanho) * 18.90

if entrega == 's':
    preco_total += 2.99

dinheiro = '{:.2f}'.format(preco_total)

print("Resumo do Pedido:")
print("Pizza selecionada: " + escolha)
print("Quantidade: " + tamanho)
if entrega == 's':
    print("Taxa de entrega: R$ 2.99")
print("Preço total: R$ " + str(dinheiro))
print("Qual será a forma de pagamento?")

pagamento = input("Para pix digite p, para cartão digite c, e d para dinheiro: ")

while pagamento not in ['c', 'p', 'd']:
    print("Opção de pagamento inválida. Por favor, digite 'c' para cartão, 'p' para pix ou 'd' para dinheiro.")
    pagamento = input("Para pix digite p, para cartão digite c, e d para dinheiro: ")

if pagamento == 'p':
    print("A chave do pix é 980989089089")
    print("")
    print("Assim que o pagamento for computado o pedido será liberado na loja ou para entrega. Obrigado!")
elif pagamento == 'c':
    print("Ok! Pague no balcão ou o motoboy irá levar a maquininha.") 
else:
    print("Para pagar em dinheiro, pague no balcão ou para o motoboy.")
