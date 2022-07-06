#Bibliotecas para manipulação dos arquivos de imagem utilizados no código para poder compactá-los no arquivo .exe quando for construido:
import sys
import os

#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
from AnimatedGIF import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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
#path_img_bg_usuario_Chat_Privado_asset = resource_path('recursos/bg_usuario_Chat_Privado.png')
#img_bg_usuario_Chat_Privado_asset = PhotoImage(file=path_img_bg_usuario_Chat_Privado_asset, master=root)

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

path_img_botao_Ok_asset = resource_path('recursos/botao_Ok.png')
img_botao_Ok_asset = PhotoImage(file=path_img_botao_Ok_asset, master=root)

def janela_Erro_Nome_Repetido_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("334x178")

    bg_label = Label(newWindow,image = img_bg_nome_repetido_warning_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    ok_button = Button(newWindow, image=img_botao_Ok_asset)
    ok_button.place(x=107, y=127)

def janela_Gerar_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("324x301")

    #newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO(newWindow))

    bg_label = Label(newWindow,image = img_bg_Gera_Usuario_asset, width=324, height=301)
    bg_label.place(x=0, y=0)

    gif_bg_asset_url = resource_path('recursos/gifs/chat_bubble_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#70ad47')
    lbl_with_my_gif.place(x=135, y=71)
    lbl_with_my_gif.start()

    cria_usuario_button = Button(newWindow, image=img_botao_gerar_Usuario_asset)
    cria_usuario_button.place(x=84, y=213)

def janela_Config_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Usuario")
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

    entrar_button = Button(newWindow, image=img_botao_Entrar_asset)
    entrar_button.place(x=259, y=37)

def janela_Lobby_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x362")

    bg_label = Label(newWindow,image = img_bg_usuario_lobby_asset, width=371, height=362)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 6.5,font = ("Callibri",9))
    text_area.place(x=36, y=140)
    text_area.focus()

    conversa_privada_text_input = Entry(newWindow)
    conversa_privada_text_input.place(x=36, y=295,width = 296,height = 25)

    conversar_button = Button(newWindow, image=img_botao_Conversar_asset)
    conversar_button.place(x=19, y=24)

def janela_Chat_Geral_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x469")

    bg_label = Label(newWindow,image = img_bg_usuario_Chat_asset, width=371, height=469)
    bg_label.place(x=0, y=0)

    #Abaixo é o campo do título do nome do usuário:
    bg_label_nome_cliente = Label(newWindow, text = "Usuario",font = ("Callibri",18, 'bold'))
    bg_label_nome_cliente.config(bg='#70ad47')
    bg_label_nome_cliente.place(x=161, y=48)

    gif_bg_asset_url = resource_path('recursos/gifs/chat_bubble_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#70ad47')
    lbl_with_my_gif.place(x=86, y=24)
    lbl_with_my_gif.start()

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 14,font = ("Callibri",9))
    text_area.place(x=37, y=144)
    text_area.focus()

    msg_text_input = Entry(newWindow)
    #msg_text_input.insert(0, "This is the default text") #https://www.geeksforgeeks.org/how-to-set-the-default-text-of-tkinter-entry-widget/
    msg_text_input.place(x=122, y=403,width = 205,height = 26)

    chat_privado_button = Button(newWindow, image=img_botao_Conversar_privado_asset)
    chat_privado_button.place(x=292, y=103)

    envia_msg_button = Button(newWindow, image=img_botao_mandar_msg_asset)
    envia_msg_button.place(x=42, y=388)

    #text_area_Topicos.insert(tk.INSERT,"Servidor conectado!\n")
    #text_area_Sensores.insert(tk.INSERT,"Servidor conectado!\n")

"""
def janela_Chat_Privado_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x469")

    bg_label = Label(newWindow,image = img_bg_usuario_Chat_Privado_asset, width=371, height=469)
    bg_label.place(x=0, y=0)

    #Abaixo é o campo do título do nome do usuário:
    bg_label_nome_cliente = Label(newWindow, text = "Usuario",font = ("Callibri",18, 'bold'))
    bg_label_nome_cliente.config(bg='#70ad47')
    bg_label_nome_cliente.place(x=161, y=48)

    gif_bg_asset_url = resource_path('recursos/gifs/chat_bubble_GIF.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#70ad47')
    lbl_with_my_gif.place(x=86, y=24)
    lbl_with_my_gif.start()

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 14,font = ("Callibri",9))
    text_area.place(x=37, y=144)
    text_area.focus()

    msg_text_input = Entry(newWindow)
    msg_text_input.place(x=122, y=403,width = 205,height = 26)

    envia_msg_button = Button(newWindow, image=img_botao_mandar_msg_asset)
    envia_msg_button.place(x=42, y=388)
"""
    
if __name__ == "__main__":

    janela_Chat_Geral_Usuario()
    root.mainloop()
