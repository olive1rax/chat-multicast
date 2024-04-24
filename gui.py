import customtkinter as ctk  # Importando a biblioteca


trechos = (["Alto Tietê", 2000], ["Médio Tietê", 3000], ["Baixo Tietê", 4000], ["Tietê Interior", 5000])


















janela = ctk.CTk()  # Criando janela

# Configurando janela
janela._set_appearance_mode("dark")
ctk.set_default_color_theme("green")
janela.title("Rio Tietê")
janela.geometry("900x600")
janela.resizable(width=False, height=False)

#Frames
frame1 = ctk.CTkFrame(janela, width=200, height=200, fg_color="green",bg_color="transparent" , border_width=10, border_color="teal", 
corner_radius=30).place(x=10, y=10)
frame2 = ctk.CTkFrame(janela, width=200, height=200).place(x=220, y=10)
frame3 = ctk.CTkFrame(janela, width=200, height=200).place(x=430, y=10)

#Criando nova janela
def novaTela():
    novaJanela = ctk.CTkToplevel(janela, fg_color="teal")
    novaJanela.geometry("200x200")


# Criando botão para chamar nova janela
btnJanela = ctk.CTkButton(master=janela, text="Nova Janela", command=novaTela).place(x=300, y=100)

janela.mainloop()  # Executando janela