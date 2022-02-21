import streamlit as st
import pandas as pd

from classes.pescador import Pescador
from streamlitInterface.databaseInterface import saveTable


def PescadorInterface(DataFramePescador):
    TypeSelect = st.selectbox(
        "Selecione as opções", ["Cadastras um Pescador", "Visualizar um Pescador"]
    )
    if TypeSelect == "Cadastras um Pescador":
        st.subheader("Coloque aqui os dados do seu Pescador")
        NewPescador = Pescador(
            Nome=st.text_input("Nome"),
            CodPescador=st.text_input("CodPescador"),
            Embarcacao=st.text_input("Emcarcacao"),
        )
        if st.button("Cadastrar"):
            text = NewPescador.consultar_cadastro_pescador()

            PescadorTable = {
                "Nome": NewPescador.Nome,
                "CodPescador": NewPescador.CodPescador,
                "Embarcacao": NewPescador.Embarcacao,
                "Wallet": 0,
            }

            DataFramePescador = DataFramePescador.append(
                pd.Series(PescadorTable), ignore_index=True
            )
            saveTable(DataFramePescador, "Pescador")
            st.success(f"Pescador Cadastrado {text}")

    else:
        st.subheader("Visualizar um Pescador")
        st.dataframe(DataFramePescador)
        pescador = st.selectbox("Selecione os pescadores", DataFramePescador["Nome"])
