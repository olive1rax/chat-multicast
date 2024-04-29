import customtkinter as ctk  # Importando a biblioteca
import tkinter
from PIL import Image

#Função para centralizar janela
def CenterWindowToDisplay(Screen: ctk, width: int, height: int, scale_factor: float = 1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"
    
def acessar():
    
    usuario = txtUsuario.get()
    print(usuario)
    jnlLogin.withdraw()
    abrirApp()

def abrirApp():
    # Configurando Janela do App
    jnlApp = ctk.CTkToplevel()
    jnlApp.title("Equipe de Inspeção - Rio Tietê")
    jnlApp.geometry(CenterWindowToDisplay(jnlApp, 900, 500, jnlApp._get_window_scaling()))
    jnlApp.resizable(width=False, height=False)

    # Frame
    frmMenu = ctk.CTkFrame(jnlApp, width=300, height=480, fg_color="transparent", border_width=3, border_color="teal", corner_radius=10)
    frmMenu.place(x=10, y=10)

    btnAlto = ctk.CTkButton(frmMenu, width=280, height=100, text="Alto Tietê", border_width=2, corner_radius=10)
    btnAlto.grid(row=0, column=0, padx=10, pady=10)

    btnMedio = ctk.CTkButton(frmMenu, width=280, height=100, text="Médio Tietê", border_width=2, corner_radius=10)
    btnMedio.grid(row=1, column=0, padx=10, pady=10)

    btnInterioriano = ctk.CTkButton(frmMenu, width=280, height=100, text="Alto Tietê", border_width=2, corner_radius=10)
    btnInterioriano.grid(row=2, column=0, padx=10, pady=10)

    btnBaixo = ctk.CTkButton(frmMenu, width=280, height=100, text="Alto Tietê", border_width=2, corner_radius=10)
    btnBaixo.grid(row=3, column=0, padx=10, pady=10)



    # Imagem SP
    #imgGov = ctk.CTkImage(light_image=Image.open(".\img\gov-sp.png"), size=(100, 90))
    #lblImgGov = ctk.CTkLabel(jnlApp, text=None, image=imgGov)
    #lblImgGov.pack(side=ctk.TOP)

    # Label Usuário
    #lblUsuario = ctk.CTkLabel(frmLogin, text="Usuário:")
    #lblUsuario.place(x=55, y=260)

    # Entry Usuário
    #txtUsuario = ctk.CTkEntry(frmLogin,
    #                    width=300,
    #                    placeholder_text=None,
    #                    corner_radius=15)

    #txtUsuario.pack(side=ctk.TOP)

    # Botão Acessar
    #btnAcessar = ctk.CTkButton(frmLogin, width=300, text="Acessar", command=None, corner_radius=15)
    #btnAcessar.pack(pady=10)

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


#Executando janela
jnlLogin.mainloop()