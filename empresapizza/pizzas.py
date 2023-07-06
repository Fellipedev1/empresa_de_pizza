import tkinter as tk
from tkinter import messagebox

pizza_choices = [("1 - A pizza de mussarela é R$ 23.90", "1"),
                 ("2 - A pizza de havaiana é R$ 20.90", "2"),
                 ("3 - A pizza de calabresa é R$ 19.90", "3"),
                 ("4 - A pizza de margarita é R$ 18.90", "4")]

pizza_selection = []

def place_order():
    tamanho = pizza_quantity.get()
    entrega = delivery_choice.get()
    pagamento = payment_choice.get()

    if not tamanho.isdigit() or int(tamanho) <= 0:
        messagebox.showerror("Erro", "Quantidade inválida. Por favor, insira um número inteiro positivo.")
        return

    if entrega != 's' and entrega != 'n':
        messagebox.showerror("Erro", "Resposta inválida. Por favor, responda 's' para Sim ou 'n' para Não.")
        return

    if pagamento not in ['c', 'p', 'd']:
        messagebox.showerror("Erro", "Opção de pagamento inválida. Por favor, digite 'c' para cartão, 'p' para pix ou 'd' para dinheiro.")
        return

    if entrega == 's':
        messagebox.showinfo("Informação", "Pedido será entregue.")

    preco_total = 0.0

    for escolha, tamanho in pizza_selection:
        preco = float(tamanho) * float(escolha.split(" ")[-1])
        preco_total += preco

    if entrega == 's':
        preco_total += 2.99

    dinheiro = '{:.2f}'.format(preco_total)

    summary = f"Resumo do Pedido:\n\n"

    for escolha, tamanho in pizza_selection:
        summary += f"Pizza selecionada: {escolha}\n"
        summary += f"Quantidade: {tamanho}\n"

    if entrega == 's':
        summary += "Taxa de entrega: R$ 2.99\n"
    summary += f"Preço total: R$ {dinheiro}\n\n"
    summary += "Qual será a forma de pagamento?"

    if pagamento == 'p':
        summary += "\n\nA chave do pix é 980989089089\n\nAssim que o pagamento for computado, o pedido será liberado na loja ou para entrega. Obrigado!"
    elif pagamento == 'c':
        summary += "\n\nOk! Pague no balcão ou o motoboy irá levar a maquininha."
    else:
        summary += "\n\nPara pagar em dinheiro, pague no balcão ou para o motoboy."

    messagebox.showinfo("Resumo do Pedido", summary)

def add_pizza():
    escolha = pizza_choice.get()
    tamanho = pizza_quantity.get()

    if not escolha.isdigit() or int(escolha) not in range(1, 5):
        messagebox.showerror("Erro", "Seleção inválida. Por favor, escolha um número de item de menu válido.")
        return

    if not tamanho.isdigit() or int(tamanho) <= 0:
        messagebox.showerror("Erro", "Quantidade inválida. Por favor, insira um número inteiro positivo.")
        return

    pizza_selection.append((pizza_choices[int(escolha) - 1][0], tamanho))
    messagebox.showinfo("Sucesso", "Pizza adicionada com sucesso!")

window = tk.Tk()
window.title("Pizzaria do Fellipaão")
window.configure(background='light blue')

# Pizza choice
pizza_choice_label = tk.Label(window, text="Escolha qual pizza você quer:", font=("Arial", 12))
pizza_choice_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
pizza_choice = tk.StringVar(window)
pizza_choice.set("1")

for i, (choice, value) in enumerate(pizza_choices):
    rb = tk.Radiobutton(window, text=choice, variable=pizza_choice, value=value, font=("Arial", 11))
    rb.grid(row=i+1, column=0, sticky="w", padx=10)
    rb.configure(bg='light blue', fg='black') 

# Pizza quantity
pizza_quantity_label = tk.Label(window, text="Informe a quantidade de pizzas que você quer:", font=("Arial", 12))
pizza_quantity_label.grid(row=len(pizza_choices)+1, column=0, sticky="w", padx=10, pady=10)
pizza_quantity = tk.Entry(window, font=("Arial", 11))
pizza_quantity.grid(row=len(pizza_choices)+2, column=0, sticky="w", padx=10)

# Add pizza button
add_pizza_button = tk.Button(window, text="Adicionar Pizza", command=add_pizza, font=("Arial", 12), bg="green", fg="white")
add_pizza_button.grid(row=len(pizza_choices)+3, column=0, pady=10)

# Delivery choice
delivery_choice_label = tk.Label(window, text="Você deseja entrega? (s/n):", font=("Arial", 12))
delivery_choice_label.grid(row=len(pizza_choices)+4, column=0, sticky="w", padx=10, pady=10)
delivery_choice = tk.StringVar(window)
delivery_choice.set("n")
delivery_rb1 = tk.Radiobutton(window, text="Sim", variable=delivery_choice, value="s", font=("Arial", 11))
delivery_rb2 = tk.Radiobutton(window, text="Não", variable=delivery_choice, value="n", font=("Arial", 11))
delivery_rb1.grid(row=len(pizza_choices)+5, column=0, sticky="w", padx=10)
delivery_rb2.grid(row=len(pizza_choices)+6, column=0, sticky="w", padx=10)

# Payment choice
payment_choice_label = tk.Label(window, text="Qual será a forma de pagamento?", font=("Arial", 12))
payment_choice_label.grid(row=len(pizza_choices)+7, column=0, sticky="w", padx=10, pady=10)
payment_choice = tk.StringVar(window)
payment_choice.set("c")
payment_rb1 = tk.Radiobutton(window, text="Pix", variable=payment_choice, value="p", font=("Arial", 11))
payment_rb2 = tk.Radiobutton(window, text="Cartão", variable=payment_choice, value="c", font=("Arial", 11))
payment_rb3 = tk.Radiobutton(window, text="Dinheiro", variable=payment_choice, value="d", font=("Arial", 11))
payment_rb1.grid(row=len(pizza_choices)+8, column=0, sticky="w", padx=10)
payment_rb2.grid(row=len(pizza_choices)+9, column=0, sticky="w", padx=10)
payment_rb3.grid(row=len(pizza_choices)+10, column=0, sticky="w", padx=10)

# Place order button
order_button = tk.Button(window, text="Fazer Pedido", command=place_order, font=("Arial", 14), bg="green", fg="white")
order_button.grid(row=len(pizza_choices)+11, column=0, pady=10)

window.mainloop()
