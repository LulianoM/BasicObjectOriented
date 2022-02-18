from datetime import datetime


class MercadoriaViva:
    "this class is for create a MercadoriaViva"

    def __init__(
        self,
        firstName,
    ):
        self.firstName = firstName
        self.create_at = datetime.now()
        self.last_att = datetime.now()

    def __str__(self):
        return f"{self.firstName} - Pescado em: {self.create_at}"

    def set_firstName(self, newName):
        self.firstName = newName
        self.last_att = datetime.now()
        return self.firstName, self.last_att

    def lastModify(self):
        return self.last_att

    def createdAt(self):
        return self.create_at
