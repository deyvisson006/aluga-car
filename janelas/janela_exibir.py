import customtkinter as ctk

class ExibirVeiculos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Visualização de Veiculos')
        self.geometry('800x600')
        self.resizable(False, False)

        self.label_vizualizar = ctk.CTkLabel(self, text="Janela Visualizar")
        self.label_visualizar.pack()