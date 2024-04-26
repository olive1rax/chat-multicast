import customtkinter as ctk  # Importando a biblioteca
import tkinter
from PIL import Image
janela = ctk.CTk()  # Criando janela

# Configurando janela
janela._set_appearance_mode("light")
ctk.set_default_color_theme("green")
janela.title("Rio Tietê")
janela.geometry("900x600")
janela.resizable(width=False, height=False)

#Tabview
#tabview = ctk.CTkTabview(janela, width=400)
#tabview.pack()
#tabview.add("Servidor")
#tabview.add("Cliente")
#tabview.tab("Servidor").grid_columnconfigure(0, weight=1)
#tabview.tab("Cliente").grid_columnconfigure(0, weight=1)
#Adicionando elementos na tab
#text = ctk.CTkLabel(tabview.tab("Servidor"), text="IP:\nPorta:")
#text.pack()

#Frames
#frame1 = ctk.CTkFrame(janela, width=200, height=200, fg_color="green",bg_color="transparent" , border_width=10, border_color="teal", corner_radius=30).place(x=10, y=10)
#frame2 = ctk.CTkFrame(janela, width=200, height=200).place(x=220, y=10)
#frame3 = ctk.CTkFrame(janela, width=200, height=200).place(x=430, y=10)

#TEXTBOX
#textbox = ctk.CTkTextbox(janela, width=300, height=100, scrollbar_button_color="green", scrollbar_button_hover_color="teal", border_width=2, corner_radius=15,bg_color="black",border_color="green")
#textbox.pack()
#textbox.insert("0.0", "Valor:" + "Olá")


#DIALOG
#def abrirDialog():
    #dialog = ctk.CTkInputDialog(title="Dialog 1", text="Digite a #porta: ")
    #print(dialog.get_input())



#btnDialog = ctk.CTkButton(janela, text="Abrir Dialog", command=abrirDialog)
#btnDialog.pack()
'''
trechosctk = ctk.StringVar(value="Escolha")

def trechos(escolha):
    print(f"Trecho: {escolha}")

label = ctk.CTkLabel(janela, text="Trechos:", font=("arial-bold", 20)).pack()

trechos = ctk.CTkOptionMenu(janela, values=["Alto Tietê", "Médio Tietê", "Baixo Tietê", "Tietê Inferior"], variable=trechosctk, command=trechos)
trechos.pack(pady=50)
'''

img = ctk.CTkImage(light_image=Image.open("./img/send.png"), dark_image=Image.open("./img/send.png"),size=(20, 20))

def enviar():
    t = entry.get()
    label11.configure(text=str(t))
    entry.delete(0, tkinter.END)
    pass

label11 = ctk.CTkLabel(janela,
                       width=100,
                       height=100,
                       text_color="red",
                       font=("arial bold", 20))

label11.pack(pady=10)

entry = ctk.CTkEntry(janela, 
                    width=100,
                    height=10,
                    placeholder_text="DIGITE")
entry.pack(pady=10)

btn11 = ctk.CTkButton(janela, width=50, height=50, text="Enviar", command=enviar, image=img)
btn11.pack(pady=50)





















#Criando nova janela
#def novaTela():
#    novaJanela = ctk.CTkToplevel(janela, fg_color="teal")
#    novaJanela.geometry("200x200")


# Criando botão para chamar nova janela
#btnJanela = ctk.CTkButton(master=janela, text="Nova Janela", command=novaTela).place(x=300, y=300)

janela.mainloop()  # Executando janela