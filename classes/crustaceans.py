from datetime import datetime

from classes.mercadoriaViva import MercadoriaViva


class Crustaceans(MercadoriaViva):
    def __init__(
        self,
        firstName,
        quantity,
        priceWeight,
        codFish,
    ):
        self.firstName = firstName
        self.quantity = quantity
        self.priceWeight = priceWeight
        self.codFish = codFish
        self.create_at = datetime.now()
        self.last_att = datetime.now()
        self.wallet = 0

    def price(self):
        return self.quantity * self.priceWeight
