from classes.pescador import Pescador


class Tools:
    def SeriesToPescador(PescadorSeries):
        return Pescador(
            Nome=PescadorSeries.Nome.values[0],
            CodPescador=PescadorSeries.CodPescador.values[0],
            Embarcacao=PescadorSeries.Embarcacao.values[0],
            Wallet=PescadorSeries.Wallet.values[0],
            qtd_peixe=PescadorSeries.qtd_peixe.values[0],
        )
