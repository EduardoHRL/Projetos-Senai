from tkinter import *
from tkinter import ttk

from insertClientes import *


class appClientes:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack(pady = 20)

        self.container = Frame(master)
        self.container.pack(pady = 5, padx = 20)

        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(pady = 5, padx = 20)

        self.terceiroContainer = Frame(master)
        self.terceiroContainer.pack(pady = 5, padx = 20)

        self.quartoContainer = Frame(master)
        self.quartoContainer.pack(pady = 5, padx = 20)

        self.quintoContainer = Frame(master)
        self.quintoContainer.pack(pady = 5, padx = 20)

        self.sextoContainer = Frame(master)
        self.sextoContainer.pack(pady = 5, padx = 20)

        self.containerComboBox = Frame(master)
        self.containerComboBox.pack(pady = 5, padx = 20)

        self.setimoContainer = Frame(master)
        self.setimoContainer.pack(pady = 5, padx = 20)


        self.cad = Label(self.primeiroContainer, text = "Cadastro de Clientes")
        self.cad.pack()

        self.buscarID = Label(self.container, text = "Buscar ID:", font = self.fontePadrao)
        self.buscarID.pack(side = LEFT)
        self.entID = Entry(self.container)
        self.entID["width"] = 5
        self.entID.pack(side = LEFT)

        self.botaoID = Button(self.container,text = "Buscar")
        self.botaoID["command"] = self.buscarUsuario
        self.botaoID.pack(padx = 5)
        

        self.txtNome = Label(self.segundoContainer,text = "Nome: ", font = self.fontePadrao, width = 10)
        self.txtNome.pack(side = LEFT)
        self.entNome = Entry(self.segundoContainer)
        self.entNome["width"] = 25
        self.entNome.pack(side = LEFT)

        self.txtTelefone = Label(self.terceiroContainer,text = "Telefone:", font = self.fontePadrao, width = 10)
        self.txtTelefone.pack(side = LEFT)
        self.entTelefone = Entry(self.terceiroContainer)
        self.entTelefone["width"] = 25
        self.entTelefone.pack()

        self.txtEmail = Label(self.quartoContainer,text = "Email:", font = self.fontePadrao, width = 10)
        self.txtEmail.pack(side=LEFT)
        self.entEmail = Entry(self.quartoContainer)
        self.entEmail["width"] = 25
        self.entEmail.pack()

        self.txtEndereco = Label(self.quintoContainer, text = "Endereço:", font = self.fontePadrao, width = 10)
        self.txtEndereco.pack(side = LEFT)
        self.entEndereco = Entry(self.quintoContainer)
        self.entEndereco["width"] =25
        self.entEndereco.pack()

        self.txtCpf = Label(self.sextoContainer, text = "Cpf:", font = self.fontePadrao, width = 10)
        self.txtCpf.pack(side = LEFT)
        self.entCpf = Entry(self.sextoContainer)
        self.entCpf["width"] =25
        self.entCpf.pack()

        self.txtCidade = Label(self.containerComboBox,text = "Seleção de cidades")
        self.txtCidade.pack()

        #self.combo = ttk.Combobox(self.containerComboBox, values=[self.buscarCombo()])
        #self.combo.pack(pady=20)

        self.b = Button()
        self.b["command"] = self.buscarCombo
        self.b.pack()



        self.botInsert = Button(self.setimoContainer,text="Inserir", width = 12)
        self.botInsert["command"] = self.inserirCliente
        self.botInsert.pack(side = LEFT)

        self.botAlterar = Button(self.setimoContainer, text = "Alterar", width = 12)
        self.botAlterar["command"] = self.alterarCliente
        self.botAlterar.pack(side = LEFT)

        self.botExcluir = Button(self.setimoContainer,text = "Excluir", width = 12)
        self.botExcluir["command"] = self.excluirCliente
        self.botExcluir.pack(side = LEFT)

        self.botLimpar = Button(self.setimoContainer, text = "Limpar", width = 12)
        self.botLimpar["command"] = self.Limpar
        self.botLimpar.pack(side = LEFT)

        self.msg = Label(text = "")
        self.msg.pack()

        self.tree = self.createTreeView(master)

    def Limpar(self):
        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entEndereco.delete(0, END)
        self.entCpf.delete(0, END)

    def inserirCliente(self):
        cli = cliente()

        cli.nome = self.entNome.get()
        cli.telefone = self.entTelefone.get()
        cli.email = self.entEmail.get()
        cli.endereco = self.entEndereco.get()
        cli.cpf = self.entCpf.get()

        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entEndereco.delete(0, END)
        self.entCpf.delete(0, END)

        self.msg["text"] = cli.insertCliente()
        self.atualizarTreeView()

    def alterarCliente(self):
        cli = cliente()

        self.msg["text"] = cli.updateCliente()

        cli.id = self.entID.get()
        cli.nome = self.entNome.get()
        cli.telefone = self.entTelefone.get()
        cli.email = self.entEmail.get()
        cli.endereco = self.entEndereco.get()
        cli.cpf = self.entCpf.get()

        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entEndereco.delete(0, END)
        self.entCpf.delete(0, END)

        self.msg["text"] = cli.updateCliente()
        self.atualizarTreeView()

    def excluirCliente(self):
        cli = cliente()

        cli.id = self.entID.get()

        self.msg["text"] = cli.deleteCliente()

        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entTelefone.delete(0, END)
        self.entEmail.delete(0, END)
        self.entEndereco.delete(0, END)
        self.entCpf.delete(0, END)
        
        self.atualizarTreeView()

    def buscarUsuario(self):
        cli = cliente()

        cli.id = self.entID.get()

        self.msg["text"] = cli.selectCliente()

        self.entID.delete(0, END)
        self.entID.insert(INSERT, cli.id)

        self.entNome.delete(0, END)
        self.entNome.insert(INSERT, cli.nome)

        self.entTelefone.delete(0, END)
        self.entTelefone.insert(INSERT,cli.telefone)

        self.entEmail.delete(0, END)
        self.entEmail.insert(INSERT, cli.email)

        self.entEndereco.delete(0, END)
        self.entEndereco.insert(INSERT, cli.endereco)

        self.entCpf.delete(0, END)
        self.entCpf.insert(INSERT, cli.cpf)


    def createTreeView(self, root):
        
        cli = cliente()

        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Telefone", "Email", "Endereco", "CPF"), show = "headings")
        self.tree.heading("ID", text = "ID")
        self.tree.heading("Nome", text = "Nome")
        self.tree.heading("Telefone", text = "Telefone")
        self.tree.heading("Email", text = "Email")
        self.tree.heading("Endereco", text = "Endereco")
        self.tree.heading("CPF", text= "CPF")
        
        self.tree.pack(fill = BOTH, expand = True)

        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = cli.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)
        
        return self.tree
    def atualizarTreeView(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        cli = cliente()
        rows = cli.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)

    def buscarCombo(self):
        cli = cliente()
        result = cli.buscarComboBox()

        for resultado in result:
            self.msg["text"] = resultado


if __name__ == "__main__":
    root = Tk()
    appClientes(root)
    root.mainloop()

        