import streamlit as st
import pandas as pd
from classes.peixeImportado import ImportedFish
from classes.peixes import Fish
from classes.pescador import Pescador
from streamlitInterface.databaseInterface import saveTable
from streamlitInterface.pescadorRegistration import CadastrarPescador
from streamlitInterface.tools import Tools


def FishInterface(DataFramePeixe, DataFramePescador):
    if DataFramePescador.shape[0] == 0:
        st.error(
            "Não há pescadores cadastrados! Cadastre um pescador primeiro antes de cadastrar um peixe"
        )
    else:
        pescador = st.selectbox(
            "Selecione os pescadores pelo seu código",
            DataFramePescador["CodPescador"],
        )
        PescadorLine = DataFramePescador[
            DataFramePescador["CodPescador"] == int(pescador)
        ]
        PescadorObject = Tools.SeriesToPescador(PescadorLine)
        st.text("Pescador Selecionado:")
        st.write(PescadorObject.consultar_cadastro_pescador())
        st.text("Mercadorias do pescador:")
        PeixesPescador = DataFramePeixe[DataFramePeixe["CodPescador"] == pescador]
        if PeixesPescador.shape[0] == 0:
            st.text("Não há Mercadorias")
        else:
            st.dataframe(PeixesPescador)

        if PescadorObject:
            CadastrarMercadoria(DataFramePeixe, pescador)


def CadastrarMercadoria(DataFramePeixe, pescador):
    st.subheader("Coloque aqui os dados da sua Mercadoria")
    TypePeixe = st.selectbox(
        "Selecione o tipo de Mercadoria Viva", ["Peixe", "Crustácio", "Peixe Importado"]
    )
    if TypePeixe == "Peixe":
        CreatePeixe(pescador, DataFramePeixe)
    elif TypePeixe == "Crustácio":
        st.error("Não disponível")
    elif TypePeixe == "Peixe Importado":
        CreatePeixeImportado(pescador, DataFramePeixe)


def CreatePeixe(pescador, DataFramePeixe):
    NewPeixe = Fish(
        firstName=st.text_input("Nome"),
        quantity=int(st.number_input("Quantidade")),
        priceUnity=st.number_input("Preço Unidade"),
        codFish=int(st.number_input("Código Peixe")),
        codPescador=pescador,
    )
    if st.button("Cadastrar"):
        text = NewPeixe.info()

        PeixeTable = {
            "Nome": NewPeixe.Nome,
            "CodPescador": NewPeixe.codPescador,
            "Quantidade": NewPeixe.quantity,
            "CodPeixe": NewPeixe.codFish,
            "PrecoUnidadade": NewPeixe.priceUnity,
            "PaísOrigem": "Brasil",
            "TaxImport": 0,
        }

        DataFramePeixe = DataFramePeixe.append(pd.Series(PeixeTable), ignore_index=True)
        saveTable(DataFramePeixe, "Peixe")
        st.success(f"Peixe Cadastrado {text}")


def CreatePeixeImportado(pescador, DataFramePeixe):
    NewPeixe = ImportedFish(
        firstName=st.text_input("Nome"),
        quantity=int(st.number_input("Quantidade")),
        priceWeight=st.number_input("Preço Unidade"),
        codFish=int(st.number_input("Código Peixe")),
        origenCountry=st.text_input("País de Origem"),
        taxImportation=st.number_input("Taxa de Importação"),
        codPescador=pescador,
    )

    if st.button("Cadastrar"):
        text = NewPeixe.info()
        PeixeTable = {
            "Nome": NewPeixe.Nome,
            "CodPescador": NewPeixe.codPescador,
            "Quantidade": NewPeixe.quantity,
            "CodPeixe": NewPeixe.codFish,
            "PaísOrigem": NewPeixe.origenCountry,
            "TaxImport": NewPeixe.taxImportation,
            "PrecoKilo": NewPeixe.priceWeight,
        }

        DataFramePeixe = DataFramePeixe.append(pd.Series(PeixeTable), ignore_index=True)
        saveTable(DataFramePeixe, "Peixe")
        st.success(f"Peixe Cadastrado {text}")
