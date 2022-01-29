from datetime import datetime
from controllers.user import User


class Hospede(User):
    def __init__(self, firstName, lastName, email, cpf, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.cpf = cpf
        self.password = password
        self.create_at = datetime.now()
        self.last_att = datetime.now()
        self.wallet = 0

    def addCredits():
        "adicionar crédito pro cara pagar a estadia"
        pass

    def subtractCredits():
        "adicionar crédito pro cara pagar a estadia"
        pass

    def payAccommodation():
        "pagar com crédito pra estadia"
        pass

    def reserveAccomodation():
        "reservar a estadia"
        pass
