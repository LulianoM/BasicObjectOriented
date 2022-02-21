import streamlit as st
from classes.peixes import Fish


def FishInterface(DataFramePeixe, DataFramePescador):
    if DataFramePescador.shape[0] == 0:
        st.error(
            "Não há pescadores cadastrados! Cadastre um pescador primeiro antes de cadastrar um peixe"
        )
    else:
        firstName = st.text_input("Nome do Peixe")
        quantity = int(st.number_input("Quantidade"))
        priceUnity = float(st.number_input("Preço da Unidade"))
        if st.button("Cadastrar"):
            st.balloons()
            peixe = Fish(
                firstName=firstName, quantity=quantity, priceUnity=priceUnity, codFish=1
            )
            print(peixe)
