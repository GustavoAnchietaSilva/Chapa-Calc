import tkinter as tk
from tkinter import messagebox


def calcular():
    medida = entrada.get().lower()

    try:
        partes = medida.split("x")

        if len(partes) != 3:
            messagebox.showerror("Erro", "Use o formato: 21x15x15")
            return

        comprimento = float(partes[0]) * 10
        largura = float(partes[1]) * 10
        altura = float(partes[2]) * 10

        # Cálculos
        largura_chapa = largura + altura + 12
        comprimento_chapa = ((comprimento + largura) * 2) + 30 + 14 + 5

        vinco_meio = altura + 6
        sobra = largura_chapa - vinco_meio
        vinco_lateral = sobra / 2

        # Validação
        if largura_chapa < 250 or largura_chapa > 1140:
            status = "REPROVADA - Largura fora do limite"
        elif comprimento_chapa < 600 or comprimento_chapa > 2440:
            status = "REPROVADA - Comprimento fora do limite"
        else:
            status = "APROVADA"

        resultado_texto = f"""
Largura da Chapa: {largura_chapa:.2f} mm
Comprimento da Chapa: {comprimento_chapa:.2f} mm
Vinco: {vinco_lateral:.2f} x {vinco_meio:.2f} x {vinco_lateral:.2f}

Status: {status}
"""

        resultado.config(text=resultado_texto)

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números no formato correto.")


# Criar janela
janela = tk.Tk()
janela.title("Calculadora de Chapa - Caixa Maleta")
janela.geometry("450x350")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Calculadora de Chapa", font=("Arial", 16, "bold"))
titulo.pack(pady=10)

# Campo de entrada
entrada_label = tk.Label(janela, text="Digite a medida da caixa (ex: 21x15x15):")
entrada_label.pack()

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=5)

# Botão
botao = tk.Button(janela, text="Calcular", command=calcular, bg="#2ecc71", fg="white")
botao.pack(pady=10)

# Resultado
resultado = tk.Label(janela, text="", justify="left")
resultado.pack(pady=10)

# Rodar app
janela.mainloop()
