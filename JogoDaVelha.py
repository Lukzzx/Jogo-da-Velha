'''Primeiramente importamos o modulo Tkinter(que é basicamente uma biblioteca multiplataforma que fornece widgets para criação de interfaces gráficas), 
após isso importamos o modulo random(com o objetivo de possibilitar o sorteio de quem vai ser o primeiro jogador) e por fim importamos o módulo PIL
( com o objetivo de inserirmos no nosso menu uma imagem!)'''

from tkinter import *
import tkinter as tk
import random
from PIL import ImageTk, Image

'''Esse ponto teve por objetivo criar algumas lista como players(jogaores), player(jogador, que ja está com o comando de esccolher aleatoriamente um dos dois players),
ainda colocamos a lista botoes, com o objetivo de definir as variaveis para os botões do tabuleiro.'''

players = ["X", "O"]
player = random.choice(players)
botoes = [] 

#Aqui colocamos uma função que vai ser responsável por suportar e depois ser chamada para abrir a página do jogo

def abrir_jogo():
        
        #Aqui criamos uma função para observar e notar quando se deve ocorrer a proxima jogada, ou se o jogo acabou.

        def proxima_jogada(row, column):
            global player

            if botoes[row][column]['text'] == "" and conferir_ganhador() is False:
                if player == players[0]:
                    botoes[row][column]['text'] = player

                    if conferir_ganhador() is False:
                        player = players[1]
                        label.config(text=(players[1]+" <- Sua vez"))
                    elif conferir_ganhador() is True:
                        label.config(text=(players[0]+" <-GANHOU!!!"))
                    elif conferir_ganhador() == "Empate":
                        label.config(text="Deu velha!")
                else:
                    botoes[row][column]['text'] = player

                    if conferir_ganhador() is False:
                        player = players[0]
                        label.config(text=(players[0]+" <- Sua vez "))
                    elif conferir_ganhador() is True:
                        label.config(text=(players[1]+" <-GANHOU!!!"))
                    elif conferir_ganhador() == "Empate":
                        label.config(text="Deu velha!")

        '''Essa função tem por objetivo indentificar o ganhador ou o caso de empate da partida e assim informar a função *proxima_jogada* desse acontecido,além disso é obrigação dessa função 
        observar o caso de nenhuma dessas condições serem alcançadas,ela também informa a função *proxima_jogada* que nennhuma condição de termino de jogo aconteceu, para o jogo continuar.'''

        def conferir_ganhador():
            for row in range(3):
                if botoes[row][0]['text'] == botoes[row][1]['text'] == botoes[row][2]['text'] != "":
                    botoes[row][0].config(bg="green")
                    botoes[row][1].config(bg="green")
                    botoes[row][2].config(bg="green")
                    return True

            for column in range(3):
                if botoes[0][column]['text'] == botoes[1][column]['text'] == botoes[2][column]['text'] != "":
                    botoes[0][column].config(bg="green")
                    botoes[1][column].config(bg="green")
                    botoes[2][column].config(bg="green")
                    return True

            if botoes[0][0]['text'] == botoes[1][1]['text'] == botoes[2][2]['text'] != "":
                botoes[0][0].config(bg="green")
                botoes[1][1].config(bg="green")
                botoes[2][2].config(bg="green")
                return True

            elif botoes[0][2]['text'] == botoes[1][1]['text'] == botoes[2][0]['text'] != "":
                botoes[0][2].config(bg="green")
                botoes[1][1].config(bg="green")
                botoes[2][0].config(bg="green")
                return True

            elif espacos_vazio() is False:
                for row in range(3):
                    for column in range(3):
                        botoes[row][column].config(bg="yellow")
                return "Empate"
            else:
                return False

        #Essa função tem por objetivo determinar os espaços que estão vazios e de acordo com a quantidade,desses espaços, informar a função *proxima_jogada*.
        
        def espacos_vazio():
            espacos = 9
            for row in range(3):
                for column in range(3):
                    if botoes[row][column]['text'] != "":
                        espacos -= 1
            if espacos == 0:
                return False
            else:
                return True

        #Essa função tem por objetivo dar inicio a uma nova partida, selecionando um jogador aleatório.

        def nova_partida():
            global player
            player = random.choice(players)
            label.config(text=player+" <- Sua vez")
            for row in range(3):
                for column in range(3):
                    botoes[row][column].config(text="", bg="#F0F0F0")
        
        #Esse conjunto de comandos dão origem a janela do jogo.

        nova_janela = tk.Toplevel(root)
        nova_janela.title("Jogo da Velha")
        label = Label(nova_janela, text=player + " <- Sua vez", font=('consolas', 40))
        label.pack(side="top")

        botao_reiniciar = Button(nova_janela, text="Reiniciar", font=('consolas', 20), command=nova_partida)
        botao_reiniciar.pack(side="top")

        frame = Frame(nova_janela)  
        frame.pack()

        for row in range(3):
            row_botoes = []
            for column in range(3):
                botao = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                            command=lambda row=row, column=column: proxima_jogada(row, column))
                botao.grid(row=row, column=column)
                row_botoes.append(botao)
            botoes.append(row_botoes)

#Esse conjunto de comandos dão origem a janela do Menu.

root = tk.Tk()
root.title("Menu")

label = Label(text="Jogo da Velha #", font=('consolas', 70))
label.pack(side="top")

botao= Button(text="Iniciar", font=('consolas', 40), command=abrir_jogo)
botao.pack(side="top")

image = Image.open("imagens/image.jpg")

tk_image = ImageTk.PhotoImage(image)

image_label = Label(root, image=tk_image)
image_label.pack()

label_cred = Label(text="Créditos:", font=('consolas', 25))
label_cred.pack(side="top")

label_creditos = Label(text="CAIO LIMA, JOSE VICTOR, LEONARDO FILIPE, LUKAS FLÁVIO E SEARLE RYAN", font=('consolas', 20))
label_creditos.pack(side="top")

root.mainloop()
