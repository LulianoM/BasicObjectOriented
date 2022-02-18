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
