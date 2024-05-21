import tkinter as tk
from random import randint
from tkinter import messagebox

# Funções do jogo
def jogar(escolha):
    itens = ('pedra', 'papel', 'tesoura')
    computador = randint(0, 2)

    escolha_computador = itens[computador]
    escolha_jogador = itens[escolha]

    resultado = f'Computador jogou {escolha_computador}\nVocê jogou {escolha_jogador}\n'

    if escolha == computador:
        resultado += 'Empate!'
    elif (escolha == 0 and computador == 2) or (escolha == 1 and computador == 0) or (escolha == 2 and computador == 1):
        resultado += 'Você ganhou!'
    else:
        resultado += 'Você perdeu!'

    messagebox.showinfo('Resultado', resultado)

# Janela principal
root = tk.Tk()
root.title('Jokenpô')

# Tamanho da janela
root.geometry('300x200')

# Centralizar janela
root.eval('tk::PlaceWindow . center')

# Texto de instrução
label = tk.Label(root, text='Vamos Jogar Jokenpô?\nEscolha uma opção:')
label.pack(pady=10)

# Botões
botoes = [
    ('Pedra', 0),
    ('Papel', 1),
    ('Tesoura', 2)
]

for texto, valor in botoes:
    button = tk.Button(root, text=texto, width=10, command=lambda v=valor: jogar(v))
    button.pack(pady=5)

# Iniciar o loop
root.mainloop()