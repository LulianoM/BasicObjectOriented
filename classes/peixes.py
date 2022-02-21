from datetime import datetime

from classes.mercadoriaViva import MercadoriaViva


class Fish(MercadoriaViva):
    def __init__(self, firstName, quantity, priceUnity, codFish):
        self.firstName = firstName
        self.quantity = quantity
        self.priceUnity = priceUnity
        self.codFish = codFish
        self.create_at = datetime.now()
        self.last_att = datetime.now()
        self.wallet = 0

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
