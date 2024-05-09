import customtkinter as ctk  # Importando a biblioteca
import tkinter
from tkinter import messagebox
from PIL import Image

#Função para centralizar janela
def CenterWindowToDisplay(Screen: ctk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

#Acessar tela do app
def acessar():

    #Verifica se foi preenchido o usuário
    if (txtUsuario.get() == ""):
        messagebox.showerror("Erro", "Informe seu usuário!")
        txtUsuario.focus()
        return

    #Minimiza tela de login
    jnlLogin.withdraw()

    # Configurando Janela do App
    jnlApp = ctk.CTkToplevel()
    jnlApp.title("Equipe de Inspeção - Rio Tietê")
    jnlApp.geometry(CenterWindowToDisplay(jnlApp, 900, 500, jnlApp._get_window_scaling()))
    jnlApp.resizable(width=False, height=False)

    #Menu de chats
    frmMenu = ctk.CTkFrame(jnlApp, width=300, height=480, fg_color="transparent", border_width=3, border_color="teal", corner_radius=10)
    frmMenu.place(x=10,y=10)

    lblTrechos = ctk.CTkLabel(frmMenu, font=("arial", 20, "bold"), text="Trechos:")
    lblTrechos.grid(row=0, column=0, padx=10, pady=10)

    btnAlto = ctk.CTkButton(frmMenu, width=280, height=65, text="Alto Tietê", border_width=2, corner_radius=10, font=("arial-bold", 20, "bold"))
    btnAlto.grid(row=1, column=0, padx=10, pady=10)

    btnMedio = ctk.CTkButton(frmMenu, width=280, height=65, text="Médio Tietê", border_width=2, corner_radius=10, font=("arial-bold", 20, 'bold'))
    btnMedio.grid(row=2, column=0, padx=10, pady=10)

    btnInterioriano = ctk.CTkButton(frmMenu, width=280, height=65, text="Tietê Interior", border_width=2, corner_radius=10, font=("arial-bold", 20, 'bold'))
    btnInterioriano.grid(row=3, column=0, padx=10, pady=10)

    btnBaixo = ctk.CTkButton(frmMenu, width=280, height=65, text="Baixo Tietê", border_width=2, corner_radius=10, font=("arial-bold", 20, 'bold'))
    btnBaixo.grid(row=4, column=0, padx=10, pady=10)

    #Usuário
    frmUsuario = ctk.CTkFrame(frmMenu, width=280, height=70, fg_color="transparent", bg_color="#d3d3d3", border_width=2, border_color="teal", corner_radius=10)
    frmUsuario.grid(row = 5, column=0, padx=10, pady=10, sticky='w')

    lblUser = ctk.CTkLabel(frmUsuario, width=260, height=50, text="Bem vindo(a), " + txtUsuario.get() + "!", font=("arial",20, "bold"), fg_color="#d3d3d3")
    lblUser.grid(row=0,column=0, sticky="nsew", padx=10, pady=10)

    #Frame de chats
    frmChats = ctk.CTkFrame(jnlApp, width=570, height=478, fg_color="transparent", border_width=3, border_color="teal", corner_radius=10)
    frmChats.place(x=320,y=10)

    txtChat = ctk.CTkTextbox(frmChats, width=540, height=400, fg_color="transparent", border_width=3, border_color="#808080", corner_radius=10)
    txtChat.grid(column=0, row=0,columnspan=2, pady=10, padx=10)

    entMensagem = ctk.CTkEntry(frmChats, width=485, height = 40, fg_color="#d3d3d3", bg_color="transparent", corner_radius=10)
    entMensagem.grid(column=0, row=1, pady=10, padx=1) 

    btnEnviar = ctk.CTkButton(frmChats, width=40, height=40, text="OK")
    btnEnviar.grid(column=1, row=1)

# Configurando Janela de Login
jnlLogin = ctk.CTk()
jnlLogin._set_appearance_mode("light")
ctk.set_default_color_theme("green")
jnlLogin.title("Equipe de Inspeção - Rio Tietê")
jnlLogin.geometry(CenterWindowToDisplay(jnlLogin, 400, 400, jnlLogin._get_window_scaling()))
jnlLogin.resizable(width=False, height=False)

# Frame
frmLogin = ctk.CTkFrame(jnlLogin, width=380, height=380, fg_color="transparent", border_width=3, border_color="teal", corner_radius=15).place(x=10, y=10)

# Imagem SP
imgGov = ctk.CTkImage(light_image=Image.open(".\img\gov-sp.png"), size=(300, 250))
lblImgGov = ctk.CTkLabel(frmLogin, text=None, image=imgGov)
lblImgGov.pack(side=ctk.TOP, pady=20)

# Label Usuário
lblUsuario = ctk.CTkLabel(frmLogin, text="Usuário:")
lblUsuario.place(x=55, y=260)

# Entry Usuário
txtUsuario = ctk.CTkEntry(frmLogin,
                    width=300,
                    placeholder_text=None,
                    corner_radius=15)
txtUsuario.pack(side=ctk.TOP)

# Botão Acessar
btnAcessar = ctk.CTkButton(frmLogin, width=300, text="Acessar", command=acessar, corner_radius=15)
btnAcessar.pack(pady=10)
txtUsuario.focus()


#Executando janela
jnlLogin.mainloop()