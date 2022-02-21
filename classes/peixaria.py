class Peixaria:
    def __init__(self, Nome, Local, CodPeixaria, Wallet=0, Estoque=0):
        self.Nome = Nome
        self.Local = Local
        self.CodPeixaria = CodPeixaria
        self.Wallet = Wallet
        self.Estoque = Estoque

    def consultar_cadastro(self):
        return (
            "Nome: "
            + self.Nome
            + "Local: "
            + self.Local
            + "CodPeixaria: "
            + str(self.CodPeixaria)
            + "Wallet: "
            + str(self.Wallet)
            + "Estoque: "
            + str(self.Estoque)
        )

    def VenderPeixe(self, valor):
        if self.Estoque >= 1:
            self.Wallet += valor
            self.Estoque -= 1
            print(
                "Nome: "
                + self.Nome
                + "Local: "
                + self.Local
                + "CodPescador: "
                + str(self.CodPescador)
                + "Wallet: "
                + str(self.Wallet)
                + "Estoque: "
                + str(self.Estoque)
            )
            return "Peixe Vendido"

    def consultarEstoque(self):
        return "Estoque: " + self.Estoque
