import customtkinter as ctk
import tkinter
import cliente
import subprocess
from cliente import conectar_servidor
from cliente import enviar_mensagem
from tkinter import messagebox
from PIL import Image

image_enviar = ctk.CTkImage(Image.open(".\img\send.png"), size=(30, 30))

class App:
    def __init__(self):
        self.jnlLogin = ctk.CTk()
        self.jnlLogin._set_appearance_mode("light")
        ctk.set_default_color_theme("green")
        self.jnlLogin.title("Equipe de Inspeção - Rio Tietê")
        self.jnlLogin.geometry(self.center_window_to_display(self.jnlLogin, 400, 400))
        self.jnlLogin.resizable(width=False, height=False)

        self.frmLogin = ctk.CTkFrame(self.jnlLogin, width=380, height=380, fg_color="transparent", border_width=3, border_color="teal", corner_radius=15).place(x=10, y=10)

        imgGov = ctk.CTkImage(light_image=Image.open(".\img\gov-sp.png"), size=(300, 250))
        self.lblImgGov = ctk.CTkLabel(self.frmLogin, text=None, image=imgGov)
        self.lblImgGov.pack(side=ctk.TOP, pady=20)

        self.lblUsuario = ctk.CTkLabel(self.frmLogin, text="Usuário:")
        self.lblUsuario.place(x=55, y=260)

        self.txtUsuario = ctk.CTkEntry(self.frmLogin, width=300, placeholder_text=None, corner_radius=15)
        self.txtUsuario.pack(side=ctk.TOP)

        self.btnAcessar = ctk.CTkButton(self.frmLogin, width=300, text="Acessar", command=self.acessar, corner_radius=15)
        self.btnAcessar.pack(pady=10)
        self.txtUsuario.focus()

    def conectar_servidor_e_entrar(self, op_servidor):
        usuario = self.txtUsuario.get()
        conectar_servidor(op_servidor, usuario, self.txtChat)
        mensagem = f"Você entrou no servidor ['nome']"



    def center_window_to_display(self, window, window_width, window_height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        return f"{window_width}x{window_height}+{x}+{y}"

    def start_servers(self):
        # Iniciar os servidores em subprocessos
        subprocess.Popen(["python", "servidor.py", "8001"])
        subprocess.Popen(["python", "servidor.py", "8002"])
        subprocess.Popen(["python", "servidor.py", "8003"])
        subprocess.Popen(["python", "servidor.py", "8004"])

    def acessar(self):
        if (self.txtUsuario.get() == ""):
            messagebox.showerror("Erro", "Informe seu usuário!")
            self.txtUsuario.focus()
            return

        self.jnlLogin.withdraw()

        self.jnlApp = ctk.CTkToplevel()
        self.jnlApp.title("Equipe de Inspeção - Rio Tietê")
        self.jnlApp.geometry(self.center_window_to_display(self.jnlApp,900, 500))
        self.jnlApp.resizable(width=False, height=False)

        frmMenu = ctk.CTkFrame(self.jnlApp, width=300, height=480, fg_color="transparent", border_width=3, border_color="teal", corner_radius=10)
        frmMenu.place(x=10, y=10)

        lblTrechos = ctk.CTkLabel(frmMenu, font=("arial", 20, "bold"), text="Trechos:")
        lblTrechos.grid(row=0, column=0, padx=10, pady=10)

        btnAlto = ctk.CTkButton(frmMenu, width=280, height=65, text="Alto Tietê", border_width=2, corner_radius=10, font=("arial-bold", 20, "bold"), command=lambda: self.conectar_servidor_e_entrar(1))
        btnAlto.grid(row=1, column=0, padx=10, pady=10)

        btnMedio = ctk.CTkButton(frmMenu, width=280, height=65, text="Médio Tietê", border_width=2, corner_radius=10, font=("arial-bold", 20, 'bold'), command=lambda: self.conectar_servidor_e_entrar(2))
        btnMedio.grid(row=2, column=0, padx=10, pady=10)

        btnInterioriano = ctk.CTkButton(frmMenu, width=280, height=65, text="Tietê Interior", border_width=2, corner_radius=10, font=("arial-bold", 20, 'bold'), command=lambda: self.conectar_servidor_e_entrar(3))
        btnInterioriano.grid(row=3, column=0, padx=10, pady=10)

        btnBaixo = ctk.CTkButton(frmMenu, width=280, height=65, text="Baixo Tietê", border_width=2, corner_radius=10, font=("arial-bold", 20, 'bold'), command=lambda: self.conectar_servidor_e_entrar(4))
        btnBaixo.grid(row=4, column=0, padx=10, pady=10)

        frmUsuario = ctk.CTkFrame(frmMenu, width=280, height=70, fg_color="transparent", bg_color="#d3d3d3", border_width=2, border_color="teal", corner_radius=10)
        frmUsuario.grid(row = 5, column=0, padx=10, pady=10, sticky='w')

        lblUser = ctk.CTkLabel(frmUsuario, width=260, height=50, text="Bem vindo(a), " + self.txtUsuario.get() + "!", font=("arial",20, "bold"), fg_color="#d3d3d3")
        lblUser.grid(row=0,column=0, sticky="nsew", padx=10, pady=10)
        
        frmChats = ctk.CTkFrame(self.jnlApp, width=570, height=478, fg_color="transparent", border_width=3, border_color="teal", corner_radius=10)
        frmChats.place(x=320,y=10)

        txtChat = ctk.CTkTextbox(frmChats, width=540, height=400, fg_color="transparent", border_width=3, border_color="#808080", corner_radius=10)
        txtChat.grid(column=0, row=0,columnspan=2, pady=10, padx=10)

        entMensagem = ctk.CTkEntry(frmChats, width=485, height = 40, fg_color="#d3d3d3", bg_color="transparent", corner_radius=10)
        entMensagem.grid(column=0, row=1, pady=10, padx=1) 

        btnEnviar = ctk.CTkButton(frmChats, image=image_enviar, width=40, height=40, text='', command=lambda: self.enviar_mensagem(entMensagem))
        btnEnviar.grid(column=1, row=1)

    def enviar_mensagem(self, entMensagem):
        mensagem = entMensagem.get()  # Obter o texto do widget entMensagem
        cliente.enviar_mensagem(mensagem)  # Passar apenas a mensagem para a função do cliente
        entMensagem.delete(0, tkinter.END)  # Limpar o widget após enviar a mensagem

if __name__ == "__main__":
    app = App()
    app.start_servers()
    app.jnlLogin.mainloop()
