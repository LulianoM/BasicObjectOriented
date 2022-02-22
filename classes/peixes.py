from datetime import datetime


class Fish:
    def __init__(self, firstName, codPescador, quantity, priceUnity, codFish):
        self.Nome = firstName
        self.codPescador = codPescador
        self.create_at = datetime.now()
        self.last_att = datetime.now()
        self.quantity = quantity
        self.priceUnity = priceUnity
        self.codFish = codFish
        self.create_at = datetime.now()
        self.last_att = datetime.now()

    def price(self):
        return self.quantity * self.priceUnity

    def calcularValidade(self):
        "Visualizar quanto tempo esse peixe foi pescado"
        return datetime.today() - self.create_at

    def calcularPrecoValidadeVencida(self):
        "Se um peixe não for vendido em 5 dias ele precisa receber um desconto progressivo"
        if (datetime.today() - self.create_at).days() > 5:
            days = (datetime.today() - self.create_at).days()
            desconto = ((days) / 100) * self.price()
            newPrice = self.price() - desconto
            return newPrice

    def info(self):
        return f"{self.Nome} - Pescado em: {self.create_at}"

    def set_Nome(self, newName):
        self.Nome = newName
        self.last_att = datetime.now()
        return self.Nome, self.last_att

    def lastModify(self):
        return self.last_att

    def createdAt(self):
        return self.create_at
