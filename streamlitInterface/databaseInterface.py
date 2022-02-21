import pandas as pd


def createTables():
    PescadorTable = {
        "Nome": [],
        "CodPescador": [],
        "Embarcacao": [],
        "Wallet": [],
    }
    DataFramePescador = pd.DataFrame(data=PescadorTable)
    DataFramePescador.to_excel("database/DataFramePescador.xlsx")

    PeixeTable = {
        "Nome": [],
        "CodPescador": [],
        "Quantidade": [],
        "Preço": [],
        "CodPeixe": [],
    }
    DataFramePeixe = pd.DataFrame(data=PeixeTable)
    DataFramePeixe.to_excel("database/DataFramePeixe.xlsx")

    return "Bases Criadas"


def loadTables():
    try:
        DataFramePescador = pd.read_excel(
            "database/DataFramePescador.xlsx", index_col=0
        )
        DataFramePeixe = pd.read_excel("database/DataFramePeixe.xlsx", index_col=0)
        return DataFramePescador, DataFramePeixe
    except FileNotFoundError:
        createTables()
        DataFramePescador = pd.read_excel(
            "database/DataFramePescador.xlsx", index_col=0
        )
        DataFramePeixe = pd.read_excel("database/DataFramePeixe.xlsx", index_col=0)
        return DataFramePescador, DataFramePeixe


def saveTable(Data, Tipo):
    if Tipo == "Peixe":
        Data.to_excel("database/DataFramePeixe.xlsx")
    if Tipo == "Pescador":
        Data.to_excel("database/DataFramePescador.xlsx")
