class Pescador:
    def __init__(self, Nome, Embarcacao, CodPescador, qtd_peixe=0, Wallet=0):
        self.Nome = Nome
        self.Embarcacao = Embarcacao
        self.CodPescador = CodPescador
        self.Wallet = Wallet
        self.qtd_peixe = qtd_peixe

    def venda_peixaria(self, quantidade_peixe, valorVenda):
        if self.qtd_peixe == 0:
            return "ATENÇÃO acabou o estoque de peixes"
        elif quantidade_peixe > self.qtd_peixe:
            return f"Não há peixes suficientes no estoque\nQuantidade de peixes no estoque:{str(self.qtd_peixe)}"
        else:
            self.qtd_peixe = self.qtd_peixe - quantidade_peixe
            self.Wallet += valorVenda
            return f"Peixe Vendido\nQuantidade de peixes no estoque:{str(self.qtd_peixe)}\nValor na carteira:{str(self.Wallet)}"

    def Estoque_peixe(self):
        return ("Quantidade de peixes no estoque:", str(self.qtd_peixe))

    def Adicionar_peixe(self, peixes):
        self.qtd_peixe += peixes
        return ("Quantidade de peixes no estoque:", str(self.qtd_peixe))

    def ganho_pescador(self):
        return ("Wallet:", self.Wallet)

    def consultar_cadastro_pescador(self):
        return (
            "Nome:",
            self.Nome,
            "Embarcação:",
            self.Embarcacao,
            "CodPescador:",
            str(self.CodPescador),
            "Wallet:",
            str(self.Wallet),
            "Quantidade de peixes no estoque:",
            str(self.qtd_peixe),
        )
