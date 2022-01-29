from datetime import datetime


class User:
    "this class is for create a user"

    def __init__(self, firstName, lastName, email, cpf, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.cpf = cpf
        self.password = password
        self.create_at = datetime.now()
        self.last_att = datetime.now()

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.cpf}"

    def set_firstName(self, newName):
        self.firstName = newName
        self.last_att = datetime.now()
        return self.firstName, self.last_att

    def set_lastName(self, newLastName):
        self.lastName = newLastName
        self.last_att = datetime.now()
        return self.lastName, self.last_att

    def set_email(self, email):
        self.email = email
        self.last_att = datetime.now()
        return self.email, self.last_att

    def set_cpf(self, cpf):
        self.cpf = cpf
        self.last_att = datetime.now()
        return self.cpf, self.last_att

    def lastModify(self):
        return self.last_att

    def createdAt(self):
        return self.create_at

    class Wallet:
        "this class is for manage wallet"

        def __init__(self):
            self.walletValue = 0

        def addCredits():
            "adicionar crédito pro cara pagar a estadia"
            pass

        def subtractCredits():
            "adicionar crédito pro cara pagar a estadia"
            pass
