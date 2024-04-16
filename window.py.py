import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class SistemaRegistroLivros:
    def __init__(self):
        # Inicializa a janela principal
        self.janela_principal = tk.Tk()
        self.janela_principal.title("Sistema de Registro de Livros)

        # Dicionário para armazenar informações sobre livros, alunos e datas de registro
        self.registros = []

        # Configurações da tabela
        self.tree = ttk.Treeview(self.janela_principal, columns=("Livro", "Aluno", "Data de Registro"), show="headings", height=10)
        self.tree.heading("Livro", text="Nome do Livro")
        self.tree.heading("Aluno", text="Nome do Aluno")
        self.tree.heading("Data de Registro", text="Data de Registro")
        self.tree.grid(row=0, column=0, columnspan=3, pady=10)

        # Configuração dos widgets da interface principal
        self.label_livro = tk.Label(self.janela_principal, text="Nome do Livro:")
        self.label_aluno = tk.Label(self.janela_principal, text="Nome do Aluno:")
        self.entry_livro = tk.Entry(self.janela_principal)
        self.entry_aluno = tk.Entry(self.janela_principal)
        self.botao_registrar = tk.Button(self.janela_principal, text="Registrar Livro", command=self.registrar_livro)
        self.botao_historico = tk.Button(self.janela_principal, text="Ver Histórico", command=self.mostrar_historico)

        # Posiciona widgets na janela principal
        self.label_livro.grid(row=1, column=0, pady=10)
        self.label_aluno.grid(row=1, column=1, pady=10)
        self.entry_livro.grid(row=1, column=2, pady=10)
        self.entry_aluno.grid(row=1, column=3, pady=10)
        self.botao_registrar.grid(row=2, column=2, pady=10)
        self.botao_historico.grid(row=2, column=3, pady=10)

        # Carrega o histórico de registros ao iniciar o sistema
        self.carregar_historico()

        # Inicia o loop principal da janela principal
        self.janela_principal.mainloop()

    def registrar_livro(self):
        livro = self.entry_livro.get()
        aluno = self.entry_aluno.get()

        if livro and aluno:
            # Adiciona o registro à lista
            data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.registros.append({"livro": livro, "aluno": aluno, "data_registro": data_registro})
            self.salvar_historico()

            # Atualiza a tabela
            self.atualizar_tabela()

            messagebox.showinfo("Registro de Livros", f"{livro} registrado com sucesso para o aluno {aluno}!")

            # Limpa os campos após o registro
            self.entry_livro.delete(0, tk.END)
            self.entry_aluno.delete(0, tk.END)
        else:
            messagebox.showerror("Registro de Livros", "Preencha o nome do livro e do aluno.")

    def atualizar_tabela(self):
        # Limpa todos os itens da tabela antes de atualizar
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Preenche a tabela com os registros
        for registro in self.registros:
            self.tree.insert("", "end", values=(registro["livro"], registro["aluno"], registro["data_registro"]))

    def mostrar_historico(self):
        # Cria uma nova janela para exibir o histórico
        janela_historico = tk.Toplevel(self.janela_principal)
        janela_historico.title("Histórico de Registros")

        # Texto para exibir o histórico
        texto_historico = tk.Text(janela_historico, width=40, height=10)
        texto_historico.pack(padx=10, pady=10)

        # Carrega o histórico de registros
        historico = self.carregar_historico()

        # Exibe o histórico no widget de texto
        texto_historico.insert(tk.END, historico)

    def salvar_historico(self):
        # Salva o histórico em um arquivo de texto
        with open("historico_registros.txt", "w") as arquivo:
            for registro in self.registros:
                arquivo.write(f"Livro: {registro['livro']}, Aluno: {registro['aluno']}, Data: {registro['data_registro']}\n")

    def carregar_historico(self):
        # Carrega o histórico de registros do arquivo de texto
        historico = ""
        try:
            with open("historico_registros.txt", "r") as arquivo:
                historico = arquivo.read()
        except FileNotFoundError:
            # Se o arquivo não existir, cria um novo
            pass
        return historico

# Inicia o sistema
sistema = SistemaRegistroLivros()
