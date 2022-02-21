from datetime import datetime

from classes.mercadoriaViva import MercadoriaViva


class ImportedFish(MercadoriaViva):
    def __init__(
        self, firstName, quantity, priceWeight, codFish, origenCountry, taxImportation
    ):
        self.firstName = firstName
        self.quantity = quantity
        self.priceWeight = priceWeight
        self.codFish = codFish
        self.origenCountry = origenCountry
        self.taxImportation = taxImportation
        self.create_at = datetime.now()
        self.last_att = datetime.now()
        self.wallet = 0

    def price(self):
        return self.quantity * self.priceWeight

    def calcularValidade(self):
        "Visualizar quanto tempo esse peixe foi pescado"
        return datetime.today() - self.create_at

    def calcularPrecoValidadeVencida(self):
        "Se um peixeImportado não for vendido em 10 dias ele precisa receber um desconto progressivo"
        if self.calcularValidade().days() > 10:
            days = self.calcularValidade().days()
            desconto = ((days) / 100) * self.price()
            newPrice = self.price() - desconto
            return newPrice

    def calcularPrecoComTaxaImportação(self):
        "Peixes importados tem uma taxa de importação"
        preco = self.price()
        taxa = preco * 0.10
        return preco + taxa
