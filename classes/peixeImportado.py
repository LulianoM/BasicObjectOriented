from datetime import datetime


class ImportedFish:
    def __init__(
        self,
        firstName,
        quantity,
        codPescador,
        priceWeight,
        codFish,
        origenCountry,
        taxImportation,
    ):
        self.Nome = firstName
        self.codPescador = codPescador
        self.quantity = quantity
        self.priceWeight = priceWeight
        self.codFish = codFish
        self.origenCountry = origenCountry
        self.taxImportation = taxImportation
        self.create_at = datetime.now()
        self.last_att = datetime.now()

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
        taxa = preco * self.taxImportation
        return preco + taxa

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
