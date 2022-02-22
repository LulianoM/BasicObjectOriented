import streamlit as st
import pandas as pd

from classes.pescador import Pescador
from streamlitInterface.databaseInterface import saveTable
from streamlitInterface.tools import Tools


def PescadorInterface(DataFramePescador):
    TypeSelect = st.selectbox(
        "Selecione as opções", ["Cadastrar um Pescador", "Visualizar um Pescador"]
    )
    if TypeSelect == "Cadastrar um Pescador":
        CadastrarPescador(DataFramePescador)

    else:
        st.subheader("Visualizar um Pescador")
        VisualizarPescador(DataFramePescador)


def CadastrarPescador(DataFramePescador):
    st.subheader("Coloque aqui os dados do seu Pescador")
    NewPescador = Pescador(
        Nome=st.text_input("Nome"),
        CodPescador=int(st.number_input("CodPescador")),
        Embarcacao=st.text_input("Emcarcacao"),
    )
    if st.button("Cadastrar"):
        text = NewPescador.consultar_cadastro_pescador()

        PescadorTable = {
            "Nome": NewPescador.Nome,
            "CodPescador": NewPescador.CodPescador,
            "Embarcacao": NewPescador.Embarcacao,
            "Wallet": 0,
            "qtd_peixe": 0,
        }

        DataFramePescador = DataFramePescador.append(
            pd.Series(PescadorTable), ignore_index=True
        )
        saveTable(DataFramePescador, "Pescador")
        st.success(f"Pescador Cadastrado {text}")


def VisualizarPescador(DataFramePescador):
    if DataFramePescador.shape[0] == 0:
        st.error("Não há pescadores cadastrados! Cadastre um pescador primeiro.")
    else:
        pescador = st.selectbox(
            "Selecione os pescadores pelo seu código",
            DataFramePescador["CodPescador"],
        )
        PescadorLine = DataFramePescador[
            DataFramePescador["CodPescador"] == int(pescador)
        ]
        PescadorObject = Tools.SeriesToPescador(PescadorLine)
        st.text("Consultar Cadastro:")
        st.write(PescadorObject.consultar_cadastro_pescador())
        st.text("Consultar Saldo:")
        st.write(PescadorObject.ganho_pescador())
        st.text("Consultar Estoque Peixe:")
        st.write(PescadorObject.Estoque_peixe())
