"""
*
********************************************************************************************************************************
* Chat_Espaco_de_Tuplas.py 02/03/2022 a 04/07/2022                                                                             *
*                                                                                                                              *
*   ( )[][]                                                                                                                    *
*   [][]                                                                                                                       *
*   [][][]                                                                                                                     *
*   [][]   - Programação Paralela e Distribuida(PPD) - 2022.1 - Prof.Cidcley                                                   *
*                                                                                                                              *
* Copyright 2022 - João Gabriel Carneiro Medeiros,                                                                             *                                                                                                                            
* Instituto Federal de Educação, Ciência e Tecnologia do Ceará - IFCE                                                          *
* Todos os direitos reservados                                                                                                 *
******************************************************************************************************************************************************
*                                                                                                                                                    *
*  {SOBRE O TRABALHO} -  O código é a implementação de um CHAT usando 'ESPAÇO DE TUPLAS' do 4° Trabalho da cadeira de PPD do curso de Eng. Computação*
*                        do IFCE. O trabalho do aluno implementa uma comunicação num chat de tuplas, aonde a comuniação deve ser TODA implemetando   *
*                        somente essa tecnologia, por mais obsoleta que seja para esse propósito, POR ISSO HÁ MUITA LENTIDÃO NA APLICAÇÃO, desculpa. *
*                                                                                                                                                    *
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - É preferível que o código seja executado em qualquer versão mais atual do Windows(Mas também funciona em Linux)!                  * 
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - Lembre que foi disponibilizado um arquivo executável! Basta procurar na pasta por ele! Use-o caso o código não rode               *
*                  apropriadamente e você queira ver o funcionamento da aplicação mesmo assim.                                                       *
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - Pode ser que ao executar todos os códigos ao mesmo tempo,  a aplicação apresente travamentos ou bugs                              *
*                  o aluno otimizou o código o máximo que pôde no tempo dado e pede desculpas por quaisquer incovenientes. Se possível rode          *
*                  os códigos e os .exe em uma máquina com configurações relativamente boas!                                                         *
*                                                                                                                                                    *
******************************************************************************************************************************************************
*
"""
"""
*
*       *******************
*  ~~~ Bibliotecas utilizada ~~~
*       *******************
*
"""

import sys
import os
import threading, time, random

# Bibliotecas sobre MANIPULAÇÃO DE ESPAÇO DE TUPLAS em 'Python' (Só encontrei essas duas e apenas UMA funciona direito no Windows e acho que Linux Também!)
#from lindypy.lindypy import * <--- Não funcionou não importava quantas vezes eu tentasse :(
import linsimpy # https://github.com/robwalton/linsimpy <---- GRAÇAS A DEUSSSS ISSO FUNCIONAAAAA!!!! (Créditos ao autor dessa maravilha!)

#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
from AnimatedGIF import *


"""Principais variáveis (GLOBAIS) utilizadas"""

# Espaço de Tuplas
tse = None

# Flag para monitorar se há novas mensagens ou não
flag_Monitora_Novas_Mensagens = 0

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


"""
*
*       *********************************
*  ~~~ Parte que Mexe com Espaço de Tuplas () ~~~
*       *********************************
*
"""
    
#
# Obs. Aqui usa-se 'ts' para abreviar 'Tuple Spaces', os 'prints' vistos nas funções são apenas para 'debug' apenas!
#
    
# Criação da Sala e dasmatrizes para armazenar os INTEGRANTES e as MENSAGENS
def criaSala(ts, nomeSala):
    mensagens = []
    integrantes = []
    ts.out(("SALA", nomeSala, tuple(mensagens)))
    ts.out(("INT", nomeSala, tuple(integrantes)))

    salas = ts.inp(("SALAS", object))
    temp = list(salas[1])
    temp.append(nomeSala)
    ts.out(("SALAS", tuple(temp)))

# Add as mensagens a Lista de mensagens que a SALA em específico do chat do usuário possúi
def mandaMensagem(ts, nomeSala, remetente, destinatario, mensagem):
    mensagens = ts.inp(("SALA", nomeSala, object))
    temp = list(mensagens[2])
    temp.clear()
    
    if destinatario != "Todos":
        temp.append((destinatario,"<" + remetente + " - *Msg Privada para vc>: " + mensagem),)
    else:
        temp.append((destinatario,"<" + remetente + ">: " + mensagem),)
        
    ts.out(("SALA", nomeSala, tuple(temp)))
    print("Destinatario " + str(destinatario))
    print("Mandou MSG " + str(temp))

# Retorna a ''última mensagem enviada'' no chat de Tuplas
def recebeMensagem(ts, nomeSala):
    mensagens = ts.rdp(("SALA", nomeSala, object))
    print("Recebe MSG " + str(mensagens))
    
    return list(mensagens[2])
    
# Add usuário na sala em que entrou
def entraSala(ts, nome, nomeSala):
    integrantes = ts.inp(("INT", nomeSala, object))
    temp = list(integrantes[2])
    temp.append(nome)
    ts.out(("INT", nomeSala, tuple(temp)))
    print("Entrou sala " + nomeSala)

# Retira usuário da sala em que entrou
def saiSala(ts, nome, nomeSala):
    integrantes = ts.inp(("INT", nomeSala, object))
    temp = list(integrantes[2])
    temp.remove(nome)
    ts.out(("INT", nomeSala, tuple(temp)))
    print("Saiu sala " + nomeSala)

# Cria a tupla do Usuário e coloca ela na tupla 'USUARIOS' para ser armazenada
def criaUsuario(ts, nome):
    usuarios = ts.inp(("USUARIOS", object))
    temp = list(usuarios[1])
    temp.append(nome)
    ts.out(("USUARIOS", tuple(temp)))
    print("Usuarios: " + str(temp))

# Retira a tupla do Usuário daa tupla 'USUARIOS' aonde foi armazenada
def deletaUsuario(ts, nome):
    usuarios = ts.inp(("USUARIOS", object))
    temp = list(usuarios[1])
    print(temp)
    temp.remove(nome)
    ts.out(("USUARIOS", tuple(temp)))

# Lista integrantes de uma sala em específico 'nomeSala' 
def listarIntegrantes(ts, nomeSala):
    integrantes = ts.rdp(("INT", nomeSala, object))
    print(integrantes)
    return list(integrantes[2])

# Lista TODOS os USUÁRIOS do 'ts' ('Tuple Space')
def listaUsarios(ts):
    usuarios = ts.rdp(("USUARIOS", object))
    print(usuarios)
    
    return list(usuarios[1])

# Lista TODAS as SALAS do 'ts' ('Tuple Space')
def listarSalas(ts):
    salas = ts.rdp(("SALAS", object))
    print(salas)
    
    return list(salas[1]) # Link que ajudou nesse trecho: https://stackoverflow.com/questions/54336337/position-of-tuple-element-in-the-list


"""
*
*       ******************************************************
*  ~~~ Construção de Interface Gráfica com a biblioteca Tkinter ~~~
*       ******************************************************
*
"""

root = Tk()
root.withdraw()

path_img_botao_Entrar_asset = resource_path('recursos/botao_Entrar.png')
img_botao_Entrar_asset = PhotoImage(file=path_img_botao_Entrar_asset, master=root)

path_img_botao_Conversar_asset = resource_path('recursos/botao_Conversar.png')
img_botao_Conversar_asset = PhotoImage(file=path_img_botao_Conversar_asset, master=root)

path_img_botao_mandar_msg_asset = resource_path('recursos/botao_mandar_msg.png')
img_botao_mandar_msg_asset = PhotoImage(file=path_img_botao_mandar_msg_asset, master=root)

path_img_bg_usuario_lobby_asset = resource_path('recursos/bg_usuario_lobby.png')
img_bg_usuario_lobby_asset = PhotoImage(file=path_img_bg_usuario_lobby_asset, master=root)

path_img_bg_usuario_Chat_asset = resource_path('recursos/bg_usuario_Chat.png')
img_bg_usuario_Chat_asset = PhotoImage(file=path_img_bg_usuario_Chat_asset, master=root)

path_img_bg_configurar_Usuario_asset = resource_path('recursos/bg_configurar_Usuario.png')
img_bg_configurar_Usuario_asset = PhotoImage(file=path_img_bg_configurar_Usuario_asset, master=root)

path_img_botao_Conversar_privado_asset = resource_path('recursos/botao_Conversar_privado.png')
img_botao_Conversar_privado_asset = PhotoImage(file=path_img_botao_Conversar_privado_asset, master=root)

path_img_bg_Gera_Usuario_asset = resource_path('recursos/bg_Gera_Usuario.png')
img_bg_Gera_Usuario_asset = PhotoImage(file=path_img_bg_Gera_Usuario_asset, master=root)

path_img_botao_gerar_Usuario_asset = resource_path('recursos/botao_gerar_Usuario.png')
img_botao_gerar_Usuario_asset = PhotoImage(file=path_img_botao_gerar_Usuario_asset, master=root)

path_img_bg_nome_repetido_warning_asset = resource_path('recursos/bg_nome_repetido_warning.png')
img_bg_nome_repetido_warning_asset = PhotoImage(file=path_img_bg_nome_repetido_warning_asset, master=root)

path_img_bg_nome_repetido_sala_warning_asset = resource_path('recursos/bg_nome_repetido_sala_warning.png')
img_bg_nome_repetido_sala_warning_asset = PhotoImage(file=path_img_bg_nome_repetido_sala_warning_asset, master=root)

path_img_botao_Ok_asset = resource_path('recursos/botao_Ok.png')
img_botao_Ok_asset = PhotoImage(file=path_img_botao_Ok_asset, master=root)

path_img_chat_bubble_asset = resource_path('recursos/chat_bubble_ICON.png')
img_chat_bubble_asset = PhotoImage(file=path_img_chat_bubble_asset, master=root)

def fecha_APLICACAO(Toplevel):
    Toplevel.destroy()      
    Toplevel.quit()
    root. destroy()
    os._exit(1) 

def fecha_janela_TOPLEVEL(Toplevel):
    Toplevel.destroy()

def retorna_Config_Usuario(Toplevel):
    Toplevel.destroy()

def janela_Erro_Nome_Repetido_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("334x178")

    bg_label = Label(newWindow,image = img_bg_nome_repetido_warning_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    ok_button = Button(newWindow, image=img_botao_Ok_asset,command=lambda:fecha_janela_TOPLEVEL(newWindow))
    ok_button.place(x=107, y=127)

def janela_Erro_Nome_Repetido_Sala():
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("334x178")

    bg_label = Label(newWindow,image = img_bg_nome_repetido_sala_warning_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    ok_button = Button(newWindow, image=img_botao_Ok_asset,command=lambda:fecha_janela_TOPLEVEL(newWindow))
    ok_button.place(x=107, y=127)

def janela_Inicial():
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: ")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x301")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO(newWindow))

    bg_label = Label(newWindow,image = img_bg_Gera_Usuario_asset, width=324, height=301)
    bg_label.place(x=0, y=0)

    gif_bg_asset_url = resource_path('recursos/gifs/chat_bubble_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#70ad47')
    lbl_with_my_gif.place(x=135, y=71)
    lbl_with_my_gif.start()

    cria_usuario_button = Button(newWindow, image=img_botao_gerar_Usuario_asset,command=lambda:threadJanela_Config_Usuario(0,""))
    cria_usuario_button.place(x=84, y=213)

def threadJanela_Config_Usuario(flag_nome_usuario,nome_usuario_anterior):
     threading.Thread(target=janela_Config_Usuario, args=(flag_nome_usuario,nome_usuario_anterior,)).start() #<---- THREAD 'recebe_mensagens' *****

def janela_Config_Usuario(flag_nome_usuario,nome_usuario_anterior):   
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("457x422")

    bg_label = Label(newWindow,image = img_bg_configurar_Usuario_asset, width=453, height=417)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 50,height = 5,font = ("Callibri",9))
    text_area.place(x=40, y=220)
    text_area.focus()

    nome_usuario_text_input = Entry(newWindow)
    nome_usuario_text_input.place(x=33, y=127,width = 385,height = 25)

    sala_de_ENTRADA_text_input = Entry(newWindow)
    sala_de_ENTRADA_text_input.place(x=35, y=359,width = 325,height = 25)

    entrar_button = Button(newWindow, image=img_botao_Entrar_asset,command=lambda:janela_checa_Validade_Dados(newWindow,str(nome_usuario_text_input.get()),str(sala_de_ENTRADA_text_input.get())))
    entrar_button.place(x=259, y=37)

    if flag_nome_usuario == 1:
        nome_usuario_text_input.insert(0, nome_usuario_anterior + " <-- último nome usado pelo usuário...") # https://www.geeksforgeeks.org/how-to-set-the-default-text-of-tkinter-entry-widget/

    listaSalasAbertas(text_area)

def janela_checa_Validade_Dados(newWindow_close,nome_usuario,nome_sala_chat):
    global tse
    usuarios = listaUsarios(tse)
    salas = listarSalas(tse)
    
    if(nome_usuario != ""):
        # Verificamos se o nome do usuário é único em relação aos das outras Tuplas
        if (nome_usuario in usuarios):
            janela_Erro_Nome_Repetido_Usuario()
        else:
            if(nome_sala_chat!=""):
                # Verificamos se o nome da salacriada é único em relação aos das outras Tuplas
                if (nome_sala_chat in salas):
                    # Cria usuário e entra na sala especificada
                    criaUsuario(tse, nome_usuario)
                    entraSala(tse, nome_usuario, nome_sala_chat)
                    # Fecha a janela de configurações e entra na sala desejada
                    fecha_janela_TOPLEVEL(newWindow_close)
                    threadJanela_Chat_Geral_Usuario(nome_usuario,nome_sala_chat)
                else:
                    # Criamos o usuário e colocamos ele na tupla de Usuários em Geral
                    criaUsuario(tse, nome_usuario)
                    # Criamos a sala e a colocamos na tupla de Salas em Geral
                    criaSala(tse, nome_sala_chat)
                    entraSala(tse, nome_usuario, nome_sala_chat)
                    # Fecha a janela de configurações e entra na sala desejada (Na Thread que vai abrir a janela de Chat dela no caso, é um pouo travado rsrsrs)
                    fecha_janela_TOPLEVEL(newWindow_close)
                    threadJanela_Chat_Geral_Usuario(nome_usuario,nome_sala_chat)
            else:
                janela_Erro_Nome_Repetido_Sala()
    else:
        janela_Erro_Nome_Repetido_Usuario()

def threadJanela_Chat_Geral_Usuario(nome_usuario,nome_sala_chat):
     threading.Thread(target=janela_Chat_Geral_Usuario, args=(nome_usuario,nome_sala_chat,)).start() #<---- THREAD 'threadJanela_Chat_Geral_Usuario' *****

#Janela que exibe os usuários presentes na sala e permite ao usuário 'remetente' escolher o usuário 'destinatário' de suas mensagens no Chat
def janela_Lobby_Usuario(conversa_chat,salaAtual):
    global tse
    
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: ")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x362")

    bg_label = Label(newWindow,image = img_bg_usuario_lobby_asset, width=371, height=362)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 6.5,font = ("Callibri",9))
    text_area.place(x=36, y=140)
    text_area.focus()

    listaIntegrantes(text_area,salaAtual)

    escolhe_conversa_text_input = Entry(newWindow)
    escolhe_conversa_text_input.place(x=36, y=295,width = 296,height = 25)

    config_conversa_button = Button(newWindow, image=img_botao_Conversar_asset,command=lambda:muda_conversa_chat(conversa_chat,str(escolhe_conversa_text_input.get())))
    config_conversa_button.place(x=19, y=24)

# Aqui mudamos a variável 'conversa_chat' que define para quem as mensagens do usuário vão ser visto na sala
def muda_conversa_chat(conversa_chat,novo_destinatario):
    if novo_destinatario != '':
        conversa_chat['ID'] = novo_destinatario
        #print("Modo do chat: " + conversa_chat)

# Interface principal da sala de chat dos usuários
def janela_Chat_Geral_Usuario(nome_usuario,nome_sala_chat):
    global tse

    # Link que ajudou nesse trecho: https://stackoverflow.com/questions/32978440/changing-a-local-variable-in-a-function-from-another-function
    conversa_chat = {'ID': "Todos"} # Aqui vai indicar com quem o usuário vai mandar msg's! Se o valor for 'Todos' e mandará msg's para todos na sala, se nçao ele manda para alguém em específico na sala apenas!
    
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x469")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:janela_retorna_Configuracoes_Usuario(newWindow,1,nome_usuario,nome_sala_chat))

    bg_label = Label(newWindow,image = img_bg_usuario_Chat_asset, width=371, height=469)
    bg_label.place(x=0, y=0)

    #Abaixo é o campo do título do nome do usuário:
    bg_label_nome_cliente = Label(newWindow, text = nome_usuario,font = ("Callibri",18, 'bold'))
    bg_label_nome_cliente.config(bg='#70ad47')
    bg_label_nome_cliente.place(x=161, y=48)

    chat_bubble_icon_label = Label(newWindow, image=img_chat_bubble_asset)
    chat_bubble_icon_label.config(bg='#70ad47')
    chat_bubble_icon_label.place(x=86, y=24)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 14,font = ("Callibri",9))
    text_area.place(x=37, y=144)
    text_area.focus()

    text_area.insert(tk.INSERT,"[Chat Geral:] Sala '" + nome_sala_chat + "' //\n\n", 'msg_inicial_1')
    text_area.insert(tk.INSERT,"<Você entrou> Bem vindo ao Chat! ~\n", 'msg_inicial_2')

    text_area.tag_config('msg_inicial_1', foreground='blue')
    text_area.tag_config('msg_inicial_2', foreground='blue')

    msg_text_input = Entry(newWindow)
    msg_text_input.place(x=122, y=403,width = 205,height = 26)

    chat_privado_button = Button(newWindow, image=img_botao_Conversar_privado_asset,command=lambda:janela_Lobby_Usuario(conversa_chat,nome_sala_chat))
    chat_privado_button.place(x=292, y=103)

    envia_msg_button = Button(newWindow, image=img_botao_mandar_msg_asset,command=lambda:envia_mensagem(str(msg_text_input.get()),nome_usuario,nome_sala_chat,conversa_chat['ID']))
    envia_msg_button.place(x=42, y=388)

    #threading.Thread(target=recebe_mensagens, args=(text_area,nome_usuario,nome_sala_chat,)).start() 
    threadRecebe_Mensagens_func(text_area,nome_usuario,nome_sala_chat)

def threadRecebe_Mensagens_func(text_area,nome_usuario,nome_sala_chat):
     threading.Thread(target=recebe_mensagens, args=(text_area,nome_usuario,nome_sala_chat,)).start() #<---- THREAD 'recebe_mensagens' *****

# Função que faz o usuário 'retornar' a interface de 'Configuração do Usuário' quando sai da sala de chat
def janela_retorna_Configuracoes_Usuario(newWindow_close,flag_nome_usuario,nome_usuario_atual, nome_sala_atual):
    global tse
    saiSala(tse, nome_usuario_atual, nome_sala_atual)
    deletaUsuario(tse, nome_usuario_atual)
    fecha_janela_TOPLEVEL(newWindow_close)                             
    janela_Config_Usuario(flag_nome_usuario,nome_usuario_atual)

# Envia a mensagem do usuário para as outras Tuplas de usuários na sala                                  
def envia_mensagem(entry_widget,nome_usuario,nome_sala_chat,destinatario):
    global tse,flag_Monitora_Novas_Mensagens
    msg = entry_widget
    if(msg != ""):
        mandaMensagem(tse, nome_sala_chat, nome_usuario, destinatario, msg)
        flag_Monitora_Novas_Mensagens = 1

# Envia a mensagem do usuário para as outras Tuplas de usuários na sala ('Loop' que checa por novas mensagens enviadas) <------ "EXTREMAMENTE LENTO MESMO USANDO THREADING!" 
def recebe_mensagens(ScrolledText,nome_usuario,salaAtual):
    global tse,flag_Monitora_Novas_Mensagens
    
    while(True):
        if flag_Monitora_Novas_Mensagens == 1:
            msg_recebida = recebeMensagem(tse, salaAtual)
                                         
            #IMPRIME TODAS AS MENSAGENS NO SCROLLAREA
            if(msg_recebida[0][0] == "Todos"):
                ScrolledText.insert(tk.INSERT,msg_recebida[0][1]+"\n")
            elif(msg_recebida[0][0] == nome_usuario):
                ScrolledText.insert(tk.INSERT,msg_recebida[0][1]+"\n", 'msg_privada')
                ScrolledText.tag_config('msg_privada', background='yellow',foreground='red')
            flag_Monitora_Novas_Mensagens = 0
        else:
            pass

# Faz a atualização da lista de integrantes numa sala em específico dentre as TUPLAS
def listaIntegrantes(ScrolledText,salaAtual):
    global tse
    ScrolledText.delete('1.0', END)
    ScrolledText.insert(tk.INSERT,"[ ! ]: USUÁRIOS PRESENTES NA SALA: ...\n")
    #ScrolledText.insert(tk.INSERT,listarIntegrantes(tse, salaAtual))
    lista = listarIntegrantes(tse, salaAtual)
    # Link que ajudou nesse trecho: https://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
    print(*lista, sep='\n')
    ScrolledText.insert(tk.INSERT,"\n\n ...\n") 

# Faz a atualização da lista de SALAS dentre as TUPLAS de salas criadas
def listaSalasAbertas(ScrolledText):
    global tse
    atualiza_Salas = listarSalas(tse)
               
    if(len(atualiza_Salas) == 0): # Checa se nenhuma sala foi criada ainda...
        ScrolledText.delete('1.0', END)
        ScrolledText.insert(tk.INSERT,"**NENHUMA SALA FOI CRIADA AINDA! ...\n")                             
        ScrolledText.insert(tk.INSERT,"\n\n ...\n")
    else:
        ScrolledText.delete('1.0', END)
        ScrolledText.insert(tk.INSERT,"[ ! ]: AS SEGUINTES SALAS ESTÃO DISPONÍVEIS: ...\n")
        lista = listarSalas(tse)
        # Link que ajudou nesse trecho: https://stackoverflow.com/questions/15769246/pythonic-way-to-print-list-items
        print(*lista, sep='\n')
        ScrolledText.insert(tk.INSERT,"\n\n ...\n")

if __name__ == "__main__":
    tse = linsimpy.TupleSpaceEnvironment()

    usuarios = []
    salas = []
    tse.out(("USUARIOS", tuple(usuarios)))
    tse.out(("SALAS", tuple(salas)))

    #janela_Inicial()
    threading.Thread(target=janela_Inicial).start() #<---- THREAD 'janela_Inicial' *****
    root.mainloop()
