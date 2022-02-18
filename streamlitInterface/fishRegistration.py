import streamlit as st
from classes.fish import Fish


class PeixeInterface:
    def CadastroPeixe():
        firstName = st.text_input("Nome do Peixe")
        quantity = int(st.number_input("Quantidade"))
        priceUnity = float(st.number_input("Preço da Unidade"))
        if st.button("Cadastrar"):
            st.balloons()
            peixe = Fish(
                firstName=firstName, quantity=quantity, priceUnity=priceUnity, codFish=1
            )
            print(peixe)
