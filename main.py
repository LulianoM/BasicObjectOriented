from classes.importedFish import ImportedFish
from classes.fish import Fish
import streamlit as st

from streamlitInterface.fishRegistration import PeixeInterface

st.header("Peixaria")
interfaceUser = st.selectbox(
    "selecione o que deseja:", ["Mercadoria", "Pescador", "Peixaria"]
)

if interfaceUser == "Mercadoria":
    st.subheader("Cadastre a sua mercadoria")
    interfaceMercadoria = st.selectbox(
        "Selecione o tipo:", ["Peixe", "Curstáceos", "Importado"]
    )
    if interfaceMercadoria == "Peixe":
        PeixeInterface.CadastroPeixe()

    if interfaceMercadoria == "Curstáceos":
        st.header("Curstáceos")
    if interfaceMercadoria == "Importado":
        st.header("Importado")
