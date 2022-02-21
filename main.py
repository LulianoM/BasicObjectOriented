import streamlit as st
from streamlitInterface.databaseInterface import loadTables
from streamlitInterface.fishRegistration import FishInterface
from streamlitInterface.pescadorRegistration import PescadorInterface

st.markdown("# 🐟 Sistema de Cadastro e Vendas de Peixes LTDA 🐟")
st.markdown(
    "#### Esse sistema ajuda pescadores a cadastrarem os peixes que querem vender e as peixarias a comprar os mesmos.Para vender peixes é necessário se cadastrar como um Pescador, na aba pescador você consiguirá vender seus peixes."
)

DataFramePescador, DataFramePeixe = loadTables()
st.dataframe(DataFramePescador)

TypeSelect = st.selectbox(
    "Selecione a sua aba para preferência:", ["Pescador", "Peixaria", "Mercadoria"]
)

if TypeSelect == "Pescador":
    PescadorInterface(DataFramePescador)
elif TypeSelect == "Peixaria":
    st.title("Peixaria")
else:
    FishInterface(DataFramePeixe, DataFramePescador)
