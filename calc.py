import tkinter as tk  
from tkinter import messagebox

# Função para calcular o empréstimo

def prestacao_mensal(valor_emprestimo, taxa_juros, prazo): # Função para calcular a prestação mensal, utilizando como entradas o valor do empréstimo, a taxa de juros e o prazo
    return (valor_emprestimo * taxa_juros) / (1 - ((1 + taxa_juros) ** (-prazo))) # Retorno da função, fornecendo a prestação mensal

def calcular_emprestimo(): # Função que calcula o empréstimo
    renda = float(entry_renda.get())  # Define a renda de quem solicita o empréstimo
    valor_emprestimo = float(entry_valor_emprestimo.get()) # Define o valor do empréstimo a ser solicitado
    prazo = int(entry_prazo.get()) # Define o prazo do empréstimo desejado pelo solicitante
    
    # Definição de taxas de juros em função das rendas do solicitante do empréstimo
    
    if 1320 <= renda <= 5000: # Define uma taxa de renda maior ou igual ao salário mínimo atual do Brasil (R$ 1.320,00) e R$ 5.000,00
        taxa_juros = 0.0799 # Define uma taxa de juros de 7,99% 
    elif 5000 < renda <= 8500: # Faixa de renda maior que R$ 5.000,00 e menor ou igual a R$ 8.500,00
        taxa_juros = 0.0855 # Define uma taxa de juros de 8,55%
    elif 8500 < renda <= 10000: # Faixa de renda maior que R$ 8.500,00 e menor ou igual a R$ 10.000,00
        taxa_juros = 0.09 # Define uma taxa de juros de 9,00%
    elif 10000 < renda <= 15000: # Faixa de renda maior que R$ 10.000,00 e menor ou igual a R$ 15.000,00
        taxa_juros = 0.12 # Define uma taxa de juros de 12,00%
    elif 15000 < renda <= 20000: # Faixa de renda maior que R$ 15.000,00 e menor ou igual a R$ 20.000,00
        taxa_juros = 0.14 # Define uma taxa de juros de 14,00%
    elif 20000 < renda <= 25000: # Faixa de renda maior que R$ 20.000,00 e menor ou igual a R$ 25.000,00
        taxa_juros = 0.16 # Define uma taxa de juros de 16,00%
    elif renda > 25000: # Faixa de renda maior que R$ 25.000,00
        taxa_juros = 0.18 # Define uma taxa de juros de 18,00%
    else:
        messagebox.showwarning("Aviso", "A renda inserida não é válida ou está fora dos limites permitidos.") 
        # Chamada para renda inferior a um salário mínimo
        return

    prestacao_mensal_valor = prestacao_mensal(valor_emprestimo, taxa_juros, prazo) # Chamada da função de cálculo da prestação mensal
    valor_total = prestacao_mensal_valor * prazo # Cálculo do valor total a ser pago no empréstimo

    label_resultado.config(text=f"O valor das prestações mensais é de: R$ {prestacao_mensal_valor:,.2f}\n"
                                f"O custo total do empréstimo é de: R$ {valor_total:,.2f}\n"
                                f"A taxa de juros para este empréstimo foi de: {taxa_juros*100:.2f}% ao mês") 
    # Informa o valor das prestações mensais, o custo total do empréstimo e a taxa de juros a ser paga

def centralizar_janela(root, largura, altura): # Função de centralização da janela da interface gráfica
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    root.geometry(f'{largura}x{altura}+{x}+{y}')


# Configuração da janela principal
root = tk.Tk()
root.title("CALCULADORA FINANCEIRA") # Título da caixa de mensagem

largura_janela = 400  # Largura desejada da janela
altura_janela = 400  # Altura desejada da janela

root.geometry(f'{largura_janela}x{altura_janela}')  # Definir tamanho da janela
root.resizable(False, False)  # Tornar a janela não redimensionável

centralizar_janela(root, largura_janela, altura_janela)  # Centralizar a janela na tela

# Criando os widgets (rótulos, entradas e botões)
label_renda = tk.Label(root, text="Renda Mensal:")
label_renda.pack()

entry_renda = tk.Entry(root)
entry_renda.pack()

label_valor_emprestimo = tk.Label(root, text="Valor do Empréstimo:")
label_valor_emprestimo.pack()

entry_valor_emprestimo = tk.Entry(root)
entry_valor_emprestimo.pack()

label_prazo = tk.Label(root, text="Prazo (em meses):")
label_prazo.pack()

entry_prazo = tk.Entry(root)
entry_prazo.pack()

button_calcular = tk.Button(root, text="Calcular Empréstimo", command=calcular_emprestimo)
button_calcular.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()


# Iniciar o loop da interface gráfica
root.mainloop()
