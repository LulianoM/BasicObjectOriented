from datetime import datetime


class Crustaceans:
    def __init__(
        self,
        kilos,
        priceWeight,
        codFish,
    ):
        self.kilos = kilos
        self.priceWeight = priceWeight
        self.codFish = codFish
        self.create_at = datetime.now()
        self.last_att = datetime.now()
        self.wallet = 0

    def price(self):
        "Crustáceos são vendidos por kg e não por unidade como os peixes"
        return self.kilos * self.priceWeight

    def calcularValidade(self):
        "Visualizar quanto tempo esse peixe foi pescado"
        return datetime.today() - self.create_at

    def calcularPrecoValidadeVencida(self):
        "Se um crustácio não for vendido em 3 dias ele precisa receber um desconto progressivo"
        if (datetime.today() - self.create_at).days() > 3:
            days = (datetime.today() - self.create_at).days()
            desconto = ((days) / 100) * self.price()
            newPrice = self.price() - desconto
            return newPrice
