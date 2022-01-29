from controllers.hospede import Hospede


Luciano = Hospede(
    firstName="Luciano",
    lastName="Martins",
    email="luci@gmail.com",
    cpf="177",
    password="123",
)

# Testando basico do usuário
print(Luciano)
print("\n")

Luciano.set_cpf("175727890")
print(Luciano)

Luciano.set_firstName("Lucianus")
print(Luciano)

Luciano.set_lastName("Figueira")
print(Luciano)

print("\n")
print(Luciano.createdAt())
print(Luciano.lastModify())
